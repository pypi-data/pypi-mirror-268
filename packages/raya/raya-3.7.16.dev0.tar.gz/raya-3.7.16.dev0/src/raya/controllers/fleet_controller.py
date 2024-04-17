from rclpy.node import Node
from raya.exceptions import *
from raya.controllers.base_controller import BaseController
from raya.enumerations import *
from raya.constants import *


class FleetController(BaseController):

    def __init__(self, name: str, node: Node, interface: RayaInterface,
                 extra_info):
        self.task_id = interface.get_fleet_arguments('task_id')

    def set_msgs_from_fleet_callback(self, callback=None, callback_async=None):
        pass

    async def request_action(self,
                             title: str,
                             message: str,
                             task_id: str = None,
                             timeout: float = 30.0):
        return

    async def finish_task(self,
                          result: FLEET_FINISH_STATUS,
                          task_id: str = None,
                          message: str = None):
        pass

    async def update_app_status(self,
                                task_id: str = None,
                                status: FLEET_UPDATE_STATUS = None,
                                message: str = None):
        pass

    async def get_path(self, x: float, y: float, path_id: str = None):
        return

    async def can_navigate(self, x: float, y: float, path_id: str = None):
        return

    async def open_camera_stream(self,
                                 title: str,
                                 button_ok_txt: str,
                                 subtitle: str = '',
                                 default_camera: str = '',
                                 button_cancel_txt: str = '',
                                 task_id: str = None):
        return

    def check_last_exception(self):
        pass

    async def request_abort_pending_tasks(self, app_names: list = []):
        pass
