from dataclasses import dataclass, asdict
from typing import List, Optional
import json

@dataclass
class HotelOption:
    name: str
    city: str
    price_per_night_inr: int
    rating: float
    distance_to_center_km: float
    booking_url: str

def fake_web_hotel_search(
    city: str,
    checkin_date: str,
    checkout_date: str,
    max_price_per_night: Optional[int] = None,
) -> List[HotelOption]:
    options = [
        HotelOption(
            name="Central Business Hotel",
            city=city,
            price_per_night_inr=8000,
            rating=4.3,
            distance_to_center_km=1.0,
            booking_url="https://example.com/hotel/central",
        ),
        HotelOption(
            name="Budget Inn",
            city=city,
            price_per_night_inr=4500,
            rating=3.9,
            distance_to_center_km=3.0,
            booking_url="https://example.com/hotel/budget-inn",
        ),
    ]
    if max_price_per_night is not None:
        options = [o for o in options if o.price_per_night_inr <= max_price_per_night]
    return options

def run_search_hotels_tool(tool_args: dict) -> str:
    options = fake_web_hotel_search(
        city=tool_args["city"],
        checkin_date=tool_args["checkin_date"],
        checkout_date=tool_args["checkout_date"],
        max_price_per_night=tool_args.get("max_price_per_night"),
    )
    return json.dumps({"hotels": [asdict(o) for o in options]}, ensure_ascii=False)
