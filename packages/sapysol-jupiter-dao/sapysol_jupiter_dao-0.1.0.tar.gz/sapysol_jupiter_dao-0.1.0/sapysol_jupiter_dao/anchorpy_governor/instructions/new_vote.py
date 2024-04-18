# =============================================================================
#
from __future__ import annotations
from   solders.pubkey           import Pubkey
from   solders.keypair          import Keypair
from   solders.system_program   import ID as SYS_PROGRAM_ID
from   solders.instruction      import Instruction, AccountMeta
from   anchorpy.borsh_extension import BorshPubkey
import borsh_construct          as borsh
from ..program_id               import PROGRAM_ID
import typing

# =============================================================================
#
class NewVoteArgs(typing.TypedDict):
    voter: Pubkey

# =============================================================================
#
layout = borsh.CStruct(
    "voter" / BorshPubkey
)

# =============================================================================
#
class NewVoteAccounts(typing.TypedDict):
    proposal: Pubkey
    vote:     Pubkey
    payer:    Pubkey

# =============================================================================
#
def new_vote(args:               NewVoteArgs,
             accounts:           NewVoteAccounts,
             program_id:         Pubkey = PROGRAM_ID,
             remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["proposal"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["vote"],     is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["payer"],    is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=SYS_PROGRAM_ID,       is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xa3l\x9d\xbd\x8cP\r\x8f"
    encoded_args = layout.build({
        "voter": args["voter"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
