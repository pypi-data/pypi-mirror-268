from rclpy.node import Node
from raya.controllers.base_controller import BaseController


class AnalyticsController(BaseController):

    def __init__(self, name: str, node: Node, interface: RayaInterface,
                 extra_info):
        pass

    async def track(self, event_name: str, parameters: dict):
        pass
