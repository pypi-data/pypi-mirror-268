# =============================================================================
#
from __future__ import annotations
import typing
from solders.pubkey import Pubkey
from solders.system_program import ID as SYS_PROGRAM_ID
from solders.instruction import Instruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID

# =============================================================================
#
class CreateProposalMetaArgs(typing.TypedDict):
    bump:             int
    title:            str
    description_link: str

# =============================================================================
#
layout = borsh.CStruct(
    "bump"             / borsh.U8,
    "title"            / borsh.String,
    "description_link" / borsh.String
)

# =============================================================================
#
class CreateProposalMetaAccounts(typing.TypedDict):
    proposal:        Pubkey
    proposer:        Pubkey
    proposal_meta:   Pubkey
    payer:           Pubkey
    event_authority: Pubkey
    program:         Pubkey

# =============================================================================
#
def create_proposal_meta(args:               CreateProposalMetaArgs,
                         accounts:           CreateProposalMetaAccounts,
                         program_id:         Pubkey = PROGRAM_ID,
                         remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["proposal"],        is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["proposer"],        is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["proposal_meta"],   is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["payer"],           is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=SYS_PROGRAM_ID,              is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["event_authority"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["program"],         is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xee\x8a\xd4\xa0.53X"
    encoded_args = layout.build({
        "bump":             args["bump"],
        "title":            args["title"],
        "description_link": args["description_link"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
