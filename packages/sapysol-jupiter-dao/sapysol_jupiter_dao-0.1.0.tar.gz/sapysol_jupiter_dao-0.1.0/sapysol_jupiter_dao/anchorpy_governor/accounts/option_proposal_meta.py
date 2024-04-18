# ================================================================================
#
import typing
from   dataclasses              import dataclass
from   construct                import Construct
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
class OptionProposalMetaJSON(typing.TypedDict):
    proposal:            str
    option_descriptions: list[str]

# ================================================================================
#
@dataclass
class OptionProposalMeta:
    discriminator: typing.ClassVar = b"\xc88\xe5|q\x9a \x1a"
    layout: typing.ClassVar = borsh.CStruct(
        "proposal"            / BorshPubkey,
        "option_descriptions" / borsh.Vec(typing.cast(Construct, borsh.String)),
    )
    proposal:            Pubkey
    option_descriptions: list[str]

    # ========================================
    #
    @classmethod
    def fetch(cls,
              conn:       Client,
              address:    Pubkey,
              commitment: typing.Optional[Commitment] = None,
              program_id: Pubkey = PROGRAM_ID) -> typing.Optional["OptionProposalMeta"]:

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
                       program_id: Pubkey = PROGRAM_ID) -> typing.List[typing.Optional["OptionProposalMeta"]]:

        entries: typing.List[typing.Optional[Account]] = conn.get_multiple_accounts(pubkeys=addresses, commitment=commitment).value
        for entry in entries:
            if entry.owner != program_id:
                raise ValueError("Account does not belong to this program")
        return [ OptionProposalMeta.decode(entry.data) if entry else None for entry in entries ]

    # ========================================
    #
    @classmethod
    def decode(cls, data: bytes) -> "OptionProposalMeta":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")
        dec = OptionProposalMeta.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(proposal            = dec.proposal,
                   option_descriptions = dec.option_descriptions)

    # ========================================
    #
    def to_json(self) -> OptionProposalMetaJSON:
        return {
            "proposal":            str(self.proposal),
            "option_descriptions": self.option_descriptions,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: OptionProposalMetaJSON) -> "OptionProposalMeta":
        return cls(proposal            = Pubkey.from_string(obj["proposal"]),
                   option_descriptions = obj["option_descriptions"])

# ================================================================================
#
