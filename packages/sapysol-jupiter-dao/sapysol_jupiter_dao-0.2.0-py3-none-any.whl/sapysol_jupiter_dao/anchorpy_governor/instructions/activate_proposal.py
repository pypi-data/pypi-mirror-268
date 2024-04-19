# =============================================================================
# 
from __future__ import annotations
from   solders.pubkey      import Pubkey
from   solders.instruction import Instruction, AccountMeta
from ..program_id          import PROGRAM_ID
import typing

# =============================================================================
# 
class ActivateProposalAccounts(typing.TypedDict):
    governor: Pubkey
    proposal: Pubkey
    locker:   Pubkey

# =============================================================================
#
def activate_proposal(accounts:           ActivateProposalAccounts,
                      program_id:         Pubkey = PROGRAM_ID,
                      remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["proposal"], is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["locker"],   is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"Z\xba\xcb\xeaF\xb9\xbf\x15"
    encoded_args = b""
    data         = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
