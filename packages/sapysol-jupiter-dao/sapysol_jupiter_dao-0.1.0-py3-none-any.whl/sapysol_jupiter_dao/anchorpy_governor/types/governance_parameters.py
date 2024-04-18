# =============================================================================
#
from __future__ import annotations
import typing
from   dataclasses     import dataclass
from   construct       import Container
import borsh_construct as borsh

# =============================================================================
#
class GovernanceParametersJSON(typing.TypedDict):
    voting_delay: int
    voting_period: int
    quorum_votes: int
    timelock_delay_seconds: int

# =============================================================================
#
@dataclass
class GovernanceParameters:
    layout: typing.ClassVar = borsh.CStruct(
        "voting_delay"           / borsh.U64,
        "voting_period"          / borsh.U64,
        "quorum_votes"           / borsh.U64,
        "timelock_delay_seconds" / borsh.I64,
    )
    voting_delay:           int
    voting_period:          int
    quorum_votes:           int
    timelock_delay_seconds: int

    # ========================================
    #
    @classmethod
    def from_decoded(cls, obj: Container) -> "GovernanceParameters":
        return cls(voting_delay           = obj.voting_delay,
                   voting_period          = obj.voting_period,
                   quorum_votes           = obj.quorum_votes,
                   timelock_delay_seconds = obj.timelock_delay_seconds)

    # ========================================
    #
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "voting_delay":           self.voting_delay,
            "voting_period":          self.voting_period,
            "quorum_votes":           self.quorum_votes,
            "timelock_delay_seconds": self.timelock_delay_seconds,
        }

    # ========================================
    #
    def to_json(self) -> GovernanceParametersJSON:
        return {
            "voting_delay":           self.voting_delay,
            "voting_period":          self.voting_period,
            "quorum_votes":           self.quorum_votes,
            "timelock_delay_seconds": self.timelock_delay_seconds,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: GovernanceParametersJSON) -> "GovernanceParameters":
        return cls(
            voting_delay           = obj["voting_delay"],
            voting_period          = obj["voting_period"],
            quorum_votes           = obj["quorum_votes"],
            timelock_delay_seconds = obj["timelock_delay_seconds"],
        )

# =============================================================================
#
