import typing
from rclpy.node import Node
from raya.logger import DEPRECATION_NEW_METHOD
from raya.enumerations import IMAGE_TYPE
from raya.controllers.base_controller import BaseController


class CamerasController(BaseController):

    def __init__(self, name: str, node: Node, app, extra_info: dict):
        pass

    def is_camera_enabled(self,
                          camera_name: str,
                          img_type: IMAGE_TYPE = IMAGE_TYPE.COLOR):
        pass

    @DEPRECATION_NEW_METHOD('available_cameras')
    def available_color_cameras(self):
        return

    def available_cameras(self, img_type: IMAGE_TYPE = IMAGE_TYPE.COLOR):
        pass

    @DEPRECATION_NEW_METHOD('enable_camera')
    async def enable_color_camera(self, camera_name: str):
        pass

    async def enable_camera(self,
                            camera_name: str,
                            img_type: IMAGE_TYPE = IMAGE_TYPE.COLOR):
        pass

    @DEPRECATION_NEW_METHOD('disable_camera')
    async def disable_color_camera(self, camera_name: str):
        pass

    async def disable_camera(self,
                             camera_name: str,
                             img_type: IMAGE_TYPE = IMAGE_TYPE.COLOR):
        pass

    async def get_next_frame(self,
                             camera_name: str,
                             compressed: bool = False,
                             get_timestamp: bool = False,
                             timeout: float = (-1.0),
                             img_type: IMAGE_TYPE = IMAGE_TYPE.COLOR):
        pass

    @DEPRECATION_NEW_METHOD('create_frame_listener')
    def create_color_frame_listener(self,
                                    camera_name: str,
                                    callback: typing.Callable = None,
                                    callback_async: typing.Callable = None,
                                    compressed: bool = False):
        pass

    def create_frame_listener(self,
                              camera_name: str,
                              callback: typing.Callable = None,
                              callback_async: typing.Callable = None,
                              compressed: bool = False,
                              img_type: IMAGE_TYPE = IMAGE_TYPE.COLOR):
        pass

    def delete_listener(self,
                        camera_name: str,
                        img_type: IMAGE_TYPE = IMAGE_TYPE.COLOR):
        pass

    async def enable_streaming(self, camera_name: str):
        return

    async def disable_streaming(self, camera_name: str):
        return

    async def get_3D_point(self, camera_name: str, pixel: tuple) -> tuple:
        return
