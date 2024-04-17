from enum import IntEnum, Enum, auto


# GENERAL


class POSITION_UNIT(IntEnum):
    '''
    Enumeration to set the unit of the coordinates in a map.
    POSITION_UNIT.PIXELS : Based on the pixel of the image map.
    POSITION_UNIT.METERS : Meters
    '''
    PIXELS = 0
    METERS = 1



class ANGLE_UNIT(IntEnum):
    '''
    Enumeration to set the angles unit.
    ANGLE_UNIT.DEGREES : Degrees
    ANGLE_UNIT.RADIANS : Radians
    '''
    DEGREES = 0
    RADIANS = 1



class SHAPE_TYPE(IntEnum):
    '''
    Enumeration to define the type of shape for obstacles.
    SHAPE_TYPE.BOX : Box
    SHAPE_TYPE.SPHERE : Sphere
    SHAPE_TYPE.CYLINDER : Cylinder
    SHAPE_TYPE.CONE : Cone
    '''
    BOX = 1
    SPHERE = 2
    CYLINDER = 3
    CONE = 4



class SHAPE_DIMENSION(IntEnum):
    '''
    Enumeration to define the array position to define the shape obstacles dimensions.
    SHAPE_DIMENSION.BOX_X : Box width
    SHAPE_DIMENSION.BOX_Y : Box large
    SHAPE_DIMENSION.BOX_Z : Box height

    SHAPE_DIMENSION.SPHERE_RADIUS : Sphere radius

    SHAPE_DIMENSION.CYLINDER_HEIGHT : Cylinder height
    SHAPE_DIMENSION.CYLINDER_RADIUS : Cylinder radius

    SHAPE_DIMENSION.CONE_HEIGHT : Cone height
    SHAPE_DIMENSION.CONE_RADIUS : Cone radius
    '''
    BOX_X = 0
    BOX_Y = 1
    BOX_Z = 2

    SPHERE_RADIUS = 0

    CYLINDER_HEIGHT = 0
    CYLINDER_RADIUS = 1

    CONE_HEIGHT = 0
    CONE_RADIUS = 1



# ARMS


class ARMS_JOINT_TYPE(IntEnum):
    '''
    Enumeration to define the type of arm joint
    ARMS_JOINT_TYPE.ROTATIONAL: Rotational joint
    ARMS_JOINT_TYPE.LINEAR: Linear joint
    '''
    NOT_DEFINED = 0
    LINEAR = 1
    ROTATIONAL = 2




class ARMS_MANAGE_ACTIONS(Enum):
    '''
    Enumeration to set the action to take when the user wants to manage predefined data
    ARMS_MANAGE_ACTIONS.GET : Getting the predefined data
    ARMS_MANAGE_ACTIONS.EDIT: Editing the predefined data
    ARMS_MANAGE_ACTIONS.REMOVE: Removing the predefined data
    ARMS_MANAGE_ACTIONS.GET_INFORMATION: Getting informartion related to the predefined data
    ARMS_MANAGE_ACTIONS.CREATE: Creating a new predefined data
    '''
    GET = 'get'
    EDIT = 'edit'
    REMOVE = 'remove'
    GET_INFORMATION = 'get_info'
    CREATE = 'create'



# UI


class UI_INPUT_TYPE(Enum):
    '''
    Enumeration to set input type
    UI_INPUT_TYPE.TEXT: user can only input a-z or A-Z
    UI_INPUT_TYPE.NUMERIC: user can only input numbers
    '''
    TEXT = 'text'
    NUMERIC = 'numeric'



class UI_THEME_TYPE(Enum):
    '''
    Enumeration to set the UI theme type
    UI_THEME_TYPE.DARK : will specify to set background to dark
    UI_THEME_TYPE.WHITE : will specify to set background to white
    '''
    DARK = 'DARK'
    WHITE = 'WHITE'



class UI_MODAL_TYPE(Enum):
    '''
    Enumeration to set the UI modal type
    UI_MODAL_TYPE.INFO : specify that this is an informative component
    UI_MODAL_TYPE.SUCCESS : showing a message indicating that the operation was successful
    UI_MODAL_TYPE.ERROR : showing a message alerting about of a bad procedure
    '''
    INFO = 'info'
    SUCCESS = 'success'
    ERROR = 'error'



class UI_TITLE_SIZE(Enum):
    '''
    Enumeration to set the title size.
    UI_TITLE_SIZE.SMALL : Small size
    UI_TITLE_SIZE.MEDIUM : Medium size
    UI_TITLE_SIZE.LARGE : Large size
    '''
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'



