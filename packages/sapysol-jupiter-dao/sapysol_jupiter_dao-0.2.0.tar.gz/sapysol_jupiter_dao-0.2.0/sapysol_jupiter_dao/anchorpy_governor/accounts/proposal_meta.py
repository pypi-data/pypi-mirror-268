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
class ProposalMetaJSON(typing.TypedDict):
    proposal:         str
    title:            str
    description_link: str

# ================================================================================
#
@dataclass
class ProposalMeta:
    discriminator: typing.ClassVar = b"2d.\x18\x97\xae\xd8N"
    layout: typing.ClassVar = borsh.CStruct(
        "proposal"         / BorshPubkey,
        "title"            / borsh.String,
        "description_link" / borsh.String,
    )
    proposal:         Pubkey
    title:            str
    description_link: str

    # ========================================
    #
    @classmethod
    def fetch(cls,
              conn:       Client,
              address:    Pubkey,
              commitment: typing.Optional[Commitment] = None,
              program_id: Pubkey = PROGRAM_ID) -> typing.Optional["ProposalMeta"]:

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
                       program_id: Pubkey = PROGRAM_ID) -> typing.List[typing.Optional["ProposalMeta"]]:

        entries: typing.List[typing.Optional[Account]] = conn.get_multiple_accounts(pubkeys=addresses, commitment=commitment).value
        for entry in entries:
            if entry.owner != program_id:
                raise ValueError("Account does not belong to this program")
        return [ ProposalMeta.decode(entry.data) if entry else None for entry in entries ]

    # ========================================
    #
    @classmethod
    def decode(cls, data: bytes) -> "ProposalMeta":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")
        dec = ProposalMeta.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(proposal         = dec.proposal,
                   title            = dec.title,
                   description_link = dec.description_link)

    # ========================================
    #
    def to_json(self) -> ProposalMetaJSON:
        return {
            "proposal":     str(self.proposal),
            "title":            self.title,
            "description_link": self.description_link,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: ProposalMetaJSON) -> "ProposalMeta":
        return cls(proposal         = Pubkey.from_string(obj["proposal"]),
                   title            = obj["title"],
                   description_link = obj["description_link"])

# ================================================================================
#
