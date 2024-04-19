# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey         import Pubkey
from   solders.system_program import ID as SYS_PROGRAM_ID
from   solders.instruction    import Instruction, AccountMeta
from   construct              import Construct
import borsh_construct        as borsh
from ..                       import types
from ..program_id             import PROGRAM_ID

# =============================================================================
#
class CreateProposalArgs(typing.TypedDict):
    proposal_type: int
    max_option:    int
    instructions:  list[types.proposal_instruction.ProposalInstruction]

# =============================================================================
#
layout = borsh.CStruct(
    "proposal_type" / borsh.U8,
    "max_option"    / borsh.U8,
    "instructions"  / borsh.Vec(
        typing.cast(Construct, types.proposal_instruction.ProposalInstruction.layout)
    ),
)

# =============================================================================
#
class CreateProposalAccounts(typing.TypedDict):
    governor:        Pubkey
    proposal:        Pubkey
    smart_wallet:    Pubkey
    proposer:        Pubkey
    payer:           Pubkey
    event_authority: Pubkey
    program:         Pubkey

# =============================================================================
#
def create_proposal(args:               CreateProposalArgs,
                    accounts:           CreateProposalAccounts,
                    program_id:         Pubkey = PROGRAM_ID,
                    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"],        is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["proposal"],        is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["smart_wallet"],    is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["proposer"],        is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["payer"],           is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=SYS_PROGRAM_ID,              is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["event_authority"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["program"],         is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\x84tD\xae\xd8\xa0\xc6\x16"
    encoded_args = layout.build({
            "proposal_type": args["proposal_type"],
            "max_option":    args["max_option"],
            "instructions":  list(map(lambda item: item.to_encodable(), args["instructions"])),
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
