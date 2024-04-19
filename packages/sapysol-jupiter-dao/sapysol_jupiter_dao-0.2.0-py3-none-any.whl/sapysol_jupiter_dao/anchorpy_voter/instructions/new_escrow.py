# ================================================================================
#
from __future__               import annotations
import typing
from   solders.pubkey         import Pubkey
from   solders.system_program import ID as SYS_PROGRAM_ID
from   solders.instruction    import Instruction, AccountMeta
from ..program_id             import PROGRAM_ID

# ================================================================================
#
class NewEscrowAccounts(typing.TypedDict):
    locker:       Pubkey
    escrow:       Pubkey
    escrow_owner: Pubkey
    payer:        Pubkey

# ================================================================================
#
def new_escrow(accounts:           NewEscrowAccounts,
               program_id:         Pubkey = PROGRAM_ID,
               remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["locker"],       is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow"],       is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["escrow_owner"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["payer"],        is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=SYS_PROGRAM_ID,           is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xd8\xb6\x8f\x0b\xdc&V\xb9"
    encoded_args = b""
    data         = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
