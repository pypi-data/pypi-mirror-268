# ================================================================================
#
from __future__ import annotations
import typing
from   dataclasses              import dataclass
from   anchorpy.borsh_extension import EnumForCodegen
import borsh_construct          as borsh

# ================================================================================
#
class YesNoJSON(typing.TypedDict):
    kind: typing.Literal["YesNo"]

# ================================================================================
#
class OptionJSON(typing.TypedDict):
    kind: typing.Literal["Option"]

# ================================================================================
#
@dataclass
class YesNo:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "YesNo"

    @classmethod
    def to_json(cls) -> YesNoJSON:
        return YesNoJSON(kind="YesNo")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"YesNo": {}}

# ================================================================================
#
@dataclass
class Option:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "Option"

    @classmethod
    def to_json(cls) -> OptionJSON:
        return OptionJSON(kind="Option")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"Option": {}}

# ================================================================================
#
ProposalTypeKind = typing.Union[YesNo,     Option    ]
ProposalTypeJSON = typing.Union[YesNoJSON, OptionJSON]

# ================================================================================
#
def from_decoded(obj: dict) -> ProposalTypeKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "YesNo" in obj:
        return YesNo()
    if "Option" in obj:
        return Option()
    raise ValueError("Invalid enum object")

# ================================================================================
#
def from_json(obj: ProposalTypeJSON) -> ProposalTypeKind:
    if obj["kind"] == "YesNo":
        return YesNo()
    if obj["kind"] == "Option":
        return Option()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")

# ================================================================================
#
layout = EnumForCodegen(
    "YesNo"  / borsh.CStruct(),
    "Option" / borsh.CStruct()
)

# ================================================================================
#