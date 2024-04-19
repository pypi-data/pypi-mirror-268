# =============================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   solders.instruction import Instruction, AccountMeta
import borsh_construct     as borsh
from ..                    import types
from ..program_id          import PROGRAM_ID

# =============================================================================
#
class SetGovernanceParamsArgs(typing.TypedDict):
    params: types.governance_parameters.GovernanceParameters

# =============================================================================
#
layout = borsh.CStruct(
    "params" / types.governance_parameters.GovernanceParameters.layout
)

# =============================================================================
#
class SetGovernanceParamsAccounts(typing.TypedDict):
    governor:     Pubkey
    smart_wallet: Pubkey

# =============================================================================
#
def set_governance_params(args:               SetGovernanceParamsArgs,
                          accounts:           SetGovernanceParamsAccounts,
                          program_id:         Pubkey = PROGRAM_ID,
                          remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["governor"],     is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["smart_wallet"], is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xaf\xbb\x03I\x08\xfbC\xb2"
    encoded_args = layout.build({
        "params": args["params"].to_encodable(),
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# =============================================================================
#
