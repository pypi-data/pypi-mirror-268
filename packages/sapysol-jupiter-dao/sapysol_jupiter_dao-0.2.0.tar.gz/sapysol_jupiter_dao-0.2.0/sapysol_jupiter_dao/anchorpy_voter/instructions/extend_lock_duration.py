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
class ExtendLockDurationArgs(typing.TypedDict):
    duration: int

# ================================================================================
#
layout = borsh.CStruct(
    "duration" / borsh.I64
)

# ================================================================================
#
class ExtendLockDurationAccounts(typing.TypedDict):
    locker:       Pubkey
    escrow:       Pubkey
    escrow_owner: Pubkey

# ================================================================================
#
def extend_lock_duration(args:               ExtendLockDurationArgs,
                         accounts:           ExtendLockDurationAccounts,
                         program_id:         Pubkey = PROGRAM_ID,
                         remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["locker"],       is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["escrow"],       is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow_owner"], is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xb1i\xc4\x81\x99\x89\x88\xe6"
    encoded_args = layout.build({
        "duration": args["duration"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
