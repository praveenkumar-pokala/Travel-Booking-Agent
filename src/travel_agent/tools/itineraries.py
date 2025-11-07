import json

def run_plan_itinerary_tool(tool_args: dict) -> str:
    origin = tool_args["origin"]
    destination = tool_args["destination"]
    depart_date = tool_args["depart_date"]
    return_date = tool_args.get("return_date")
    preferences = tool_args.get("preferences", "")
    summary = f"Trip from {origin} to {destination} starting {depart_date}."
    if return_date:
        summary += f" Returning on {return_date}."
    itinerary = {
        "summary": summary,
        "notes": f"Preferences: {preferences}",
        "days": [{"day": 1, "title": f"Arrival in {destination}", "activities": ["Check in", "City walk"]}],
    }
    return json.dumps({"itinerary": itinerary}, ensure_ascii=False)
