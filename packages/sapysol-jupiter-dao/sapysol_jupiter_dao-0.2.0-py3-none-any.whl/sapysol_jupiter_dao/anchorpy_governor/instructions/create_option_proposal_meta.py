# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey         import Pubkey
from   solders.system_program import ID as SYS_PROGRAM_ID
from   solders.instruction    import Instruction, AccountMeta
from   construct              import Construct
import borsh_construct        as borsh
from ..program_id             import PROGRAM_ID

# =============================================================================
#
class CreateOptionProposalMetaArgs(typing.TypedDict):
    bump:                int
    option_descriptions: list[str]

# =============================================================================
#
layout = borsh.CStruct(
    "bump"                / borsh.U8,
    "option_descriptions" / borsh.Vec(typing.cast(Construct, borsh.String)),
)

# =============================================================================
#
class CreateOptionProposalMetaAccounts(typing.TypedDict):
    proposal:             Pubkey
    proposer:             Pubkey
    option_proposal_meta: Pubkey
    payer:                Pubkey
    event_authority:      Pubkey
    program:              Pubkey

# =============================================================================
#
def create_option_proposal_meta(args:               CreateOptionProposalMetaArgs,
                                accounts:           CreateOptionProposalMetaAccounts,
                                program_id:         Pubkey = PROGRAM_ID,
                                remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["proposal"],             is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["proposer"],             is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["option_proposal_meta"], is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["payer"],                is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=SYS_PROGRAM_ID,                   is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["event_authority"],      is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["program"],              is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\x98\x90h\xe4\xf5\xea\xa4\xe0"
    encoded_args = layout.build({
        "bump":                args["bump"],
        "option_descriptions": args["option_descriptions"],
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
