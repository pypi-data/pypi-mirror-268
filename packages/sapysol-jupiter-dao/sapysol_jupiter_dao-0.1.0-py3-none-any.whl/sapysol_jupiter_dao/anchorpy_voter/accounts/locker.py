# ================================================================================
#
import typing
from   dataclasses              import dataclass
from   solders.pubkey           import Pubkey
from   solders.account          import Account
from   solana.rpc.api           import Client
from   solana.rpc.commitment    import Commitment
import borsh_construct          as borsh
from   anchorpy.coder.accounts  import ACCOUNT_DISCRIMINATOR_SIZE
from   anchorpy.error           import AccountInvalidDiscriminator
from   anchorpy.utils.rpc       import get_multiple_accounts
from   anchorpy.borsh_extension import BorshPubkey
from ..program_id               import PROGRAM_ID
from ..                         import types
from   sapysol.helpers          import MakePubkey, FetchAccount, FetchAccounts

# ================================================================================
#
class LockerJSON(typing.TypedDict):
    base:          str
    bump:          int
    token_mint:    str
    locked_supply: int
    total_escrow:  int
    governor:      str
    params:        types.locker_params.LockerParamsJSON
    buffers:       list[int]

# ================================================================================
#
@dataclass
class Locker:
    discriminator: typing.ClassVar = b"J\xf6\x06q\xf9\xe4K\xa9"
    layout: typing.ClassVar = borsh.CStruct(
        "base"          / BorshPubkey,
        "bump"          / borsh.U8,
        "token_mint"    / BorshPubkey,
        "locked_supply" / borsh.U64,
        "total_escrow"  / borsh.U64,
        "governor"      / BorshPubkey,
        "params"        / types.locker_params.LockerParams.layout,
        "buffers"       / borsh.U128[32],
    )
    base:          Pubkey
    bump:          int
    token_mint:    Pubkey
    locked_supply: int
    total_escrow:  int
    governor:      Pubkey
    params:        types.locker_params.LockerParams
    buffers:       list[int]

    # ========================================
    #
    @classmethod
    def fetch(cls,
              conn:       Client,
              address:    Pubkey,
              commitment: typing.Optional[Commitment] = None,
              program_id: Pubkey = PROGRAM_ID) -> typing.Optional["Locker"]:

        resp = FetchAccount(connection    = conn, 
                            pubkey        = address,
                            requiredOwner = program_id,
                            commitment    = commitment)
        return None if resp is None else cls.decode(resp.data)

    # ========================================
    #
    @classmethod
    def fetch_multiple(cls,
                       conn:       Client,
                       addresses:  list[Pubkey],
                       commitment: typing.Optional[Commitment] = None,
                       program_id: Pubkey = PROGRAM_ID) -> typing.List[typing.Optional["Locker"]]:

        entries = FetchAccounts(connection   = conn, 
                                pubkeys      = addresses,
                                requiredOwner= program_id,
                                commitment   = commitment)
        return [ Locker.decode(entry.data) if entry else None for entry in entries ]

    # ========================================
    #
    @classmethod
    def decode(cls, data: bytes) -> "Locker":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")
        dec = Locker.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(base          = dec.base,
                   bump          = dec.bump,
                   token_mint    = dec.token_mint,
                   locked_supply = dec.locked_supply,
                   total_escrow  = dec.total_escrow,
                   governor      = dec.governor,
                   params        = types.locker_params.LockerParams.from_decoded(dec.params),
                   buffers       = dec.buffers)

    # ========================================
    #
    def to_json(self) -> LockerJSON:
        return {
            "base":          str(self.base),
            "bump":              self.bump,
            "token_mint":    str(self.token_mint),
            "locked_supply":     self.locked_supply,
            "total_escrow":      self.total_escrow,
            "governor":      str(self.governor),
            "params":            self.params.to_json(),
            "buffers":           self.buffers,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: LockerJSON) -> "Locker":
        return cls(base          = MakePubkey(obj["base"]),
                   bump          =            obj["bump"],
                   token_mint    = MakePubkey(obj["token_mint"]),
                   locked_supply =            obj["locked_supply"],
                   total_escrow  =            obj["total_escrow"],
                   governor      = MakePubkey(obj["governor"]),
                   params        = types.locker_params.LockerParams.from_json(obj["params"]),
                   buffers       =            obj["buffers"])

# ================================================================================
#
