from typing import NoReturn
from raya.exceptions_bases import RayaException
from raya.exceptions_bases import RayaCodedException


class RayaFSMException(RayaException):
    pass


class RayaFSMAlreadyRegisteredFSM(RayaFSMException):
    pass


class RayaFSMMissinTick(RayaFSMException):
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


class _RayaFSMSetStateControlledException(RayaFSMException):
    pass


class RayaFSMAborted(RayaCodedException, RayaFSMException):
    pass


class FSMArgs():
    pass


class BaseTransitions():

    def __init__(self):
        self.args = None

    def set_state(self, state) -> NoReturn:
        pass

    def abort(self, code, msg) -> NoReturn:
        pass


class BaseActions():

    def __init__(self):
        self.args = None

    def abort(self, code, msg) -> NoReturn:
        pass


class FSM():

    def __init__(self,
                 app=None,
                 name=None,
                 path='FSMs',
                 log_transitions=False):
        pass

    def was_successful(self):
        return

    def get_error(self):
        return

    def get_current_state(self):
        return

    def is_running(self):
        return

    def has_finished(self):
        return

    def restart(self):
        pass

    async def run_and_await(self, tick_period=0.1, **kargs):
        pass

    async def run_in_background(self, tick_period=0.1, **kargs):
        pass

    async def raise_last_execution_exception(self):
        pass

    async def tick(self):
        return
