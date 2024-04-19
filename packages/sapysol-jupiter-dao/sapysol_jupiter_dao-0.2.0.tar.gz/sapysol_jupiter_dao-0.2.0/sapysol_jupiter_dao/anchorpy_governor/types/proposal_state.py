# ================================================================================
#
from __future__ import annotations
import typing
from   dataclasses              import dataclass
from   anchorpy.borsh_extension import EnumForCodegen
import borsh_construct          as borsh

# ================================================================================
#
class DraftJSON(typing.TypedDict):
    kind: typing.Literal["Draft"]

class ActiveJSON(typing.TypedDict):
    kind: typing.Literal["Active"]

class CanceledJSON(typing.TypedDict):
    kind: typing.Literal["Canceled"]

class DefeatedJSON(typing.TypedDict):
    kind: typing.Literal["Defeated"]

class SucceededJSON(typing.TypedDict):
    kind: typing.Literal["Succeeded"]

class QueuedJSON(typing.TypedDict):
    kind: typing.Literal["Queued"]

# ================================================================================
#
@dataclass
class Draft:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "Draft"

    @classmethod
    def to_json(cls) -> DraftJSON:
        return DraftJSON(kind="Draft")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"Draft": {}}

# ================================================================================
#
@dataclass
class Active:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "Active"

    @classmethod
    def to_json(cls) -> ActiveJSON:
        return ActiveJSON(kind="Active")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"Active": {}}

# ================================================================================
#
@dataclass
class Canceled:
    discriminator: typing.ClassVar = 2
    kind: typing.ClassVar = "Canceled"

    @classmethod
    def to_json(cls) -> CanceledJSON:
        return CanceledJSON(kind="Canceled")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"Canceled": {}}

# ================================================================================
#
@dataclass
class Defeated:
    discriminator: typing.ClassVar = 3
    kind: typing.ClassVar = "Defeated"

    @classmethod
    def to_json(cls) -> DefeatedJSON:
        return DefeatedJSON(kind="Defeated")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"Defeated": {}}

# ================================================================================
#
@dataclass
class Succeeded:
    discriminator: typing.ClassVar = 4
    kind: typing.ClassVar = "Succeeded"

    @classmethod
    def to_json(cls) -> SucceededJSON:
        return SucceededJSON(kind="Succeeded")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"Succeeded": {}}

# ================================================================================
#
@dataclass
class Queued:
    discriminator: typing.ClassVar = 5
    kind: typing.ClassVar = "Queued"

    @classmethod
    def to_json(cls) -> QueuedJSON:
        return QueuedJSON(kind="Queued")

    @classmethod
    def to_encodable(cls) -> dict:
        return {"Queued": {}}

# ================================================================================
#
ProposalStateKind = typing.Union[Draft,     Active,     Canceled,     Defeated,     Succeeded,     Queued    ]
ProposalStateJSON = typing.Union[DraftJSON, ActiveJSON, CanceledJSON, DefeatedJSON, SucceededJSON, QueuedJSON]

# ================================================================================
#
def from_decoded(obj: dict) -> ProposalStateKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Draft" in obj:
        return Draft()
    if "Active" in obj:
        return Active()
    if "Canceled" in obj:
        return Canceled()
    if "Defeated" in obj:
        return Defeated()
    if "Succeeded" in obj:
        return Succeeded()
    if "Queued" in obj:
        return Queued()
    raise ValueError("Invalid enum object")

# ================================================================================
#
def from_json(obj: ProposalStateJSON) -> ProposalStateKind:
    if obj["kind"] == "Draft":
        return Draft()
    if obj["kind"] == "Active":
        return Active()
    if obj["kind"] == "Canceled":
        return Canceled()
    if obj["kind"] == "Defeated":
        return Defeated()
    if obj["kind"] == "Succeeded":
        return Succeeded()
    if obj["kind"] == "Queued":
        return Queued()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")

# ================================================================================
#
layout = EnumForCodegen(
    "Draft"     / borsh.CStruct(),
    "Active"    / borsh.CStruct(),
    "Canceled"  / borsh.CStruct(),
    "Defeated"  / borsh.CStruct(),
    "Succeeded" / borsh.CStruct(),
    "Queued"    / borsh.CStruct(),
)

# ================================================================================
#
