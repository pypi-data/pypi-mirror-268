# =============================================================================
#
import typing
from   anchorpy.error import ProgramError

# =============================================================================
#
class InvalidVoteSide(ProgramError):
    def __init__(self) -> None:
        super().__init__(6000, "Invalid vote side.")

    code = 6000
    name = "InvalidVoteSide"
    msg = "Invalid vote side."


class InvalidProposalType(ProgramError):
    def __init__(self) -> None:
        super().__init__(6001, "Invalid proposal type.")

    code = 6001
    name = "InvalidProposalType"
    msg = "Invalid proposal type."


class GovernorNotFound(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6002, "The owner of the smart wallet doesn't match with current."
        )

    code = 6002
    name = "GovernorNotFound"
    msg = "The owner of the smart wallet doesn't match with current."


class VotingDelayNotMet(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6003,
            "The proposal cannot be activated since it has not yet passed the voting delay.",
        )

    code = 6003
    name = "VotingDelayNotMet"
    msg = (
        "The proposal cannot be activated since it has not yet passed the voting delay."
    )


class ProposalNotDraft(ProgramError):
    def __init__(self) -> None:
        super().__init__(6004, "Only drafts can be canceled.")

    code = 6004
    name = "ProposalNotDraft"
    msg = "Only drafts can be canceled."


class ProposalNotActive(ProgramError):
    def __init__(self) -> None:
        super().__init__(6005, "The proposal must be active.")

    code = 6005
    name = "ProposalNotActive"
    msg = "The proposal must be active."


class InvalidMaxOption(ProgramError):
    def __init__(self) -> None:
        super().__init__(6006, "Max option is invalid")

    code = 6006
    name = "InvalidMaxOption"
    msg = "Max option is invalid"


class NotYesNoProposal(ProgramError):
    def __init__(self) -> None:
        super().__init__(6007, "Proposal is not YesNo.")

    code = 6007
    name = "NotYesNoProposal"
    msg = "Proposal is not YesNo."


class NotOptionProposal(ProgramError):
    def __init__(self) -> None:
        super().__init__(6008, "Proposal is not Option.")

    code = 6008
    name = "NotOptionProposal"
    msg = "Proposal is not Option."


class InvalidOptionDescriptions(ProgramError):
    def __init__(self) -> None:
        super().__init__(6009, "Invalid option descriptions.")

    code = 6009
    name = "InvalidOptionDescriptions"
    msg = "Invalid option descriptions."

# =============================================================================
#
CustomError = typing.Union[
    InvalidVoteSide,
    InvalidProposalType,
    GovernorNotFound,
    VotingDelayNotMet,
    ProposalNotDraft,
    ProposalNotActive,
    InvalidMaxOption,
    NotYesNoProposal,
    NotOptionProposal,
    InvalidOptionDescriptions,
]
CUSTOM_ERROR_MAP: dict[int, CustomError] = {
    6000: InvalidVoteSide(),
    6001: InvalidProposalType(),
    6002: GovernorNotFound(),
    6003: VotingDelayNotMet(),
    6004: ProposalNotDraft(),
    6005: ProposalNotActive(),
    6006: InvalidMaxOption(),
    6007: NotYesNoProposal(),
    6008: NotOptionProposal(),
    6009: InvalidOptionDescriptions(),
}

# =============================================================================
#
def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err

# =============================================================================
#
