# ================================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   spl.token.constants import TOKEN_PROGRAM_ID
from   solders.instruction import Instruction, AccountMeta
from ..program_id          import PROGRAM_ID

# ================================================================================
#
class WithdrawAccounts(typing.TypedDict):
    locker:             Pubkey
    escrow:             Pubkey
    escrow_owner:       Pubkey
    escrow_tokens:      Pubkey
    destination_tokens: Pubkey
    payer:              Pubkey

# ================================================================================
#
def withdraw(accounts:           WithdrawAccounts,
             program_id:         Pubkey = PROGRAM_ID,
             remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["locker"],             is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow"],             is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow_owner"],       is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["escrow_tokens"],      is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["destination_tokens"], is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["payer"],              is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID,               is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b'\xb7\x12F\x9c\x94m\xa1"'
    encoded_args = b""
    data         = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
