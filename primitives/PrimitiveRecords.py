from Storable import Storable;
from dataclasses import dataclass;

import datetime;
import json;
import xml;
import csv;
import datetime;

@dataclass
class WeatherData(Storable):
    """`WeatherData` is a dataclass for storing weather data.

    @param temperature: The temperature of the weather data.
    @param humidity: The humidity of the weather data.
    @param pressure: The pressure of the weather data.
    @param wind_speed: The wind speed of the weather data.
    @param wind_direction: The wind direction of the weather data.
    @param cloudiness: The cloudiness of the weather data.
    @param visibility: The visibility of the weather data.
    @param timestamp: The timestamp of the weather data.
    """

    temperature: float
    humidity: float
    pressure: float
    wind_speed: float
    wind_direction: float
    cloudiness: float
    visibility: float
    timestamp: datetime

    def __init__(self, temperature:float, humidity:float, pressure:float, wind_speed:float, wind_direction:float, cloudiness:float, visibility:float, timestamp:datetime):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.cloudiness = cloudiness
        self.visibility = visibility
        self.timestamp = timestamp
        
    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__);
    
    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__);
    
    def csv(self):
        return f"{self.timestamp},{self.temperature},{self.humidity},{self.pressure},{self.wind_speed},{self.wind_direction},{self.cloudiness},{self.visibility}";
    
    def xml(self):
        return f"""<weather>
            <timestamp>{self.timestamp.isoformat()}</timestamp>
            <temperature>{self.temperature}</temperature>
            <humidity>{self.humidity}</humidity>
            <pressure>{self.pressure}</pressure>
            <wind_speed>{self.wind_speed}</wind_speed>
            <wind_direction>{self.wind_direction}</wind_direction>
            <cloudiness>{self.cloudiness}</cloudiness>
            <visibility>{self.visibility}</visibility>
        </weather>
        """;
    
    @staticmethod
    def from_xml(self, xml):
        return WeatherData.from_dict(xml);     
        
        
    def json(self) -> dict:
        return json.loads(self.__str__());
    
if __name__ == "__main__":
    wd__1 = WeatherData(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, datetime.datetime.now());
    wd__2 = WeatherData(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, datetime.datetime.now());
    
    print(wd__1.csv());
    print(wd__2.csv());
    
    print(wd__1.xml());
    print(wd__2.xml());
    
    
    