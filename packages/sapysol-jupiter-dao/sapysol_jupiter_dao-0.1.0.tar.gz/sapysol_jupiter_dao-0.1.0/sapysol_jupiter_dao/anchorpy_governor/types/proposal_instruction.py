# ================================================================================
#
from __future__ import annotations
import typing
from .                          import proposal_account_meta
from   dataclasses              import dataclass
from   construct                import Container, Construct
from   solders.pubkey           import Pubkey
from   anchorpy.borsh_extension import BorshPubkey
import borsh_construct          as borsh

# ================================================================================
#
class ProposalInstructionJSON(typing.TypedDict):
    program_id: str
    keys:       list[proposal_account_meta.ProposalAccountMetaJSON]
    data:       list[int]

# ================================================================================
#
@dataclass
class ProposalInstruction:
    layout: typing.ClassVar = borsh.CStruct(
        "program_id" / BorshPubkey,
        "keys"       / borsh.Vec(typing.cast(Construct, proposal_account_meta.ProposalAccountMeta.layout)),
        "data"       / borsh.Bytes,
    )
    program_id: Pubkey
    keys:       list[proposal_account_meta.ProposalAccountMeta]
    data:       bytes

    # ========================================
    #
    @classmethod
    def from_decoded(cls, obj: Container) -> "ProposalInstruction":
        return cls(program_id = obj.program_id,
                   keys       = list(map(lambda item: proposal_account_meta.ProposalAccountMeta.from_decoded(item),
                                         obj.keys)),
                   data       = obj.data)

    # ========================================
    #
    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "program_id": self.program_id,
            "keys":       list(map(lambda item: item.to_encodable(), self.keys)),
            "data":       self.data,
        }

    # ========================================
    #
    def to_json(self) -> ProposalInstructionJSON:
        return {
            "program_id": str(self.program_id),
            "keys":       list(map(lambda item: item.to_json(), self.keys)),
            "data":       list(self.data),
        }

    # ========================================
    #
    @classmethod
    def from_json(cls, obj: ProposalInstructionJSON) -> "ProposalInstruction":
        return cls(program_id = Pubkey.from_string(obj["program_id"]),
                   keys       = list(map(lambda item: proposal_account_meta.ProposalAccountMeta.from_json(item),
                                         obj["keys"])),
                   data       = bytes(obj["data"]))

# ================================================================================
#
