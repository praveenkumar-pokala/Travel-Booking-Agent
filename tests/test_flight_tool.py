from travel_agent.tools.flights import fake_web_flight_search

def test_fake_web_flight_search_basic():
    flights = fake_web_flight_search(
        origin="HYD",
        destination="LHR",
        depart_date="2025-11-15",
        max_price=None,
    )
    assert len(flights) >= 1
    for f in flights:
        assert f.price_inr > 0
        assert f.airline

def test_fake_web_flight_search_price_filter():
    flights = fake_web_flight_search(
        origin="HYD",
        destination="LHR",
        depart_date="2025-11-15",
        max_price=55000,
    )
    assert all(f.price_inr <= 55000 for f in flights)
