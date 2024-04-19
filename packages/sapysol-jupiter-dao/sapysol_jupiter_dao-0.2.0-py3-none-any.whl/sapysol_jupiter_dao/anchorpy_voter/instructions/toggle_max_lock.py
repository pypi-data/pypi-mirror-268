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
class ToggleMaxLockArgs(typing.TypedDict):
    is_max_lock: bool

# ================================================================================
#
layout = borsh.CStruct(
    "is_max_lock" / borsh.Bool
)

# ================================================================================
#
class ToggleMaxLockAccounts(typing.TypedDict):
    locker:       Pubkey
    escrow:       Pubkey
    escrow_owner: Pubkey

# ================================================================================
#
def toggle_max_lock(args:               ToggleMaxLockArgs,
                    accounts:           ToggleMaxLockAccounts,
                    program_id:         Pubkey = PROGRAM_ID,
                    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["locker"],       is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["escrow"],       is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow_owner"], is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xa3\x9d\xa1\x84\xb3k\x7f\x8f"
    encoded_args = layout.build({
        "is_max_lock": args["is_max_lock"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
