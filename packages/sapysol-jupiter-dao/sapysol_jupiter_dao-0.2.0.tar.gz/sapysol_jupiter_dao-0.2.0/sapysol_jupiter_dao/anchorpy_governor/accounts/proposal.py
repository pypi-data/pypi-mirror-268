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
from ..                         import types
from ..program_id               import PROGRAM_ID

# ================================================================================
#
class ProposalJSON(typing.TypedDict):
    governor:             str
    index:                int
    bump:                 int
    proposer:             str
    quorum_votes:         int
    max_option:           int
    option_votes:         list[int]
    canceled_at:          int
    created_at:           int
    activated_at:         int
    voting_ends_at:       int
    queued_at:            int
    queued_transaction:   str
    voting_reward:        types.voting_reward.VotingRewardJSON
    total_claimed_reward: int
    proposal_type:        int
    buffers:              list[int]
    instructions:         list[types.proposal_instruction.ProposalInstructionJSON]

# ================================================================================
#
@dataclass
class Proposal:
    discriminator: typing.ClassVar = b"\x1a^\xbd\xbbt\x885!"
    layout: typing.ClassVar = borsh.CStruct(
        "governor"             / BorshPubkey,
        "index"                / borsh.U64,
        "bump"                 / borsh.U8,
        "proposer"             / BorshPubkey,
        "quorum_votes"         / borsh.U64,
        "max_option"           / borsh.U8,
        "option_votes"         / borsh.Vec(typing.cast(Construct, borsh.U64)),
        "canceled_at"          / borsh.I64,
        "created_at"           / borsh.I64,
        "activated_at"         / borsh.I64,
        "voting_ends_at"       / borsh.I64,
        "queued_at"            / borsh.I64,
        "queued_transaction"   / BorshPubkey,
        "voting_reward"        / types.voting_reward.VotingReward.layout,
        "total_claimed_reward" / borsh.U64,
        "proposal_type"        / borsh.U8,
        "buffers"              / borsh.U128[10],
        "instructions"
        / borsh.Vec(
            typing.cast(
                Construct, types.proposal_instruction.ProposalInstruction.layout
            )
        ),
    )
    governor:             Pubkey
    index:                int
    bump:                 int
    proposer:             Pubkey
    quorum_votes:         int
    max_option:           int
    option_votes:         list[int]
    canceled_at:          int
    created_at:           int
    activated_at:         int
    voting_ends_at:       int
    queued_at:            int
    queued_transaction:   Pubkey
    voting_reward:        types.voting_reward.VotingReward
    total_claimed_reward: int
    proposal_type:        int
    buffers:              list[int]
    instructions:         list[types.proposal_instruction.ProposalInstruction]

    # ========================================
    #
    @classmethod
    def fetch(cls,
              conn:       Client,
              address:    Pubkey,
              commitment: typing.Optional[Commitment] = None,
              program_id: Pubkey = PROGRAM_ID) -> typing.Optional["Proposal"]:

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
                       program_id: Pubkey = PROGRAM_ID) -> typing.List[typing.Optional["Proposal"]]:

        entries: typing.List[typing.Optional[Account]] = conn.get_multiple_accounts(pubkeys=addresses, commitment=commitment).value
        for entry in entries:
            if entry.owner != program_id:
                raise ValueError("Account does not belong to this program")
        return [ Proposal.decode(entry.data) if entry else None for entry in entries ]

    # ========================================
    #
    @classmethod
    def decode(cls, data: bytes) -> "Proposal":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator("The discriminator for this account is invalid")
        dec = Proposal.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(governor             = dec.governor,
                   index                = dec.index,
                   bump                 = dec.bump,
                   proposer             = dec.proposer,
                   quorum_votes         = dec.quorum_votes,
                   max_option           = dec.max_option,
                   option_votes         = dec.option_votes,
                   canceled_at          = dec.canceled_at,
                   created_at           = dec.created_at,
                   activated_at         = dec.activated_at,
                   voting_ends_at       = dec.voting_ends_at,
                   queued_at            = dec.queued_at,
                   queued_transaction   = dec.queued_transaction,
                   voting_reward        = types.voting_reward.VotingReward.from_decoded(dec.voting_reward),
                   total_claimed_reward = dec.total_claimed_reward,
                   proposal_type        = dec.proposal_type,
                   buffers              = dec.buffers,
                   instructions         = list(
                       map(
                           lambda item: types.proposal_instruction.ProposalInstruction.from_decoded(
                               item
                           ),
                           dec.instructions,
                       )
                   ),
        )

    # ========================================
    #
    def to_json(self) -> ProposalJSON:
        return {
            "governor":           str(self.governor),
            "index":                  self.index,
            "bump":                   self.bump,
            "proposer":           str(self.proposer),
            "quorum_votes":           self.quorum_votes,
            "max_option":             self.max_option,
            "option_votes":           self.option_votes,
            "canceled_at":            self.canceled_at,
            "created_at":             self.created_at,
            "activated_at":           self.activated_at,
            "voting_ends_at":         self.voting_ends_at,
            "queued_at":              self.queued_at,
            "queued_transaction": str(self.queued_transaction),
            "voting_reward":          self.voting_reward.to_json(),
            "total_claimed_reward":   self.total_claimed_reward,
            "proposal_type":          self.proposal_type,
            "buffers":                self.buffers,
            "instructions":           list(map(lambda item: item.to_json(), self.instructions)),
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: ProposalJSON) -> "Proposal":
        return cls(governor             = Pubkey.from_string(obj["governor"]),
                   index                = obj["index"],
                   bump                 = obj["bump"],
                   proposer             = Pubkey.from_string(obj["proposer"]),
                   quorum_votes         = obj["quorum_votes"],
                   max_option           = obj["max_option"],
                   option_votes         = obj["option_votes"],
                   canceled_at          = obj["canceled_at"],
                   created_at           = obj["created_at"],
                   activated_at         = obj["activated_at"],
                   voting_ends_at       = obj["voting_ends_at"],
                   queued_at            = obj["queued_at"],
                   queued_transaction   = Pubkey.from_string(obj["queued_transaction"]),
                   voting_reward        = types.voting_reward.VotingReward.from_json(obj["voting_reward"]),
                   total_claimed_reward = obj["total_claimed_reward"],
                   proposal_type        = obj["proposal_type"],
                   buffers              = obj["buffers"],
                   instructions         = list(
                       map(
                           lambda item: types.proposal_instruction.ProposalInstruction.from_json(
                               item
                           ),
                           obj["instructions"],
                       )
                   ),
        )

# ================================================================================
#
