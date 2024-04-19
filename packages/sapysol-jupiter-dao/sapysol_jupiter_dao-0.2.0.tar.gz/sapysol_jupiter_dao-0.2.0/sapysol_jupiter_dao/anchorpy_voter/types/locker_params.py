# ================================================================================
#
from __future__ import annotations
import typing
from   dataclasses     import dataclass
from   construct       import Container
import borsh_construct as borsh

# ================================================================================
#
class LockerParamsJSON(typing.TypedDict):
    max_stake_vote_multiplier:     int
    min_stake_duration:            int
    max_stake_duration:            int
    proposal_activation_min_votes: int

# ================================================================================
#
@dataclass
class LockerParams:
    layout: typing.ClassVar = borsh.CStruct(
        "max_stake_vote_multiplier"     / borsh.U8,
        "min_stake_duration"            / borsh.U64,
        "max_stake_duration"            / borsh.U64,
        "proposal_activation_min_votes" / borsh.U64,
    )
    max_stake_vote_multiplier:     int
    min_stake_duration:            int
    max_stake_duration:            int
    proposal_activation_min_votes: int

    # ========================================
    #
    @classmethod
    def from_decoded(cls, obj: Container) -> "LockerParams":
        return cls(max_stake_vote_multiplier     = obj.max_stake_vote_multiplier,
                   min_stake_duration            = obj.min_stake_duration,
                   max_stake_duration            = obj.max_stake_duration,
                   proposal_activation_min_votes = obj.proposal_activation_min_votes)

    # ========================================
    #
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "max_stake_vote_multiplier":     self.max_stake_vote_multiplier,
            "min_stake_duration":            self.min_stake_duration,
            "max_stake_duration":            self.max_stake_duration,
            "proposal_activation_min_votes": self.proposal_activation_min_votes,
        }

    # ========================================
    #
    def to_json(self) -> LockerParamsJSON:
        return {
            "max_stake_vote_multiplier":     self.max_stake_vote_multiplier,
            "min_stake_duration":            self.min_stake_duration,
            "max_stake_duration":            self.max_stake_duration,
            "proposal_activation_min_votes": self.proposal_activation_min_votes,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: LockerParamsJSON) -> "LockerParams":
        return cls(max_stake_vote_multiplier     = obj["max_stake_vote_multiplier"],
                   min_stake_duration            = obj["min_stake_duration"],
                   max_stake_duration            = obj["max_stake_duration"],
                   proposal_activation_min_votes = obj["proposal_activation_min_votes"])

# ================================================================================
#
