from typing import Dict, List, Any
from langgraph.graph import MessagesState

class AppState(MessagesState):
  document: Dict[str, Any]
  schema: Dict[str, Any]
  instructions: List[str]
  patches: List[Dict[str, Any]]