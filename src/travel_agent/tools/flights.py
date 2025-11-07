from dataclasses import dataclass, asdict
from typing import List, Optional
import json
import datetime as dt

@dataclass
class FlightOption:
    airline: str
    depart_time: str
    arrive_time: str
    price_inr: int
    stops: int
    booking_url: str

def fake_web_flight_search(
    origin: str,
    destination: str,
    depart_date: str,
    return_date: Optional[str] = None,
    max_price: Optional[int] = None,
) -> List[FlightOption]:
    base_date = dt.date.fromisoformat(depart_date)
    options = [
        FlightOption(
            airline="IndiGo + Qatar",
            depart_time=str(dt.datetime.combine(base_date, dt.time(hour=4, minute=30))),
            arrive_time=str(dt.datetime.combine(base_date, dt.time(hour=14, minute=10))),
            price_inr=52000,
            stops=1,
            booking_url="https://example.com/booking/indigo-qatar",
        ),
        FlightOption(
            airline="British Airways",
            depart_time=str(dt.datetime.combine(base_date, dt.time(hour=7, minute=45))),
            arrive_time=str(dt.datetime.combine(base_date, dt.time(hour=13, minute=10))),
            price_inr=67000,
            stops=0,
            booking_url="https://example.com/booking/ba-direct",
        ),
    ]
    if max_price is not None:
        options = [o for o in options if o.price_inr <= max_price]
    return options

def run_search_flights_tool(tool_args: dict) -> str:
    options = fake_web_flight_search(
        origin=tool_args["origin"],
        destination=tool_args["destination"],
        depart_date=tool_args["depart_date"],
        return_date=tool_args.get("return_date"),
        max_price=tool_args.get("max_price"),
    )
    return json.dumps({"flights": [asdict(o) for o in options]}, ensure_ascii=False)