class UI_ANIMATION_TYPE(Enum):
    '''
    Enumeration to set the animation format.
    UI_ANIMATION_TYPE.LOTTIE : Lottie format
    UI_ANIMATION_TYPE.PNG : PNG format
    UI_ANIMATION_TYPE.JPEG : JPEG format
    UI_ANIMATION_TYPE.GIF : GIF format
    UI_ANIMATION_TYPE.URL : URL format
    '''

    LOTTIE = 'LOTTIE'
    PNG = 'BASE64'
    JPEG = 'BASE64' # in reality, for UI side, it is the same as PNG
    GIF = 'BASE64'
    URL = 'URL'



class UI_SPLIT_TYPE(Enum):
    '''
    Emumeration of all the ui methods options.
    UI_SPLIT_TYPE.DISPLAY_MODAL : Display a modal
    UI_SPLIT_TYPE.DISPLAY_SCREEN : Display a screen
    UI_SPLIT_TYPE.DISPLAY_INTERACTIVE_MAP : Display an interactive map
    UI_SPLIT_TYPE.DISPLAY_ACTION_SCREEN : Display an action screen
    UI_SPLIT_TYPE.DISPLAY_INPUT_MODAL : Display an input modal
    UI_SPLIT_TYPE.DISPLAY_CHOICE_SELECTOR : Display a choice selector
    UI_SPLIT_TYPE.DISPLAY_ANIMATION : Display an animation
    '''
    DISPLAY_MODAL = 'Modal'
    DISPLAY_SCREEN = 'DisplayScreen'
    DISPLAY_INTERACTIVE_MAP = 'InteractiveMap'
    DISPLAY_ACTION_SCREEN = 'CallToAction'
    DISPLAY_INPUT_MODAL = 'InputModal'
    DISPLAY_CHOICE_SELECTOR = 'Choice'
    DISPLAY_ANIMATION = 'Animation'
    


class UI_MODAL_SIZE(Enum):
    '''
    Enumeration to set the size of the modal.
    UI_MODAL_SIZE.NORMAL : Normal size
    UI_MODAL_SIZE.BIG : Big size
    '''
    NORMAL = 'Normal'
    BIG = 'Big'



#LEDS


class LEDS_EXECUTION_CONTROL(IntEnum):
    '''
    Enumeration to set the animation to be overriden.
    LEDS_EXECUTION_CONTROL.OVERRIDE : Overide current animation
    LEDS_EXECUTION_CONTROL.ADD_TO_QUEUE : Insert animation to serial queue
    LEDS_EXECUTION_CONTROL.AFTER_CURRENT : Run animation at the end of current animation
    '''
    OVERRIDE = 0
    ADD_TO_QUEUE = 1
    AFTER_CURRENT = 2
    


# FLEET

class FLEET_FINISH_STATUS(Enum):
    '''
    Enumeration to set indicate whether the app finished successfully or not.
    FLEET_FINISH_STATUS.SUCCESS : The app finished successfully.
    FLEET_FINISH_STATUS.FAILED : The app finished with errors or did not finish as expected.
    '''
    SUCCESS = 'Done'
    FAILED = 'Failed'

    

class FLEET_UPDATE_STATUS(Enum):
    '''
    Enumeration indicate how is the progress of the application.
    FLEET_UPDATE_STATUS.INFO : General information to the user.
    FLEET_UPDATE_STATUS.WARNING : Warning message to the user.
    FLEET_UPDATE_STATUS.SUCCESS : Success message to the user.
    FLEET_UPDATE_STATUS.ERROR : Error message to the user.
    '''
    INFO = 'Info'
    WARNING = 'Warning'
    SUCCESS = 'Success'
    ERROR = 'Error'



# STATUS

class RAYA_STATUS(Enum):
    '''
    Enumeration to indicate the status of RaYa.
    RAYA_STATUS.UNKNOWN : Unknown status
    RAYA_STATUS.AVAILABLE : Available status and can run apps
    RAYA_STATUS.BUSY : The robot is already running an app
    RAYA_STATUS.UNAVAILABLE : Unavailable status and cannot run apps (e.g. battery low)
    '''
    UNKNOWN = 0
    AVAILABLE = 1
    BUSY = 2
    UNAVAILABLE = 3
    ERROR = 4

    
