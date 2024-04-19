# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   solders.instruction import Instruction, AccountMeta
from ..program_id          import PROGRAM_ID

# =============================================================================
#
class CancelProposalAccounts(typing.TypedDict):
    governor:        Pubkey
    proposal:        Pubkey
    proposer:        Pubkey
    event_authority: Pubkey
    program:         Pubkey

# =============================================================================
#
def cancel_proposal(accounts:           CancelProposalAccounts,
                    program_id:         Pubkey = PROGRAM_ID,
                    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"],        is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["proposal"],        is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["proposer"],        is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["event_authority"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["program"],         is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"jJ\x80\x92\x13A'\x17"
    encoded_args = b""
    data         = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
