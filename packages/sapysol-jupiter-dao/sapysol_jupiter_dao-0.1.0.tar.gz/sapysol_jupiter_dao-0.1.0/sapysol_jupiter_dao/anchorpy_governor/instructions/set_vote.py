# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   solders.instruction import Instruction, AccountMeta
import borsh_construct     as borsh
from ..program_id          import PROGRAM_ID, GOVERNOR_PROGRAM_ID, VOTER_PROGRAM_ID

# =============================================================================
#
class SetVoteArgs(typing.TypedDict):
    side:   int
    weight: int

# =============================================================================
#
layout = borsh.CStruct(
    "side"   / borsh.U8, 
    "weight" / borsh.U64
)

# =============================================================================
#
class SetVoteAccounts(typing.TypedDict):
    governor: Pubkey
    proposal: Pubkey
    vote:     Pubkey
    locker:   Pubkey

# =============================================================================
#
def set_vote(args:               SetVoteArgs,
             accounts:           SetVoteAccounts,
             program_id:         Pubkey = PROGRAM_ID,
             remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["proposal"], is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["vote"],     is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["locker"],   is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xab!S\xac\x94\xd7\xefa"
    encoded_args = layout.build({
        "side":   args["side"],
        "weight": args["weight"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
