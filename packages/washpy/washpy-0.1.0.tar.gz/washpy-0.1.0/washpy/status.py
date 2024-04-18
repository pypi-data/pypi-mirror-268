from enum import Enum


class Status(Enum):
    """
    represents the <object:DeviceState>.Status

    Codes and descriptions are retrieved directly from the Miele IPprofileCore document.

    use the `status_from_code` method to convert from integer to Status

    RESERVED : 0, 18..30, 36..63,  -- Reserved No use
    OFF : 1 -- Appliance in off state
    STAND_BY : 2 -- Appliance in stand-by
    PROGRAMMED : 3 -- Appliance already programmed
    PROGRAMMED_WAITING_TO_START : 4 -- Appliance already programmed and ready to start
    RUNNING : 5 -- Appliance is running
    PAUSE : 6 -- Appliance is in pause
    END_PROGRAMMED : 7 -- Appliance end programmed task
    FAILURE : 8
    PROGRAMME_INTERRUPTED : 9 -- The appliance programmed tasks have been interrupted
    IDLE : 10 -- Appliance is in idle state
    RINSE_HOLD : 11 -- Appliance rinse hold
    SERVICE : 12 -- Appliance in service state
    SUPERFREEZING : 13 -- Appliance in superfreezing state
    SUPERCOOLING : 14 -- Appliance in supercooling state
    SUPERHEATING : 15 -- Appliance in superheating state
    MANUALCONTROL : (
        16,
        "Appliance is in manual program control state (e.g. manual external control on Benchmark machines)",
    )
    WATERDRAIN : 17 -- Appliance in water drain state
    BOOT : 31 -- Appliance is in booting state
    SAFE_STATE : 32 -- Appliance is in safe state
    SHUTDOWN : 33 -- Appliance is shutting down
    UPDATE : 34 -- Appliance is in update state
    SYSTEST : 35 -- Appliance is in systest state
    NON_STANDARDIZED : 64..127 -- Non standardized
    DEFAULT : 144 -- Default – proprietary
    LOCKED : 145 -- Locked – proprietary
    SUPERCOOLING_SUPERFREEZING : 146 -- Supercooling_Superfreezing - proprietary
    NOT_CONNECTED : 255 -- No connection to this appliance
    PROPRIETARY : 128..255 -- Proprietary
    """

    RESERVED = 0
    OFF = 1
    STAND_BY = 2
    PROGRAMMED = 3
    PROGRAMMED_WAITING_TO_START = 4
    RUNNING = 5
    PAUSE = 6
    END_PROGRAMMED = 7
    FAILURE = 8
    PROGRAMME_INTERRUPTED = 9
    IDLE = 10
    RINSE_HOLD = 11
    SERVICE = 12
    SUPERFREEZING = 13
    SUPERCOOLING = 14
    SUPERHEATING = 15
    MANUALCONTROL = 16
    WATERDRAIN = 17
    BOOT = 31
    SAFE_STATE = 32
    SHUTDOWN = 33
    UPDATE = 34
    SYSTEST = 35
    NON_STANDARDIZED = 64
    DEFAULT = 144
    LOCKED = 145
    SUPERCOOLING_SUPERFREEZING = 146
    NOT_CONNECTED = 255
    PROPRIETARY = 128


def status_from_code(status_code: int) -> Status:
    """
    Converts integer status codes to Status enum objects,
    according to section 4.3.4.2.1 of the Miele IPprofileCore document.
    """
    # the code ranges 18...30 and 36...63 belong to the reserved value 0
    if (
        status_code >= 18
        and status_code <= 30
        or status_code >= 36
        and status_code <= 63
    ):
        return Status.RESERVED

    # the code range 64...127 is all NON_STANDARDIZED
    if status_code >= 64 and status_code <= 127:
        return Status.NON_STANDARDIZED

    # the code range 128..255 is PROPRIETARY, except for some codes in that range
    if (
        status_code >= 128
        and status_code <= 255
        and status_code not in {144, 145, 146, 255}
    ):
        return Status.PROPRIETARY

    return Status(status_code)


class StatusException(Exception):
    """
    This exception is raised, if the status of the machine
    is incompatible to the requested action.
    """
