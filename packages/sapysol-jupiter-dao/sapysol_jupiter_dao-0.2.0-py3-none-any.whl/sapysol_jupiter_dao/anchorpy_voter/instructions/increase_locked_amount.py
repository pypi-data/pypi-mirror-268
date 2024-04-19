# ================================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   spl.token.constants import TOKEN_PROGRAM_ID
from   solders.instruction import Instruction, AccountMeta
import borsh_construct     as borsh
from ..program_id          import PROGRAM_ID

# ================================================================================
#
class IncreaseLockedAmountArgs(typing.TypedDict):
    amount: int

# ================================================================================
#
layout = borsh.CStruct(
    "amount" / borsh.U64
)

# ================================================================================
#
class IncreaseLockedAmountAccounts(typing.TypedDict):
    locker:        Pubkey
    escrow:        Pubkey
    escrow_tokens: Pubkey
    payer:         Pubkey
    source_tokens: Pubkey

# ================================================================================
#
def increase_locked_amount(args:               IncreaseLockedAmountArgs,
                           accounts:           IncreaseLockedAmountAccounts,
                           program_id:         Pubkey = PROGRAM_ID,
                           remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["locker"],        is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow"],        is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow_tokens"], is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["payer"],         is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["source_tokens"], is_signer=False, is_writable=True ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID,          is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\x05\xa8v5H.\xcb\x92"
    encoded_args = layout.build({
        "amount": args["amount"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
