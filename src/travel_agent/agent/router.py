from typing import Dict, Any
import logging
import json

from ..tools.flights import run_search_flights_tool
from ..tools.hotels import run_search_hotels_tool
from ..tools.itineraries import run_plan_itinerary_tool

logger = logging.getLogger(__name__)

def dispatch_tool_call(tool_name: str, tool_args: Dict[str, Any]) -> str:
    if tool_name == "search_flights":
        return run_search_flights_tool(tool_args)
    if tool_name == "search_hotels":
        return run_search_hotels_tool(tool_args)
    if tool_name == "plan_itinerary":
        return run_plan_itinerary_tool(tool_args)
    logger.warning("Unknown tool '%s'", tool_name)
    return json.dumps({"error": f"Unknown tool '{tool_name}'"})
