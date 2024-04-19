# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey           import Pubkey
from   solders.instruction      import Instruction, AccountMeta
from   anchorpy.borsh_extension import BorshPubkey
import borsh_construct          as borsh
from ..program_id               import PROGRAM_ID

# =============================================================================
#
class SetLockerArgs(typing.TypedDict):
    new_locker: Pubkey

# =============================================================================
#
layout = borsh.CStruct(
    "new_locker" / BorshPubkey
)

# =============================================================================
#
class SetLockerAccounts(typing.TypedDict):
    governor:     Pubkey
    smart_wallet: Pubkey

# =============================================================================
#
def set_locker(args:               SetLockerArgs,
               accounts:           SetLockerAccounts,
               program_id:         Pubkey = PROGRAM_ID,
               remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["smart_wallet"], is_signer=True, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\x11\x06eH\xfa\x17\x98`"
    encoded_args = layout.build({
        "new_locker": args["new_locker"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
