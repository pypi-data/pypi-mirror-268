# ================================================================================
#
from __future__ import annotations
import typing
from   solders.pubkey         import Pubkey
from   solders.system_program import ID as SYS_PROGRAM_ID
from   solders.instruction    import Instruction, AccountMeta
import borsh_construct        as borsh
from ..                       import types
from ..program_id             import PROGRAM_ID

# ================================================================================
#
class NewLockerArgs(typing.TypedDict):
    params: types.locker_params.LockerParams

# ================================================================================
#
layout = borsh.CStruct(
    "params" / types.locker_params.LockerParams.layout
)

# ================================================================================
#
class NewLockerAccounts(typing.TypedDict):
    base:       Pubkey
    locker:     Pubkey
    token_mint: Pubkey
    governor:   Pubkey
    payer:      Pubkey

# ================================================================================
#
def new_locker(args:               NewLockerArgs,
               accounts:           NewLockerAccounts,
               program_id:         Pubkey = PROGRAM_ID,
               remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None) -> Instruction:

    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["base"],       is_signer=True,  is_writable=False),
        AccountMeta(pubkey=accounts["locker"],     is_signer=False, is_writable=True ),
        AccountMeta(pubkey=accounts["token_mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["governor"],   is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["payer"],      is_signer=True,  is_writable=True ),
        AccountMeta(pubkey=SYS_PROGRAM_ID,         is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier   = b"\xb1\x85 Z\xe5\xd8\x83/"
    encoded_args = layout.build({
        "params": args["params"].to_encodable(),
    })
    data = identifier + encoded_args
    return Instruction(program_id, data, keys)

# ================================================================================
#
