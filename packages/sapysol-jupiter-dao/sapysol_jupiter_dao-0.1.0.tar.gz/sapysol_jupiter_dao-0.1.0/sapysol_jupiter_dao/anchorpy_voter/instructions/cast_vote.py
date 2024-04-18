# ================================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   solders.instruction import Instruction, AccountMeta
import borsh_construct     as borsh
from ..program_id          import PROGRAM_ID

# ================================================================================
#
class CastVoteArgs(typing.TypedDict):
    side: int

# ================================================================================
#
layout = borsh.CStruct(
    "side" / borsh.U8
)

# ================================================================================
#
class CastVoteAccounts(typing.TypedDict):
    locker:         Pubkey
    escrow:         Pubkey
    vote_delegate:  Pubkey
    proposal:       Pubkey
    vote:           Pubkey
    governor:       Pubkey
    govern_program: Pubkey

# ================================================================================
#
def cast_vote(args:               CastVoteArgs,
              accounts:           CastVoteAccounts,
              program_id:         Pubkey = PROGRAM_ID,
              remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["locker"],         is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["escrow"],         is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["vote_delegate"],  is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["proposal"],       is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["vote"],           is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["governor"],       is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["govern_program"], is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\x14\xd4\x0f\xbdE\xb4E\x97"
    encoded_args = layout.build({
        "side": args["side"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
