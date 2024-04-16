from raya.exceptions import *

ALREADY_RUNNING_ERROR = 20


def check_raya_exception(map, response):
    pass


def check_raya_exception_code(map, error_code, error_msg):
    pass


def search_raya_exception_code(map, exception):
    pass


EXCEPTIONS_MAP_GENERAL = {
    1: (RayaApplicationAlreadyRegistered, ''),
    2: (RayaApplicationNotRegistered, ''),
    3: (RayaApplicationException, ''),
    4: (RayaNotAvailableServer, ''),
    5: (RayaNotServerPermissions, ''),
    14: (RayaSimulatorError, ''),
    15: (RayaSignalNotImplemented, ''),
    16: (RayaUnknownServerError, ''),
    17: (RayaGoalNotAccepted, ''),
    18: (RayaCommandCanceled, ''),
    19: (RayaWrongArgument, ''),
    20: (RayaCommandAlreadyRunning, ''),
    119: (RayaUnknownServerError, ''),
    219: (RayaUnknownServerError, ''),
    126: (RayaNoPathToGoal, '')
}
EXCEPTIONS_MAP_COMMUNICATION = {
    **EXCEPTIONS_MAP_GENERAL, 20:
    (RayaCommSimultaneousRequests, 'Simultaneous msg requests'),
    21: (RayaCommNotRunningApp, 'Destination app not running'),
    22: (RayaCommNotRunningApp, 'RGS not running')
}
EXCEPTIONS_MAP_CAMERAS = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaCameraAlreadyEnabled, ''),
    21: (RayaCameraNotEnabled, ''),
    22: (RayaCameraInvalidName, ''),
    23: (RayaCameraWrongType, ''),
    121: (RayaCameraInvalidName, ''),
    122: (RayaCameraStreamServerNoResponse, ''),
    123: (RayaCameraStreamServerNoConnection, '')
}
EXCEPTIONS_MAP_INTERACTIONS = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaInteractionsAlreadyRunning, ''),
    21: (RayaInteractionsWrongName, '')
}
EXCEPTIONS_MAP_SOUND = {
    **EXCEPTIONS_MAP_GENERAL, 120: (RayaSoundPredefinedSoundNotFound, ''),
    121: (RayaSoundWrongFormat, ''),
    122: (RayaSoundErrorPlayingAudiofile, ''),
    123: (RayaSoundErrorPlayingAudioData, ''),
    124: (RayaSoundPlayingCanceled, ''),
    125: (RayaSoundErrorRecording, ''),
    126: (RayaSoundMicropohoneNotFound, ''),
    127: (RayaSoundBufferNotFound, ''),
    128: (RayaSoundDataNotProcessed, ''),
    129: (RayaSoundDataNotMatchBuffer, '')
}
EXCEPTIONS_MAP_LEDS = {
    **EXCEPTIONS_MAP_GENERAL, 120: (RayaLedsWrongGroup, ''),
    121: (RayaLedsWrongColorName, ''),
    122: (RayaLedsWrongColorValue, ''),
    123: (RayaLedsWrongAnimationName, ''),
    124: (RayaLedsWrongRepetitions, ''),
    125: (RayaLedsWrongSpeed, '')
}
EXCEPTIONS_MAP_MOTION = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaAlreadyMoving, ''),
    21: (RayaNotValidMotionCommand, ''),
    22: (RayaNotValidMotionCommand, ''),
    23: (RayaObstacleDetected, ''),
    24: (RayaInvalidMinDistance, ''),
    25: (RayaMotionTimeout, ''),
    26: (RayaRobotNotMoving, ''),
    105: (RayaMotionUnableToMove, 'Robot unable to move.'),
    107: (RayaMotionObstacleDetected, 'Obstacle detected, movement canceled.'),
    136: (RayaUnableToEnableCamera, '')
}
EXCEPTIONS_MAP_NAV = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaNavAlreadyNavigating, ''),
    22: (RayaNavNotMapping, ''),
    23: (RayaNavLocationAlreadyExist, ''),
    24: (RayaNavErrorReadingYaml, ''),
    25: (RayaNavErrorWritingYaml, ''),
    26: (RayaNavLocationNotFound, ''),
    27: (RayaNavLocationsNotFound, ''),
    28: (RayaNavNoMapLoaded, ''),
    29: (RayaNavNoDataFromMapTopic, ''),
    30: (RayaNavZoneNotFound, ''),
    31: (RayaNavNotLocated, ''),
    32: (RayaNavSortedPointsEmpty, ''),
    33: (RayaNavZoneAlreadyExist, ''),
    34: (RayaNavErrorSavingZone, ''),
    35: (RayaNavZoneIsNotPolygon, ''),
    36: (RayaNavNotValidPointFound, ''),
    105: (RayaMotionUnableToMove, 'FinalOrientation: Robot unable to move.'),
    107: (RayaMotionObstacleDetected, 'FinalOrientation: Obstacle detected.'),
    115: (RayaUnableToFollowPath, ''),
    116: (RayaUnableToComputePath, ''),
    121: (RayaNavUnableToSaveMap, ''),
    122: (RayaNavNoDataFromMapTopic, ''),
    123: (RayaNavUnableToChangeMap, ''),
    124: (RayaNavInvalidGoal, ''),
    125: (RayaUnableToFollowPath, ''),
    126: (RayaNoPathToGoal, ''),
    127: (RayaNavIncompletePath, ''),
    128: (RayaNavIncorrectPath, ''),
    129: (RayaNavBadImageSize, ''),
    130: (RayaNavMappingDisabled, ''),
    136: (RayaNavUnableToEnableCamera, ''),
    137: (RayaNavLocalizationRejected, ''),
    140: (RayaNavFileNotFound, ''),
    141: (RayaNavWrongFileFormat, '')
}
EXCEPTIONS_MAP_CV = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaCVAlreadyEnabled, ''),
    21: (RayaCVNotCameraInterface, ''),
    22: (RayaCVTopicNotPublishig, ''),
    23: (RayaCVGPUNotAvailable, ''),
    24: (RayaCVModelNotRunning, ''),
    25: (RayaCVModelLimitReached, ''),
    26: (RayaCVNotTrain, ''),
    27: (RayaCVWrongAppInfo, ''),
    28: (RayaCVWrongModelMode, ''),
    29: (RayaCVCameraStatusFail, ''),
    30: (RayaCVWrongCamera, ''),
    31: (RayaCVRunningOtherCamera, ''),
    32: (RayaCVRunningOtherParams, ''),
    33: (RayaCVRunningOtherName, ''),
    34: (RayaCVNotFacesTrain, ''),
    35: (RayaCVNotRegisterServer, ''),
    36: (RayaCVNotDisabled, ''),
    37: (RayaCVNotToken, ''),
    38: (RayaCVNotFolder, ''),
    39: (RayaCVNotFile, ''),
    40: (RayaCVWrongConfigFile, ''),
    41: (RayaCVWrongParam, '')
}
EXCEPTIONS_MAP_NLP = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaNlpAlreadyEnabled, ''),
    21: (RayaNlpWrongProvider, ''),
    22: (RayaNlpSetCredentialsError, ''),
    23: (RayaNlpCredentialsFileNeeded, ''),
    24: (RayaNlpInvalidCredentials, ''),
    25: (RayaNlpNotMicAvailable, ''),
    26: (RayaNlpNotAvailableMethod, ''),
    27: (RayaNlpNotMicData, ''),
    28: (RayaNlpErrorRegisterServer, ''),
    29: (RayaNlpInvalidRegisterServer, '')
}
EXCEPTIONS_MAP_ARMS = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaAlreadyMoving, ''),
    21: (RayaArmsInvalidArmName, ''),
    22: (RayaArmsNotPoseArmDataAvailable, ''),
    23: (RayaArmsNotPredefinedPoseAvailable, ''),
    24: (RayaArmsInvalidNumberOfJoints, ''),
    25: (RayaArmsOutOfLimits, ''),
    26: (RayaArmsPredefinedPoseEmptyName, ''),
    27: (RayaArmsPredefinedPoseNameAlreadyExist, ''),
    28: (RayaArmsPredefinedPoseNameNotExist, ''),
    29: (RayaArmsPredefinedTrajectoryNameAlreadyExist, ''),
    30: (RayaArmsPredefinedTrajectoryNameNotExist, ''),
    31: (RayaArmsErrorParsingPredefinedTrajectory, ''),
    32: (RayaArmsInvalidNumberOfELements, ''),
    33: (RayaArmsInvalidCustomCommand, ''),
    34: (RayaArmsInvalidJointName, ''),
    35: (RayaCustomMissingRequiredParameter, ''),
    36: (RayaCustomErrorParsingParameter, ''),
    37: (RayaCustomCommandServerNotAvailable, ''),
    121: (RayaArmsExternalException, ''),
    122: (RayaArmsExternalException, ''),
    123: (RayaArmsExternalException, ''),
    124: (RayaArmsExternalException, ''),
    125: (RayaArmsExternalException, ''),
    126: (RayaArmsExternalException, ''),
    127: (RayaArmsExternalException, ''),
    130: (RayaArmsExternalException, ''),
    131: (RayaArmsExternalException, ''),
    132: (RayaArmsExternalException, ''),
    133: (RayaArmsExternalException, ''),
    134: (RayaArmsExternalException, ''),
    136: (RayaArmsExternalException, ''),
    137: (RayaArmsExternalException, ''),
    138: (RayaArmsExternalException, ''),
    139: (RayaArmsExternalException, ''),
    141: (RayaArmsExternalException, ''),
    142: (RayaArmsExternalException, ''),
    143: (RayaArmsExternalException, ''),
    144: (RayaArmsExternalException, ''),
    145: (RayaArmsExternalException, ''),
    146: (RayaArmsExternalException, ''),
    151: (RayaArmsExternalException, ''),
    152: (RayaArmsExternalException, ''),
    161: (RayaArmsExternalException, ''),
    162: (RayaArmsExternalException, ''),
    163: (RayaArmsExternalException, ''),
    164: (RayaArmsExternalException, ''),
    171: (RayaArmsExternalException, ''),
    172: (RayaArmsExternalException, ''),
    173: (RayaArmsExternalException, ''),
    174: (RayaArmsExternalException, ''),
    175: (RayaArmsExternalException, ''),
    180: (RayaArmsExternalException, ''),
    181: (RayaArmsExternalException, ''),
    191: (RayaArmsExternalException, ''),
    192: (RayaArmsExternalException, ''),
    193: (RayaArmsExternalException, ''),
    194: (RayaArmsExternalException, ''),
    195: (RayaArmsExternalException, ''),
    196: (RayaArmsExternalException, ''),
    197: (RayaArmsExternalException, ''),
    198: (RayaArmsExternalException, '')
}
EXCEPTIONS_MAP_MANIPULATION = {
    **EXCEPTIONS_MAP_GENERAL, 20: (RayaManipulationAlreadyEnabled, ''),
    21: (RayaManipulationArmNameError, ''),
    22: (RayaManipulationObjNotFound, ''),
    23: (RayaManipulationNotDetections, ''),
    24: (RayaManipulationTopicNotPublishing, ''),
    25: (RayaManipulationSrvNotAvailable, ''),
    26: (RayaManipulationPickSolutionNotFound, ''),
    28: (RayaManipulationNotReference, ''),
    28: (RayaManipulationNotArm, ''),
    29: (RayaManipulationNotHeight, ''),
    30: (RayaManipulationPlaceSolutionNotFound, ''),
    31: (RayaManipulationNotTag, ''),
    32: (RayaManipulationInvalidPoint, ''),
    33: (RayaManipulationNotObjName, ''),
    34: (RayaManipulationArmsNotPlace, ''),
    35: (RayaManipulationArmsNotPick, ''),
    36: (RayaManipulationWrongValues, ''),
    37: (RayaManipulationWrongPickMethod, ''),
    38: (RayaManipulationCheckPosesError, ''),
    39: (RayaManipulationArmsBusy, '')
}
EXCEPTIONS_MAP_STATUS = {
    **EXCEPTIONS_MAP_GENERAL, 21: (RayaStatusServerProviderDown, '')
}
EXCEPTIONS_MAP_SENSORS = {
    **EXCEPTIONS_MAP_GENERAL, 21: (RayaSensorsUnknownPath, ''),
    22: (RayaSensorsIncompatiblePath, ''),
    23: (RayaSensorsInvalidPath, '')
}
