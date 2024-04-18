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

# ================================================================================
#
class VoteJSON(typing.TypedDict):
    proposal:     str
    voter:        str
    bump:         int
    side:         int
    voting_power: int
    claimed:      bool
    buffers:      list[int]

# ================================================================================
#
@dataclass
class Vote:
    discriminator: typing.ClassVar = b"`[h9\x91#\xac\x9b"
    layout: typing.ClassVar = borsh.CStruct(
        "proposal"     / BorshPubkey,
        "voter"        / BorshPubkey,
        "bump"         / borsh.U8,
        "side"         / borsh.U8,
        "voting_power" / borsh.U64,
        "claimed"      / borsh.Bool,
        "buffers"      / borsh.U8[32],
    )
    proposal:     Pubkey
    voter:        Pubkey
    bump:         int
    side:         int
    voting_power: int
    claimed:      bool
    buffers:      list[int]

    # ========================================
    #
    @classmethod
    def fetch(cls,
              conn:       Client,
              address:    Pubkey,
              commitment: typing.Optional[Commitment] = None,
              program_id: Pubkey = PROGRAM_ID) -> typing.Optional["Vote"]:

        resp = conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id:
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    # ========================================
    #
    @classmethod
    def fetch_multiple(cls,
                       conn:       Client,
                       addresses:  list[Pubkey],
                       commitment: typing.Optional[Commitment] = None,
                       program_id: Pubkey = PROGRAM_ID) -> typing.List[typing.Optional["Vote"]]:

        entries: typing.List[typing.Optional[Account]] = conn.get_multiple_accounts(pubkeys=addresses, commitment=commitment).value
        for entry in entries:
            if entry.owner != program_id:
                raise ValueError("Account does not belong to this program")
        return [ Vote.decode(entry.data) if entry else None for entry in entries ]

    # ========================================
    #
    @classmethod
    def decode(cls, data: bytes) -> "Vote":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")

        dec = Vote.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(proposal     = dec.proposal,
                   voter        = dec.voter,
                   bump         = dec.bump,
                   side         = dec.side,
                   voting_power = dec.voting_power,
                   claimed      = dec.claimed,
                   buffers      = dec.buffers,
                  )

    # ========================================
    #
    def to_json(self) -> VoteJSON:
        return {
            "proposal": str(self.proposal),
            "voter":    str(self.voter),
            "bump":         self.bump,
            "side":         self.side,
            "voting_power": self.voting_power,
            "claimed":      self.claimed,
            "buffers":      self.buffers,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: VoteJSON) -> "Vote":
        return cls(proposal     = Pubkey.from_string(obj["proposal"]),
                   voter        = Pubkey.from_string(obj["voter"]),
                   bump         = obj["bump"],
                   side         = obj["side"],
                   voting_power = obj["voting_power"],
                   claimed      = obj["claimed"],
                   buffers      = obj["buffers"],
                  )

# ================================================================================
#
