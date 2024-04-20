import typing
from typing import NoReturn
from raya.controllers import ALL_CONTROLLERS_UNION
from raya.exceptions import *


class RayaSkill():

    def __init__(self, app):
        self.log = self.__app.create_logger(f'skill.{type(self).__name__}')
        self.setup_args = {}
        self.execute_args = {}

    @__only_in_setup('enable_controller')
    async def enable_controller(self, ctlr_name: str) -> ALL_CONTROLLERS_UNION:
        return

    @__only_in_setup('get_controller')
    async def get_controller(self, ctlr_name: str) -> ALL_CONTROLLERS_UNION:
        return

    async def sleep(self, sleep_time: float):
        pass

    def register_skill(self, skill_cls):
        return

    async def send_feedback(self, feedback_dict):
        pass

    def abort(self, error_code, error_msg) -> NoReturn:
        pass


class RayaSkillHandler():

    def __init__(self, app, skill_cls):
        pass

    async def execute_setup(self,
                            setup_args: dict = {},
                            callback_feedback: typing.Coroutine = None,
                            callback_done: typing.Coroutine = None,
                            wait=True):
        pass

    async def wait_setup(self):
        pass

    async def execute_main(self,
                           execute_args: dict = {},
                           callback_feedback: typing.Coroutine = None,
                           callback_done: typing.Coroutine = None,
                           wait=True):
        pass

    async def wait_main(self):
        pass

    async def execute_finish(self,
                             callback_feedback: typing.Coroutine = None,
                             callback_done: typing.Coroutine = None,
                             wait=True):
        pass

    async def wait_finish(self):
        pass

    async def run(self,
                  setup_args: dict = {},
                  execute_args: dict = {},
                  callback_feedback: typing.Coroutine = None,
                  callback_done: typing.Coroutine = None,
                  wait=True):
        pass

    async def wait_run(self):
        pass

    def raise_last_execution_exception(self):
        pass

    def get_execution_state(self):
        return
