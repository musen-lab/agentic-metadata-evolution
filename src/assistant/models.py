from typing import List, Literal, Optional
from pydantic import BaseModel, Field

class ChangeInstruction(BaseModel):
  instructions: List[str] = Field(
    description="A list of instructions to update the metadata.")

class Instruction(BaseModel):
  command: str = Field(
    description="The instruction command to generate the metadata.")
  note: str = Field(
    description="A note to explain the instruction command.")

class JsonPatch(BaseModel):
  op: Literal["add", "remove", "replace"] = Field(
    description="The patching operation to perform on the target document.")
  path: str = Field(
    description="A string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.")
  value_json: Optional[str] = Field(
    default=None, 
    description="The JSON value to be added or replaced. Not required for 'remove' operations.")