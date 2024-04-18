# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey         import Pubkey
from   solders.system_program import ID as SYS_PROGRAM_ID
from   solders.instruction    import Instruction, AccountMeta
from ..program_id             import PROGRAM_ID

# =============================================================================
#
class QueueProposalAccounts(typing.TypedDict):
    governor:             Pubkey
    proposal:             Pubkey
    transaction:          Pubkey
    smart_wallet:         Pubkey
    payer:                Pubkey
    smart_wallet_program: Pubkey
    event_authority:      Pubkey
    program:              Pubkey

# =============================================================================
#
def queue_proposal(accounts:           QueueProposalAccounts,
                   program_id:         Pubkey = PROGRAM_ID,
                   remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"],             is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["proposal"],             is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["transaction"],          is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["smart_wallet"],         is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["payer"],                is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["smart_wallet_program"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=SYS_PROGRAM_ID,                   is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["event_authority"],      is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["program"],              is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xa8\xdb\x8b\xd3\xcd\x98}n"
    encoded_args = b""
    data         = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
