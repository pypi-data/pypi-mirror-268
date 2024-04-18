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
from   sapysol.helpers          import MakePubkey, FetchAccount, FetchAccounts

# ================================================================================
#
class EscrowJSON(typing.TypedDict):
    locker:            str
    owner:             str
    bump:              int
    tokens:            str
    amount:            int
    escrow_started_at: int
    escrow_ends_at:    int
    vote_delegate:     str
    is_max_lock:       bool
    buffers:           list[int]

# ================================================================================
#
@dataclass
class Escrow:
    discriminator: typing.ClassVar = b"\x1f\xd5{\xbb\xba\x16\xda\x9b"
    layout: typing.ClassVar = borsh.CStruct(
        "locker"            / BorshPubkey,
        "owner"             / BorshPubkey,
        "bump"              / borsh.U8,
        "tokens"            / BorshPubkey,
        "amount"            / borsh.U64,
        "escrow_started_at" / borsh.I64,
        "escrow_ends_at"    / borsh.I64,
        "vote_delegate"     / BorshPubkey,
        "is_max_lock"       / borsh.Bool,
        "buffers"           / borsh.U128[10],
    )
    locker:            Pubkey
    owner:             Pubkey
    bump:              int
    tokens:            Pubkey
    amount:            int
    escrow_started_at: int
    escrow_ends_at:    int
    vote_delegate:     Pubkey
    is_max_lock:       bool
    buffers:           list[int]

    # ========================================
    #
    @classmethod
    def fetch(cls,
              conn:       Client,
              address:    Pubkey,
              commitment: typing.Optional[Commitment] = None,
              program_id: Pubkey = PROGRAM_ID) -> typing.Optional["Escrow"]:

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
                       program_id: Pubkey = PROGRAM_ID) -> typing.List[typing.Optional["Escrow"]]:

        entries = FetchAccounts(connection   = conn, 
                                pubkeys      = addresses,
                                requiredOwner= program_id,
                                commitment   = commitment)
        return [ Escrow.decode(entry.data) if entry else None for entry in entries ]

    # ========================================
    #
    @classmethod
    def decode(cls, data: bytes) -> "Escrow":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")
        dec = Escrow.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(locker            = dec.locker,
                   owner             = dec.owner,
                   bump              = dec.bump,
                   tokens            = dec.tokens,
                   amount            = dec.amount,
                   escrow_started_at = dec.escrow_started_at,
                   escrow_ends_at    = dec.escrow_ends_at,
                   vote_delegate     = dec.vote_delegate,
                   is_max_lock       = dec.is_max_lock,
                   buffers           = dec.buffers)

    # ========================================
    #
    def to_json(self) -> EscrowJSON:
        return {
            "locker":            str(self.locker),
            "owner":             str(self.owner),
            "bump":                  self.bump,
            "tokens":            str(self.tokens),
            "amount":                self.amount,
            "escrow_started_at":     self.escrow_started_at,
            "escrow_ends_at":        self.escrow_ends_at,
            "vote_delegate":     str(self.vote_delegate),
            "is_max_lock":           self.is_max_lock,
            "buffers":               self.buffers,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: EscrowJSON) -> "Escrow":
        return cls(locker            = MakePubkey(obj["locker"]),
                   owner             = MakePubkey(obj["owner"]),
                   bump              =            obj["bump"],
                   tokens            = MakePubkey(obj["tokens"]),
                   amount            =            obj["amount"],
                   escrow_started_at =            obj["escrow_started_at"],
                   escrow_ends_at    =            obj["escrow_ends_at"],
                   vote_delegate     = MakePubkey(obj["vote_delegate"]),
                   is_max_lock       =            obj["is_max_lock"],
                   buffers           =            obj["buffers"])

# ================================================================================
#
