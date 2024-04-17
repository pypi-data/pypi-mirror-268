import pyvista as pv
import argparse
from pyvista.trame.ui import plotter_ui
from trame.app import get_server
from trame.ui.vuetify3 import VAppLayout
from trame.widgets import vuetify3 as vuetify
from trame.widgets import html
from aiohttp import web
from trame.decorators import TrameApp, change, controller

import logging
import os
import numpy as np
import time, threading
import asyncio
from abc import ABC, abstractmethod

from typing import Dict

root_logger = logging.getLogger("solidipes")
root_logger.propagate = True
root_logger.setLevel(logging.INFO)
if "FULL_SOLIDIPES_LOG" not in os.environ:
    root_logger.setLevel(logging.INFO)


@TrameApp()
class MeshViewer:
    """ A Trame server class that manage the view of a 3d mesh and its controls """

    def __init__(self, mesh=None, plotter=None, server=None, port=8080):

        root_logger.info("Server started")
        pv.OFF_SCREEN = True

        self.scalar_bar_exist = None
        if server is None:
            self.server = get_server(port=port)
        else:
            self.server = server
        self.slider_playing = False
        self.path = None

        self.mesh = None
        self.clean_mesh = None

        self.style = {
            "background-color": "black",
            "font-color": "white"
        }

        self.pl = self.setup_pl()

        setattr(self, "on_server_bind", self.server.controller.add("on_server_bind")(self.on_server_bind))

        # Setup api endpoints
        self.my_routes = [
            web.get("/select_mesh", self.change_mesh),
            web.get("/init_connection", self.init_connection),
        ]

        self.setup_state()

        self.setup_timer()

        self.loop = asyncio.get_event_loop()

        self.mesh_array = None

        self.actor = None
        self.width = 800
        self.height = 900
        self.ui = self.build_ui()

    def setup_pl(self) -> pv.Plotter:
        """ Setup all class attributes related to the pyvista Plotter """
        # Create the plotter and add its styles
        pl = pv.Plotter()
        pl.background_color = self.style["background-color"]
        pl.theme.font.color = self.style["font-color"]
        # Initialize attribute related to the plotter
        self.bounds_scalar = None
        self.scalar_bar_exist = False
        self.scalar_bar_mapper = None
        return pl

    def setup_state(self):
        """ Set up all the state variables to initial values """
        self.state.is_full_screen = False
        self.state.mesh_representation = self.state.options[0] if self.state.options is not None else None
        self.state.warped_field = None

        # Option's dropdown
        self.state.options = [None]
        self.state.options_warp = [None]

        # Inputs
        self.state.warp_input = 0
        self.state.wireframe_on = True
        self.state.slider_value = 0
        self.state.play_pause_icon = "mdi-play"

        # Choice save
        self.prev_bar_repr = self.state.mesh_representation
        self.prev_wrap = "0"

    def setup_timer(self):
        """ Set up the timer callback and timeout """
        self.timer_timeout = 0.25
        self.timer = threading.Thread(target=self.timer_callback)
        self.sequence_bounds = [0, 70]

    @change("mesh_representation")
    def update_mesh_representation(self, mesh_representation, **kwargs):
        """ This function is automatically called when the state 'mesh_representation' is changed.
        This state is used to determine which vector field is shown """
        # Remove the scalar bar representing the last vector field shown
        if self.mesh is not None and self.mesh.active_scalars is not None:
            self.pl.remove_scalar_bar()
        self.prev_bar_repr = mesh_representation

        # Replace the string input "None" with None
        if mesh_representation == "None":
            self.state.mesh_representation = None

        # Set all element of the mesh sequence with the same field shown
        for i in range(self.sequence_bounds[1]):
            if self.mesh_array is not None:
                self.mesh_array[i].set_active_scalars(self.state.mesh_representation)

        # Update ui elements
        self.update_mesh_from_index(self.state.slider_value)
        self.update_warp_input(self.state.warp_input)
        self.ui = self.build_ui()

    @change("warp_input")
    def update_warp_input(self, warp_input, **kwargs):
        """ This function is automatically called when the state 'warp_input' is changed. """
        try:

            new_warp = float(warp_input)
            dim = self.mesh.point_data.get_array(self.state.mesh_representation).ndim  # 1 if scalar, 2 if vector

            # if the dimension of the field is 1 we can warp by a scalar, else we warp by a vector
            if dim == 1:
                new_pyvista_mesh = self.clean_mesh.warp_by_scalar(self.state.warped_field,
                                                                  factor=new_warp)
            else:
                new_pyvista_mesh = self.clean_mesh.warp_by_vector(self.state.warped_field,
                                                                  factor=new_warp)
            self.prev_wrap = self.state.warp_input
            # Show the mesh that was warped
            self.replace_mesh(new_pyvista_mesh)

        except ValueError as e:
            print(e)
            pass
        except Exception as e:
            print(e)

    @change("warped_field")
    def update_warped_field(self, warped_field, **kwargs):
        """ This function is automatically called when the state 'warped_field' is changed.
         This state is used to describe which vector field of the mesh we want to warp. """
        if warped_field is None or warped_field == "None":
            return
        self.update_warp_input(warped_field=warped_field)

    @change("wireframe_on")
    def update_wireframe_on(self, **kwargs):
        """ This function is automatically called when the state 'wireframe_on' is changed.
         This state is used to store whether we should show the wireframe of the mesh or the plain mesh. """
        self.replace_mesh(self.mesh)

    @change("slider_value")
    def slider_value_change(self, slider_value, **kwargs):
        """ This function is automatically called when the state 'slider_value' is changed.
         This state is used to store the frame to actually displayed in a sequence. """
        self.update_mesh_from_index(int(slider_value))
        self.state.warp_input = 0

    @property
    def state(self):
        return self.server.state

    @property
    def ctrl(self):
        return self.server.controller

    def timer_callback(self):
        """ This function is called on all timer tick and update the mesh viewed to animate a sequence of mesh playing """

        # The animation needs to stop when the server stop or if the animation was paused by the user
        while self.slider_playing and self.server.running:
            # Increment the counter while keeping it within the bound of the mesh sequence
            self.state.slider_value = (self.state.slider_value + 1) % self.sequence_bounds[1]
            # Call function on the main thread using thread safe method to update the server states and ui
            self.loop.call_soon_threadsafe(self.update_mesh_from_index, self.state.slider_value)
            self.loop.call_soon_threadsafe(self.server.force_state_push, "slider_value")

            time.sleep(self.timer_timeout)
        # After the animation was stopped, reset the timer
        self.timer = threading.Thread(target=self.timer_callback)

    def update_mesh_from_index(self, idx):
        """
        Update the mesh displayed in the plotter using its index in the sequence
        Args:
            idx: an int setting the index of the mesh to show
        """
        if self.mesh_array is not None:
            if idx < self.sequence_bounds[1]:
                self.clean_mesh = self.mesh_array[idx]
                self.replace_mesh(self.mesh_array[idx])

    def handle_new_mesh(self, mesh_path, seq_len=1):
        """
        This function handles the loading of new mesh in the server
        Args:
            mesh_path: the path of the mesh
            seq_len: if it's a sequence of mesh, give its length else its one
        """
        self.mesh_array = []
        # If the seqence is of length 1, just load it
        if seq_len == 1:
            if not os.path.exists(mesh_path):
                root_logger.error(f"Error, the file {mesh_path} does not exist")
                return
            self.mesh_array.append(pv.read(mesh_path))
            return
        # If the mesh is a sequence, then format its path and load all element in the mesh array
        for i in range(self.sequence_bounds[1]):
            path = self.path % i
            if not os.path.exists(path):
                root_logger.error(f"Error, the file {path} does not exist")
                return
            self.mesh_array.append(pv.read(path))

    async def change_mesh(self, request):
        """
        This function is called when a request to '/select_mesh' is made
        Args:
            request: the request received

        Returns:
            a http status 200 if there was no error, else a http status 400
        """
        request_body: Dict[str, str] = await request.json()
        # Retrieve information from the request
        self.path = request_body.get("mesh_path", None)
        self.width = request_body.get("width", self.width)
        self.height = request_body.get("height", self.height)
        self.sequence_bounds[1] = request_body.get("nbr_frames", self.sequence_bounds[1])
        if self.path is None:
            root_logger.error("No filepath found in the change mesh request")
            return web.json_response({"error": "Error : No filepath found in the change mesh request"}, status=400)

        # Reset the viewer to an empty state
        self.clear_viewer()

        # Get the mesh and prepare it to be displayed
        self.handle_new_mesh(self.path, self.sequence_bounds[1])
        self.replace_mesh(self.mesh_array[0])

        # Prepare ui elements that depends on the mesh
        self.state.options = self.mesh_array[0].array_names.copy()
        self.state.options.insert(0, "None")
        self.state.options_warp = self.state.options.copy()

        # Show the new mesh in the viewers and its controls
        self.computes_bounds_scalar()
        self.update_ui()
        self.pl.reset_camera()

        # If the height allocated by the streamlit component, ask for more space in the response of the request
        response_body = {}
        if self.height - self.estimate_controller_height()[1] < 700:
            response_body["request_space"] = 1.65 * self.height
        return web.json_response(response_body, status=200)

    def clear_scalar_bars(self):
        """ Remove all the scalar bars shown on the plotter """
        if self.pl is None:
            return
        bar_to_remove = [key for key in self.pl.scalar_bars.keys()]
        [self.pl.remove_scalar_bar(title=key) for key in bar_to_remove]

    def clear_viewer(self):
        """ Reset the viewer and its related attribute to an empty viewer """
        self.clear_scalar_bars()
        self.state.slider_value = 0
        self.state.mesh_representation = None

    def compute_field_interval(self, field=None):
        """
        Compute the min and max of a field of vector over all it's frame ot get the all-time min and max to get the upper
        and lower bound of the scalar bar
        Args:
            field: the field you want to compute the bounds

        Returns: (min, max), it returns a tuple with the min and max

        """
        # If the field is None get the default field on which to compute the min and max
        if field is None:
            field = self.state.mesh_representation
        if field is None or field == "None":
            field = self.state.options[1]
        # Loop over all the images and find the max of the array and the min
        max_bound = -np.inf
        min_bound = np.inf
        for i in range(self.sequence_bounds[1]):
            l_max = self.mesh_array[i].get_array(field).max()
            l_min = self.mesh_array[i].get_array(field).min()
            if l_max > max_bound:
                max_bound = l_max
            if l_min < min_bound:
                min_bound = l_min
        return min_bound, max_bound

    def show_scalar_bar(self, field=None):
        """
        Show the scalar bar associated with the field
        Args:
            field: The associated field of the bar that you want to show

        """
        if self.mesh_array is None:
            return

        # If the field is not specified try to get the actual field displayed in the plotter
        if field is None:
            field = self.state.mesh_representation
        if field is None:
            return

        # Get the bounds of the bar or compute it if it does not exist
        if self.bounds_scalar is None:
            self.computes_bounds_scalar()

        # Create the pyvista scalar bar
        bounds = self.bounds_scalar.get(field, None)
        if bounds is not None:
            self.pl.mapper.lookup_table.SetTableRange(bounds[0], bounds[1])
            self.pl.add_scalar_bar(self.state.mesh_representation)

        # Return the mapper to display the good max and min value on the bar
        return self.pl.mapper

    def computes_bounds_scalar(self):
        """ Compute the bounds of all the scalars of the mesh and store it in an attribute
        to avoid doing all the computation everytime a bar is shown """
        if self.state.options is None:
            return

        # Store bounds and mapper for all the fields available except "None" which is the first one of the options array
        self.bounds_scalar = {}
        for field in self.state.options[1:]:
            self.bounds_scalar[field] = self.compute_field_interval(field)

    def replace_mesh(self, new_mesh):
        """
        Change the mesh displayed in the plotter and its related data
        Args:
            new_mesh: the new mesh to display
        """
        if new_mesh is None:
            return

        # set custom style
        kwargs_plot = {}
        if self.state.wireframe_on:
            kwargs_plot["style"] = "wireframe"

        # update mesh and set its active scalar field, as well as adding the scalar bar
        self.mesh = new_mesh

        # Set the active scalar and create it's scalar bar if it does not exist
        self.mesh.set_active_scalars(self.state.mesh_representation)

        self.pl.mapper = self.show_scalar_bar(self.state.mesh_representation)

        # Replace actor with the new mesh (automatically update the actor because they have the same name)
        self.actor = self.pl.add_mesh(self.mesh, style="wireframe" if self.state.wireframe_on else None,
                                      name="displayed_mesh", show_scalar_bar=True,
                                      scalar_bar_args={"mapper": self.pl.mapper})

    def start_server(self):
        """ Start the server """
        try:
            self.server.start()
        except KeyboardInterrupt:
            # Stop the thread that manage the play of the mesh sequence
            self.timer.join()  # Wait for the timer thread to finish

    def update_ui(self):
        """ Force to redraw the ui """
        if self.mesh is not None and self.mesh.active_scalars is not None:
            self.pl.remove_scalar_bar()
        self.ui = self.build_ui()

    def option_dropdown(self):
        """ This function return the ui element displaying the mesh_representation dropdown """
        return vuetify.VSelect(
            v_model=("mesh_representation", "None"),
            items=("options", self.state.options),
            label="Representation",
            hide_details=True,
            dense=True,
            outlined=True,
            classes="pt-1",
        )

    def build_slider(self):
        """
        This function build the ui component containing the slider to select the frame displayed
        Returns: a row containing a play-pause button and a slider

        """
        row = html.Div(style='display:flex;justify-content:center;align-content:center;gap:20px;')
        with row:
            with vuetify.VBtn(
                    icon=True,
                    click=self.play_button
            ):
                vuetify.VIcon("{{ play_pause_icon }}")
            html.Div("{{ slider_value }}")
            vuetify.VSlider(
                ref="slider",
                label="",
                min=self.sequence_bounds[0],
                max=self.sequence_bounds[1] - 1,
                v_model=("slider_value", 8),
                step=1
            )
        return row

    @controller.set("play_button")
    def play_button(self):
        """ This function is called the play-pause button of the slider is played and manage the state
        of the timer that updates the frame displayed in a periodic manner. """
        if self.sequence_bounds[1] <= 1:
            root_logger.error("Impossible to start the sequence since it's a unique mesh")
            return

        # Invert the state of the play button and if it's playing start the timer updating frame at a fixed interval
        self.slider_playing = not self.slider_playing
        if self.slider_playing and not self.timer.is_alive():
            self.state.play_pause_icon = "mdi-pause"
            self.timer.start()
        else:
            self.state.play_pause_icon = "mdi-play"
        self.update_ui()

    def build_warp_option(self):
        """
        This function build the dropdown used to select which field is being warped
        Returns: a vuetify dropdown component
        """
        return vuetify.VSelect(
            v_model=("warped_field"),
            items=("options_warp", self.state.options_warp),
            label="Warped Field",
            hide_details=True,
            dense=True,
            outlined=True,
            classes="pt-1",
        )

    def build_warper(self):
        """
        build the ui component responsible for the warping which is in more details a column with a dropdown and an
         input of type number
        Returns: a vuetify Column containing all the element of the component
        """
        warper = vuetify.VCol(cols="6")
        with warper:
            self.build_warp_option()

            # if self.state.warped_field != "None" and self.state.warped_field is not None:
            html.Input(type="number", label="warp",
                       v_model=("warp_input", 0.0),
                       ref=f"warp-input",
                       step="1"
                       )
        return warper

    def build_mesh_control_layout(self):
        """
        This function return all the control part of the ui composed of:
            - The dropdown to select the vector field to display
            - The warp control
            - The slider controller
            - other various control
        Returns: a vuetify component representing all the control layout

        """
        layout = html.Div()
        with (layout):
            with vuetify.VRow(dense=True):
                with vuetify.VCol(cols="6"):
                    # If there are options show the dropdown
                    if self.state.options[0] is not None and len(self.state.options) > 1:
                        self.option_dropdown()
                # If there are options create the warper layout
                # if len(self.state.options) > 1:
                self.build_warper()
            vuetify.VCheckbox(v_model=("wireframe_on",), label="Wireframe on", id="wireframe_checkbox")
            # If the viewer display a sequence of mesh show the slider
            if self.sequence_bounds[1] != 1:
                self.build_slider()

            with vuetify.VBtn(click=self.request_full, style="position: absolute; bottom:25px; right:25px;", icon=True):
                vuetify.VIcon("mdi-fullscreen" if not self.state.is_full_screen else "mdi-fullscreen-exit")
        return layout

    def estimate_controller_height(self):
        """
        This function make an estimation of the size the component might required in the worst case
        Returns: The computed worst case height
        """
        # Get the worst dimension of any warper to find how many input would be required and add the height
        # of all these input to the default height
        if self.mesh_array is not None and self.state.mesh_representation is not None:
            ndim = self.mesh_array[0].get_array(self.state.mesh_representation).shape[1]
            return 30 * ndim, 9 * 30
        return 0.2 * self.height, 9 * 30

    def build_ui(self):
        """
        Build all the ui frontend with all different components
        Returns:
            a VAppLayout for the server
        """
        control_height = self.estimate_controller_height()[0]
        # Define some styling variables
        if not self.state.is_full_screen:
            plotter_height = self.height - control_height
            plotter_height = f"{plotter_height}px"
            width = "100%"
        else:
            plotter_height = "100%"
            width = "100%"

        with VAppLayout(self.server) as layout:
            with layout.root:
                with html.Div(
                        style=f"height: {self.height}px ;width:{width}"):  # add the following arg: style="height: 100vh; width:100vw" to have the plotter taking all screen
                    with html.Div(ref="container", style=f"height:{plotter_height};padding: 0;"):
                        # Create the plotter section
                        with vuetify.VCol(style=f"height:{plotter_height};padding: 0;"):
                            # If the slider is playing we force the app to use remote rendering to avoid bug
                            # with local rendering
                            if self.slider_playing:
                                plotter_ui(self.pl, default_server_rendering=True, mode="server",
                                           style="width: 100%; height:100%;background-color: black;")
                            else:
                                plotter_ui(self.pl, default_server_rendering=True,
                                           style="width: 100%; height:100%;background-color: black;")
                    with vuetify.VCol(style=f"height:{control_height}px;padding: 0;width:100%;"):
                        # Create the whole control layout
                        self.build_mesh_control_layout()
            return layout

    def on_server_bind(self, wslink_server):
        """
        When the server is bind, add api endpoint to it
        Args:
            wslink_server: the socket manager of the server
        """
        wslink_server.app.add_routes(self.my_routes)

    async def init_connection(self, request):
        """
        Base api endpoint on '/init_connection' to inform the client of all the endpoints available and their locations
        Args:
            request: the request made to this endpoint

        Returns:
            a json with all information about endpoints required and a success status 200
        """
        response_body = {
            "select_mesh": "/select_mesh",
            "host": f"http://127.0.0.1:{self.server.port}"
        }
        return web.json_response(response_body, status=200)

    def request_full(self):
        """ Make a js call to request full screen on the iframe """
        self.server.js_call("container", "requestFullscreen")
        self.state.is_full_screen = not self.state.is_full_screen
        self.update_ui()


class Component(ABC):
    def __init__(self, state, ctrl):
        self.supported_handler = ["change"]
        self.state = state
        self.ctrl = ctrl

    # add corresponding decorator to fucntion (change or set)
    @abstractmethod
    def handler(self, new_value, **kwargs):
        pass

    @abstractmethod
    def render(self):
        pass


if __name__ == "__main__":
    # Add command line argument and support
    parser = argparse.ArgumentParser(description='Launch a trame server instance')
    # Add the port argument that allow user to specify the port to use for the server from command line
    parser.add_argument('--port', type=int, help='Specify the port of the server')
    # Add --server flag that is used to specify whether to use the trame as only a server and block the
    # automatic open of a browser
    parser.add_argument('--server', action="store_true", help='Specify if the trame is opened as a server')
    args = parser.parse_args()
    mv = MeshViewer(port=args.port)
    mv.start_server()
