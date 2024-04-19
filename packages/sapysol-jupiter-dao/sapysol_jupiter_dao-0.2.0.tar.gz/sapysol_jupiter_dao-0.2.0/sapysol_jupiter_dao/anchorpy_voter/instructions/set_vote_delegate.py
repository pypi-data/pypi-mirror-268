# ================================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey           import Pubkey
from   solders.instruction      import Instruction, AccountMeta
from   anchorpy.borsh_extension import BorshPubkey
import borsh_construct          as borsh
from ..program_id               import PROGRAM_ID

# ================================================================================
#
class SetVoteDelegateArgs(typing.TypedDict):
    new_delegate: Pubkey

# ================================================================================
#
layout = borsh.CStruct(
    "new_delegate" / BorshPubkey
)

# ================================================================================
#
class SetVoteDelegateAccounts(typing.TypedDict):
    escrow:       Pubkey
    escrow_owner: Pubkey

# ================================================================================
#
def set_vote_delegate(args:               SetVoteDelegateArgs,
                      accounts:           SetVoteDelegateAccounts,
                      program_id:         Pubkey = PROGRAM_ID,
                      remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["escrow"],       is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow_owner"], is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b".\xec\xf1\xf3\xfbl\x9c\x0c"
    encoded_args = layout.build({
        "new_delegate": args["new_delegate"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
