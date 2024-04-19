# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   solders.instruction import Instruction, AccountMeta
import borsh_construct     as borsh
from ..program_id          import PROGRAM_ID

# =============================================================================
#
class SetVotingRewardArgs(typing.TypedDict):
    reward_per_proposal: int

# =============================================================================
#
layout = borsh.CStruct(
    "reward_per_proposal" / borsh.U64
)

# =============================================================================
#
class SetVotingRewardAccounts(typing.TypedDict):
    governor:     Pubkey
    reward_mint:  Pubkey
    smart_wallet: Pubkey

# =============================================================================
#
def set_voting_reward(args:               SetVotingRewardArgs,
                      accounts:           SetVotingRewardAccounts,
                      program_id:         Pubkey = PROGRAM_ID,
                      remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"],     is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["reward_mint"],  is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["smart_wallet"], is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xe3\xf10\x89\x1e\x1ahF"
    encoded_args = layout.build({
        "reward_per_proposal": args["reward_per_proposal"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
