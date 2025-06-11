from typing import Dict, List, Any
from langgraph.graph import MessagesState
from assistant.models import Instruction, JsonPatch

class AppState(MessagesState):
  document: Dict[str, Any]
  schema: Dict[str, Any]
  instructions: List[Instruction]
  patches: List[JsonPatch]