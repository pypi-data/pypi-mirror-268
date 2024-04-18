# ================================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey      import Pubkey
from   solders.instruction import Instruction, AccountMeta
import borsh_construct     as borsh
from ..                    import types
from ..program_id          import PROGRAM_ID

# ================================================================================
#
class SetLockerParamsArgs(typing.TypedDict):
    params: types.locker_params.LockerParams

# ================================================================================
#
layout = borsh.CStruct(
    "params" / types.locker_params.LockerParams.layout
)

# ================================================================================
#
class SetLockerParamsAccounts(typing.TypedDict):
    locker:       Pubkey
    governor:     Pubkey
    smart_wallet: Pubkey

# ================================================================================
#
def set_locker_params(args:               SetLockerParamsArgs,
                      accounts:           SetLockerParamsAccounts,
                      program_id:         Pubkey = PROGRAM_ID,
                      remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["locker"],       is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["governor"],     is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["smart_wallet"], is_signer=True,  is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"j'\x84T\xfeM\xa1\xa9"
    encoded_args = layout.build({
        "params": args["params"].to_encodable(),
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
