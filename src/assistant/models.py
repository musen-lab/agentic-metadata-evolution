from typing import Dict, List, Any, Literal, Optional
from pydantic import BaseModel, Field

class ChangeInstruction(BaseModel):
  instructions: List[str] = Field(
    description="A list of instructions to update the metadata.")

class JsonPatch(BaseModel):
  op: Literal["add", "remove", "replace"] = Field(
    description="The patching operation to perform on the target document.")
  path: str = Field(
    description="A string containing a JSON-Pointer value that references a location within the target document (the 'target location') where the operation is performed.")
  value: Optional[str] = Field(
    default=None, 
    description="The value to be added or replaced. Not required for 'remove' operations.")