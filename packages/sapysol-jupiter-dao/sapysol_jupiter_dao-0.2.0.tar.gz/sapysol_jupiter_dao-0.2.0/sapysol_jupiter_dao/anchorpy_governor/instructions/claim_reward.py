# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   spl.token.constants import TOKEN_PROGRAM_ID
from   solders.instruction import Instruction, AccountMeta
from ..program_id          import PROGRAM_ID

# =============================================================================
#
class ClaimRewardAccounts(typing.TypedDict):
    governor:            Pubkey
    reward_vault:        Pubkey
    proposal:            Pubkey
    vote:                Pubkey
    voter:               Pubkey
    voter_token_account: Pubkey
    event_authority:     Pubkey
    program:             Pubkey

# =============================================================================
#
def claim_reward(accounts:           ClaimRewardAccounts,
                 program_id:         Pubkey = PROGRAM_ID,
                 remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"],            is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["reward_vault"],        is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["proposal"],            is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["vote"],                is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["voter"],               is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["voter_token_account"], is_signer=False, is_writable=True ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID,                is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["event_authority"],     is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["program"],             is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\x95_\xb5\xf2^Z\x9e\xa2"
    encoded_args = b""
    data         = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
