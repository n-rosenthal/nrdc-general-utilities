"""Test suite for the `Location.py` module
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-28    
"""
#   Test data
VALID_LATITUDES:list[float]     = [];
VALID_LONGITUDES:list[float]    = [];
VALID_TIMEZONES:list[str]       = [];
INVALID_LATITUDES:list[float]   = [];
INVALID_LONGITUDES:list[float]  = [];
INVALID_TIMEZONES:list[str]     = [];

import zoneinfo;


def initializeTestData():
    global VALID_LATITUDES;
    global VALID_LONGITUDES;
    global VALID_TIMEZONES;
    global INVALID_LATITUDES;
    global INVALID_LONGITUDES;
    global INVALID_TIMEZONES;
    
    import random;
    
    VALID_LATITUDES = [random.uniform(-90, 90) for i in range(10)];
    VALID_LONGITUDES = [random.uniform(-180, 180) for i in range(10)];
    VALID_TIMEZONES = [f"UTC{i}" for i in range(10)];
    INVALID_LATITUDES = [random.choice(random.uniform(-180, -90), random.uniform(90, 180)) for i in range(10)];
    INVALID_LONGITUDES = [random.choice(random.uniform(-180, -90), random.uniform(90, 180)) for i in range(10)];
    INVALID_TIMEZONES = [f"UTC{i}" for i in range(10)];
    
    return True;


def test_constructor():
    initializeTestData();
    for i in range(len(VALID_LATITUDES)):
        location = Location(VALID_LATITUDES[i], VALID_LONGITUDES[i], VALID_TIMEZONES[i]);
        assert location.latitude == VALID_LATITUDES[i];
        assert location.longitude == VALID_LONGITUDES[i];
        assert location.timezone == VALID_TIMEZONES[i];
    for i in range(len(INVALID_LATITUDES)):
        location = Location(INVALID_LATITUDES[i], INVALID_LONGITUDES[i], INVALID_TIMEZONES[i]);
        assert location.latitude == INVALID_LATITUDES[i];
        assert location.longitude == INVALID_LONGITUDES[i];
        assert location.timezone == INVALID_TIMEZONES[i];
    return True



if __name__ == "__main__":
    print(zoneinfo.available_timezones());
    test_constructor();