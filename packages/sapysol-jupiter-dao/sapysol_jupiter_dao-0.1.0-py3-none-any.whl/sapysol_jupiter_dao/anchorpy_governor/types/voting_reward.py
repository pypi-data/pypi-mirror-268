# ================================================================================
#
from __future__ import annotations
import typing
from   dataclasses              import dataclass
from   construct                import Container
from   solders.pubkey           import Pubkey
from   anchorpy.borsh_extension import BorshPubkey
import borsh_construct          as borsh

# ================================================================================
#
class VotingRewardJSON(typing.TypedDict):
    reward_mint:         str
    reward_vault:        str
    reward_per_proposal: int

# ================================================================================
#
@dataclass
class VotingReward:
    layout: typing.ClassVar = borsh.CStruct(
        "reward_mint"         / BorshPubkey,
        "reward_vault"        / BorshPubkey,
        "reward_per_proposal" / borsh.U64,
    )
    reward_mint:         Pubkey
    reward_vault:        Pubkey
    reward_per_proposal: int

    # ========================================
    #
    @classmethod
    def from_decoded(cls, obj: Container) -> "VotingReward":
        return cls(reward_mint         = obj.reward_mint,
                   reward_vault        = obj.reward_vault,
                   reward_per_proposal = obj.reward_per_proposal)

    # ========================================
    #
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "reward_mint":         self.reward_mint,
            "reward_vault":        self.reward_vault,
            "reward_per_proposal": self.reward_per_proposal,
        }

    # ========================================
    #
    def to_json(self) -> VotingRewardJSON:
        return {
            "reward_mint":         str(self.reward_mint),
            "reward_vault":        str(self.reward_vault),
            "reward_per_proposal":     self.reward_per_proposal,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: VotingRewardJSON) -> "VotingReward":
        return cls(
            reward_mint         = Pubkey.from_string(obj["reward_mint"]),
            reward_vault        = Pubkey.from_string(obj["reward_vault"]),
            reward_per_proposal =                    obj["reward_per_proposal"],
        )

# ================================================================================
#