class RAYA_STATUS_REASON(Enum):
    '''
    Enumeration to indicate the reason of the status of RaYa.
    RAYA_STATUS_REASON.UNKNOWN : Unknown reason
    RAYA_STATUS_REASON.BATTERY_NOT_CONNECTED : Battery not connected
    RAYA_STATUS_REASON.BATTERY_NOT_CHARGING : Battery not charging
    RAYA_STATUS_REASON.LOW_BATTERY : Low battery but still run apps
    RAYA_STATUS_REASON.CRITICAL_LOW_BATTERY : Critical low battery, any running app will be closed
    RAYA_STATUS_REASON.CHARGING_NOT_AVAILABLE : Charging not available
    RAYA_STATUS_REASON.APPS_ARE_RUNNING : There is already an app running
    '''
    UNKNOWN = 0
    BATTERY_NOT_CONNECTED = 1
    BATTERY_NOT_CHARGING = 2
    LOW_BATTERY = 3
    CRITICAL_LOW_BATTERY = 4
    CHARGING_NOT_AVAILABLE = 5
    APPS_ARE_RUNNING = 6
    

class STATUS_BATTERY(Enum):
    '''
    Enumeration to indicate the status of the battery.
    STATUS_BATTERY.UNKNOWN : Unknown status
    STATUS_BATTERY.CHARGING : Charging battery
    STATUS_BATTERY.DISCHARGING : Discharging battery
    STATUS_BATTERY.NOT_CHARGING : Battery not charging
    STATUS_BATTERY.FULL : Battery full
    STATUS_BATTERY.NO_BATTERY : No battery
    STATUS_BATTERY.LOW_BATTERY : Low battery
    STATUS_BATTERY.CRITICAL_LOW_BATTERY : Critical battery
    STATUS_BATTERY.CHARGING_NOT_AVAILABLE : Charging not available
    STATUS_BATTERY.CHARGING_AVAILABLE : Charging available
    '''
    UNKNOWN = 0
    CHARGING = 1
    DISCHARGING = 2
    NOT_CHARGING = 3
    FULL = 4
    NO_BATTERY = 5
    LOW_BATTERY = 6
    CRITICAL_LOW_BATTERY = 7
    CHARGING_NOT_AVAILABLE = 8
    CHARGING_AVAILABLE = 9



class STATUS_BATTERY_HEALTH(Enum):
    '''
    Enumeration to indicate the health of the battery.
    STATUS_BATTERY_HEALTH.UNKNOWN : Unknown status
    STATUS_BATTERY_HEALTH.GOOD : Good battery
    STATUS_BATTERY_HEALTH.OVERHEAT : Overheat battery
    STATUS_BATTERY_HEALTH.DEAD : Dead battery
    STATUS_BATTERY_HEALTH.OVERVOLTAGE : Overvoltage battery
    STATUS_BATTERY_HEALTH.UNSPEC_FAILURE : Unspecified failure battery
    STATUS_BATTERY_HEALTH.COLD : Cold battery
    STATUS_BATTERY_HEALTH.WATCHDOG_TIMER_EXPIRE : Watchdog timer expire battery
    STATUS_BATTERY_HEALTH.SAFETY_TIMER_EXPIRE : Safety timer expire battery
    '''
    UNKNOWN = 0
    GOOD = 1
    OVERHEAT = 2
    DEAD = 3
    OVERVOLTAGE = 4
    UNSPEC_FAILURE = 5
    COLD = 6
    WATCHDOG_TIMER_EXPIRE = 7
    SAFETY_TIMER_EXPIRE = 8



class STATUS_BATTERY_TECHNOLOGY(Enum):
    '''
    Enumeration to indicate the technology of the battery.
    STATUS_BATTERY_TECHNOLOGY.UNKNOWN : Unknown technology
    STATUS_BATTERY_TECHNOLOGY.NIMH : Nickel Metal Hydride technology
    STATUS_BATTERY_TECHNOLOGY.LION : Lithium Ion technology
    STATUS_BATTERY_TECHNOLOGY.LIPO : Lithium Polymer technology
    STATUS_BATTERY_TECHNOLOGY.LIFE : Lithium Iron Phosphate technology
    STATUS_BATTERY_TECHNOLOGY.NICD : Nickel Cadmium technology
    STATUS_BATTERY_TECHNOLOGY.LIMN : Lithium Manganese technology
    '''
    UNKNOWN = 0
    NIMH = 1
    LION = 2
    LIPO = 3
    LIFE = 4
    NICD = 5
    LIMN = 6



class STATUS_SERVER(Enum):
    '''
    Enumeration to indicate the server status.
    STATUS_SERVER.NOT_AVAILABLE : Server not available
    STATUS_SERVER.STOPPED : Server stopped
    STATUS_SERVER.STARTING : Server starting
    STATUS_SERVER.RUNNING : Server running
    STATUS_SERVER.FAILED : Server failed
    '''
    NOT_AVAILABLE = 0
    STOPPED = 1
    STARTING = 2
    RUNNING = 3
    FAILED = 4



