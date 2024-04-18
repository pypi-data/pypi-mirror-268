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

# ================================================================================
#
class GovernorJSON(typing.TypedDict):
    base:           str
    bump:           int
    proposal_count: int
    locker:         str
    smart_wallet:   str
    params:         types.governance_parameters.GovernanceParametersJSON
    voting_reward:  types.voting_reward.VotingRewardJSON
    buffers:        list[int]

# ================================================================================
#
@dataclass
class Governor:
    discriminator: typing.ClassVar = b"%\x88,PDU\xd5\xb2"
    layout: typing.ClassVar = borsh.CStruct(
        "base"           / BorshPubkey,
        "bump"           / borsh.U8,
        "proposal_count" / borsh.U64,
        "locker"         / BorshPubkey,
        "smart_wallet"   / BorshPubkey,
        "params"         / types.governance_parameters.GovernanceParameters.layout,
        "voting_reward"  / types.voting_reward.VotingReward.layout,
        "buffers"        / borsh.U128[32],
    )
    base:           Pubkey
    bump:           int
    proposal_count: int
    locker:         Pubkey
    smart_wallet:   Pubkey
    params:         types.governance_parameters.GovernanceParameters
    voting_reward:  types.voting_reward.VotingReward
    buffers:        list[int]

    # ========================================
    #
    @classmethod
    def fetch(cls,
              conn:       Client,
              address:    Pubkey,
              commitment: typing.Optional[Commitment] = None,
              program_id: Pubkey = PROGRAM_ID) -> typing.Optional["Governor"]:

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
                       program_id: Pubkey = PROGRAM_ID) -> typing.List[typing.Optional["Governor"]]:

        entries: typing.List[typing.Optional[Account]] = conn.get_multiple_accounts(pubkeys=addresses, commitment=commitment).value
        for entry in entries:
            if entry.owner != program_id:
                raise ValueError("Account does not belong to this program")
        return [ Governor.decode(entry.data) if entry else None for entry in entries ]

    # ========================================
    #
    @classmethod
    def decode(cls, data: bytes) -> "Governor":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")
        dec = Governor.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(base           = dec.base,
                   bump           = dec.bump,
                   proposal_count = dec.proposal_count,
                   locker         = dec.locker,
                   smart_wallet   = dec.smart_wallet,
                   params         = types.governance_parameters.GovernanceParameters.from_decoded(dec.params),
                   voting_reward  = types.voting_reward.VotingReward.from_decoded(dec.voting_reward),
                   buffers        = dec.buffers,
        )

    # ========================================
    #
    def to_json(self) -> GovernorJSON:
        return {
            "base":           str(self.base),
            "bump":           self.bump,
            "proposal_count": self.proposal_count,
            "locker":         str(self.locker),
            "smart_wallet":   str(self.smart_wallet),
            "params":         self.params.to_json(),
            "voting_reward":  self.voting_reward.to_json(),
            "buffers":        self.buffers,
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: GovernorJSON) -> "Governor":
        return cls(base           = Pubkey.from_string(obj["base"]),
                   bump           = obj["bump"],
                   proposal_count = obj["proposal_count"],
                   locker         = Pubkey.from_string(obj["locker"]),
                   smart_wallet   = Pubkey.from_string(obj["smart_wallet"]),
                   params         = types.governance_parameters.GovernanceParameters.from_json(obj["params"]),
                   voting_reward  = types.voting_reward.VotingReward.from_json(obj["voting_reward"]),
                   buffers        = obj["buffers"],
        )

# ================================================================================
#
