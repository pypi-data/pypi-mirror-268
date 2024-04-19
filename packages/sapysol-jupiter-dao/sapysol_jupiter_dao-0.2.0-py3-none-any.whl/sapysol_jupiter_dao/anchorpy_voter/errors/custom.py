# ================================================================================
#
import typing
from   anchorpy.error import ProgramError

# ================================================================================
#
class LockupDurationTooShort(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6000, "Lockup duration must at least be the min stake duration"
        )

    code = 6000
    name = "LockupDurationTooShort"
    msg = "Lockup duration must at least be the min stake duration"


class LockupDurationTooLong(ProgramError):
    def __init__(self) -> None:
        super().__init__(6001, "Lockup duration must at most be the max stake duration")

    code = 6001
    name = "LockupDurationTooLong"
    msg = "Lockup duration must at most be the max stake duration"


class RefreshCannotShorten(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6002, "A voting escrow refresh cannot shorten the escrow time remaining"
        )

    code = 6002
    name = "RefreshCannotShorten"
    msg = "A voting escrow refresh cannot shorten the escrow time remaining"


class EscrowNotEnded(ProgramError):
    def __init__(self) -> None:
        super().__init__(6003, "Escrow has not ended")

    code = 6003
    name = "EscrowNotEnded"
    msg = "Escrow has not ended"


class MaxLockIsSet(ProgramError):
    def __init__(self) -> None:
        super().__init__(6004, "Maxlock is set")

    code = 6004
    name = "MaxLockIsSet"
    msg = "Maxlock is set"


class ExpirationIsLessThanCurrentTime(ProgramError):
    def __init__(self) -> None:
        super().__init__(6005, "Cannot set expiration less than the current time")

    code = 6005
    name = "ExpirationIsLessThanCurrentTime"
    msg = "Cannot set expiration less than the current time"


class LockerIsExpired(ProgramError):
    def __init__(self) -> None:
        super().__init__(6006, "Locker is expired")

    code = 6006
    name = "LockerIsExpired"
    msg = "Locker is expired"


class ExpirationIsNotZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(6007, "Expiration is not zero")

    code = 6007
    name = "ExpirationIsNotZero"
    msg = "Expiration is not zero"


class AmountIsZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(6008, "Amount is zero")

    code = 6008
    name = "AmountIsZero"
    msg = "Amount is zero"

# ================================================================================
#
CustomError = typing.Union[
    LockupDurationTooShort,
    LockupDurationTooLong,
    RefreshCannotShorten,
    EscrowNotEnded,
    MaxLockIsSet,
    ExpirationIsLessThanCurrentTime,
    LockerIsExpired,
    ExpirationIsNotZero,
    AmountIsZero,
]
CUSTOM_ERROR_MAP: dict[int, CustomError] = {
    6000: LockupDurationTooShort(),
    6001: LockupDurationTooLong(),
    6002: RefreshCannotShorten(),
    6003: EscrowNotEnded(),
    6004: MaxLockIsSet(),
    6005: ExpirationIsLessThanCurrentTime(),
    6006: LockerIsExpired(),
    6007: ExpirationIsNotZero(),
    6008: AmountIsZero(),
}

# ================================================================================
#
def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err

                                    # ================================================================================
#
