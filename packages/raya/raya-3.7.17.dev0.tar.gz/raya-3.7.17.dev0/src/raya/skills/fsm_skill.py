from typing import NoReturn
from raya.skills.skill import RayaSkill


class RayaFSMException(Exception):
    pass


class RayaFSMAlreadyRegisteredFSM(RayaFSMException):
    pass


class RayaFSMMissinTransition(RayaFSMException):
    pass


class RayaFSMNotCallableMethod(RayaFSMException):
    pass


class RayaFSMNotAsyncMethod(RayaFSMException):
    pass


class RayaFSMInvalidState(RayaFSMException):
    pass


class RayaFSMInvalidInitialState(RayaFSMException):
    pass


class RayaFSMInvalidEndState(RayaFSMException):
    pass


class RayaFSMUnknownState(RayaFSMException):
    pass


class RayaFSMInvalidTransition(RayaFSMException):
    pass


class RayaFSMNotRunning(RayaFSMException):
    pass


class RayaFSMInvalidErrorCode(RayaFSMException):
    pass


class RayaFSMMissingRequiredArgument(RayaFSMException):
    pass


class _RayaFSMSetStateControlledException(Exception):
    pass


class RayaFSMSkill(RayaSkill):

    def __init__(self, app, name: str = None):
        pass

    def set_state(self, state) -> NoReturn:
        pass

    async def main(self):
        return
