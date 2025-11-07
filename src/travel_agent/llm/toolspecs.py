SEARCH_FLIGHTS_SPEC = {
    "name": "search_flights",
    "description": "Search available flights between two cities on given dates.",
    "parameters": {
        "type": "object",
        "properties": {
            "origin": {"type": "string"},
            "destination": {"type": "string"},
            "depart_date": {"type": "string"},
            "return_date": {"type": "string", "nullable": True},
            "max_price": {"type": "integer", "nullable": True},
        },
        "required": ["origin", "destination", "depart_date"],
    },
}

SEARCH_HOTELS_SPEC = {
    "name": "search_hotels",
    "description": "Search hotels in a given city for given dates and budget.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "checkin_date": {"type": "string"},
            "checkout_date": {"type": "string"},
            "max_price_per_night": {"type": "integer", "nullable": True},
        },
        "required": ["city", "checkin_date", "checkout_date"],
    },
}

PLAN_ITINERARY_SPEC = {
    "name": "plan_itinerary",
    "description": "Given high-level trip details, draft a simple itinerary.",
    "parameters": {
        "type": "object",
        "properties": {
            "origin": {"type": "string"},
            "destination": {"type": "string"},
            "depart_date": {"type": "string"},
            "return_date": {"type": "string", "nullable": True},
            "preferences": {"type": "string"},
        },
        "required": ["origin", "destination", "depart_date"],
    },
}

ALL_TOOLS = [SEARCH_FLIGHTS_SPEC, SEARCH_HOTELS_SPEC, PLAN_ITINERARY_SPEC]
