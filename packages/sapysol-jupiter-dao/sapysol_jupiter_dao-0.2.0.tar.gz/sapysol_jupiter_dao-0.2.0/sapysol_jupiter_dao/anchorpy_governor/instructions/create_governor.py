# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey           import Pubkey
from   solders.system_program   import ID as SYS_PROGRAM_ID
from   solders.instruction      import Instruction, AccountMeta
from   anchorpy.borsh_extension import BorshPubkey
import borsh_construct          as borsh
from ..                         import types
from ..program_id               import PROGRAM_ID

# =============================================================================
#
class CreateGovernorArgs(typing.TypedDict):
    locker: Pubkey
    params: types.governance_parameters.GovernanceParameters

# =============================================================================
#
layout = borsh.CStruct(
    "locker" / BorshPubkey,
    "params" / types.governance_parameters.GovernanceParameters.layout,
)

# =============================================================================
#
class CreateGovernorAccounts(typing.TypedDict):
    base:         Pubkey
    governor:     Pubkey
    smart_wallet: Pubkey
    payer:        Pubkey

# =============================================================================
#
def create_governor(args:               CreateGovernorArgs,
                    accounts:           CreateGovernorAccounts,
                    program_id:         Pubkey = PROGRAM_ID,
                    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["base"],         is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["governor"],     is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["smart_wallet"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["payer"],        is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=SYS_PROGRAM_ID,           is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"g\x1eN\xfc\x1c\x80(\x03"
    encoded_args = layout.build({
        "locker": args["locker"],
        "params": args["params"].to_encodable(),
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