class STATUS_ENGINE(Enum):
    '''
    Enumeration to indicate the engine status.
    STATUS_ENGINE.NOT_AVAILABLE : Engine not available
    STATUS_ENGINE.STOPPED : Engine stopped
    STATUS_ENGINE.STARTING : Engine starting
    STATUS_ENGINE.RUNNING : Engine running
    STATUS_ENGINE.FAILED : Engine failed
    '''
    NOT_AVAILABLE = 0
    STOPPED = 1
    STARTING = 2
    RUNNING = 3
    FAILED = 4



class STATUS_SERVER_ERROR(Enum):
    '''
    Enumeration to indicate the error code, when the server is not available.
    STATUS_SERVER_ERROR.OK : No error
    STATUS_SERVER_ERROR.ERROR_UNKNOWN : Unknown error
    '''    
    OK = 0
    ERROR_UNKNOWN = 255



class STATUS_ENGINE_ERROR(Enum):
    '''
    Enumeration to indicate the error code, when the engine is not available.
    STATUS_ENGINE_ERROR.OK : No error
    STATUS_ENGINE_ERROR.ERROR_UNKNOWN : Unknown error
    '''    
    OK = 0
    ERROR_UNKNOWN = 255


# Skills

class SKILL_STATE(Enum):
    '''
    Enumeration to indicate the state of the skill
    SKILL_STATE.CREATED : Skill created
    SKILL_STATE.INITIALIZING : Skill initializing
    SKILL_STATE.ERROR_INITIALIZING : Skill error initializing
    SKILL_STATE.INITIALIZED : Skill initialized
    SKILL_STATE.EXECUTING : Skill executing
    SKILL_STATE.ERROR_EXECUTING : Skill error executing
    SKILL_STATE.EXECUTED : Skill executed
    SKILL_STATE.FINISHING : Skill finishing
    SKILL_STATE.ERROR_FINISHING : Skill error finishing
    SKILL_STATE.FINISHED : Skill finished
    '''
    CREATED = 0
    INITIALIZING = 1
    ERROR_INITIALIZING = 2
    INITIALIZED = 3
    EXECUTING = 4
    ERROR_EXECUTING = 5
    EXECUTED = 6
    FINISHING = 7
    ERROR_FINISHING = 8
    FINISHED = 9

# Signals recieved

class SIGNAL_ID(Enum):
    '''
    Enumeration to indicate the signal id
    SIGNAL_ID.INTERRUPT : Signal interrupt
    SIGNAL_ID.ABORT : Signal abort
    '''
    INTERRUPTED = 2
    ABORTED = 9


class REASON_CODE(Enum):
    '''
    Enumeration to indicate the reason code
    REASON_CODE.UNKNOWN : Unknown reason
    REASON_CODE.BATTERY_NOT_CONNECTED : Battery not connected
    REASON_CODE.BATTERY_NOT_CHARGING : Battery not charging
    REASON_CODE.LOW_BATTERY : Low battery but still run apps
    REASON_CODE.CRITICAL_LOW_BATTERY : Critical low battery, any running app will be aborted
    REASON_CODE.CHARGING_NOT_AVAILABLE : Charging not available
    REASON_CODE.APPS_ARE_RUNNING : There is already an app running
    '''
    UNKNOWN = 0
    BATTERY_NOT_CONNECTED = 1
    BATTERY_NOT_CHARGING = 2
    LOW_BATTERY = 3
    CRITICAL_LOW_BATTERY = 4
    CHARGING_NOT_AVAILABLE = 5
    APPS_ARE_RUNNING = 6

# Exit codes for apps

class EXIT_CODE(Enum):
    '''
    Enumeration to indicate the exit code
    EXIT_CODE.SUCCESS : Success exit code
    EXIT_CODE.BUSY : Busy exit code
    EXIT_CODE.NOT_AVAILABLE : Not available exit code
    EXIT_CODE.ERROR : Error exit code
    EXIT_CODE.INTERRUPTED_WITHOUT_ERROR : App Interrupted without error exit code
    EXIT_CODE.INTERRUPTED_WITH_ERROR : App Interrupted with error exit code
    EXIT_CODE.ABORTED : App Aborted exit code
    '''
    SUCCESS = 0
    BUSY = 101
    NOT_AVAILABLE = 102
    ERROR = 103
    INTERRUPTED_WITHOUT_ERROR = 150
    INTERRUPTED_WITH_ERROR = 151
    ABORTED = 152

# Cameras

class IMAGE_TYPE(IntEnum):
    '''
    Enumeration to indicate the camera.
    '''
    COLOR = 0
    DEPTH = 1