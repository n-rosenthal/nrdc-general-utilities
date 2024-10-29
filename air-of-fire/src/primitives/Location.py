""" `location.py`
    Module for defining the `Location` class, its subclasses (...) and specific functions over `Location` objects.
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-28
"""

from dataclasses import dataclass;
from zoneinfo import ZoneInfo;

@dataclass
class Location:
    """A `Location` is a dataclass for storing information about a geographical location.
    It includes obligatory fields `latitude` and `longitude`, as well as an optional `timezone`.
    
    @param latitude: The latitude of the `Location`.
    @param longitude: The longitude of the `Location`.
    @param timezone: The timezone of the `Location`, or `None` if not specified.
    """
    latitude: float;
    longitude: float;
    timezone: ZoneInfo | None;
    
    
    #   Consistency checking methods
    def _checkParams(self, latitude, longitude, timezone) -> None:
        if(latitude == None or longitude == None):
            raise ValueError("Both latitude and longitude must be specified");
        if(type(latitude) != float or type(longitude) != float):
            raise ValueError("Latitude and longitude must be of type float");
        if(type(timezone) != ZoneInfo and timezone != None):
            raise ValueError("Timezone must be of type ZoneInfo or None");
        if(latitude < -90 or latitude > 90):
            raise ValueError("Latitude out of range");
        if(longitude < -180 or longitude > 180):
            raise ValueError("Longitude out of range");
    
    
    def __init__(self, latitude:float , longitude:float, timezone:ZoneInfo | None=None):
        """Initializes a `Location` object with the given `latitude` and `longitude`, and an optional `timezone`.
        
        @param latitude: The latitude of the `Location`.
        @param longitude: The longitude of the `Location`.
        @param timezone: The timezone of the `Location`, or `None` if not specified.
        """
        #   Consistency checking
        try:
            self._checkParams(latitude, longitude, timezone);
        except ValueError as e:
            print(e);
            return;
        
        #   Initialization
        self.latitude = latitude;
        self.longitude = longitude;
        self.timezone = timezone;

            
    def __str__(self):
        if(self.timezone != None):
            return f"Location[lat={self.latitude}, long={self.longitude}, tz='{self.timezone}']";
        else:
            return f"Location[lat={self.latitude}, long={self.longitude}]";
        

    def __repr__(self):
        return self.__str__();
    
    
    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timezone": self.timezone
        };
        

    @staticmethod
    def from_dict(data):
        return Location(
            data["latitude"],
            data["longitude"],
            data["timezone"]
        );
        
    @classmethod
    def from_json(cls, data):
        return cls.from_dict(data);
    
    @classmethod
    def from_xml(cls, data):
        return cls.from_dict(data);
    
    @classmethod
    def from_csv(cls, data):
        return cls.from_dict(data);
    
    def to_csv(self):
        return f"{self.latitude},{self.longitude},{self.timezone}";

@dataclass
class GeoLocation(Location):    
    """A `GeoLocation` is a subclass of `Location` that includes additional fields for geolocation information.
    
    @param latitude: The latitude of the `Location`.
    @param longitude: The longitude of the `Location`.
    @param timezone: The timezone of the `Location`, or `None` if not specified.
    @param altitude: The altitude of the `Location`, or `None` if not specified.
    @param accuracy: The accuracy of the `Location`, or `None` if not specified.
    """
    def _checkParams(self, latitude, longitude, timezone, altitude=None, accuracy=None) -> None:
        #   Checks latitude, longitude, and timezone
        """Checks the parameters of the `GeoLocation` object.
        
        Args:
            latitude (float): The latitude of the `Location`.
            longitude (float): The longitude of the `Location`.
            timezone (ZoneInfo | None): The timezone of the `Location`, or `None` if not specified.
        
        Raises:
            ValueError: If the parameters are invalid.
        """
        super()._checkParams(latitude, longitude, timezone);
    
        #   Checks altitude and accuracy
        if(type(altitude) != float and altitude != None):
            raise ValueError("Altitude must be of type float or None");
        if(type(accuracy) != float and accuracy != None):
            raise ValueError("Accuracy must be of type float or None");
    
    def __init__(self, latitude:float , longitude:float, timezone:ZoneInfo | None=None, altitude:float | None=None, accuracy:float | None=None):
        """Initializes a `GeoLocation` object with the given `latitude` and `longitude`, and an optional `timezone`, `altitude`, and `accuracy`.
        
        @param latitude: The latitude of the `Location`.
        @param longitude: The longitude of the `Location`.
        @param timezone: The timezone of the `Location`, or `None` if not specified.
        @param altitude: The altitude of the `Location`, or `None` if not specified.
        @param accuracy: The accuracy of the `Location`, or `None` if not specified.
        """
        super().__init__(latitude, longitude, timezone);
        self._checkParams(latitude, longitude, timezone, altitude, accuracy);
        self.altitude = altitude;
        self.accuracy = accuracy;
    
    def __str__(self):
        try:
            return super().__str__() + f"[Geo][alt={self.altitude}, acc={self.accuracy}]";
        except ValueError as e:
            print(e);
            return "";
        
    def __repr__(self):
        return self.__str__();
    
    def to_dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timezone": self.timezone,
            "altitude": self.altitude,
            "accuracy": self.accuracy
        };
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["latitude"],
            data["longitude"],
            data["timezone"],
            data["altitude"],
            data["accuracy"]
        );
        
    @classmethod
    def from_json(cls, data):
        return cls.from_dict(data);
    
    @classmethod
    def from_xml(cls, data):
        return cls.from_dict(data);
    
    @classmethod
    def from_csv(cls, data):
        return cls.from_dict(data);
    
    def to_csv(self):
        return f"{self.latitude},{self.longitude},{self.timezone},{self.altitude},{self.accuracy}";
    
    def to_json(self):
        return self.to_dict();

@dataclass
class CityData:
    city:       str;
    region:     str;
    country:    str;
    location:   Location | None;
    
    def __str__(self):
        return f"CityData[city={self.city}, region={self.region}, country={self.country}, location={self.location}]";
    
    def __repr__(self):
        return self.__str__();
    
    def to_dict(self):
        return {
            "city": self.city,
            "region": self.region,
            "country": self.country,
            "location": self.location
        };
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["city"],
            data["region"],
            data["country"],
            data["location"]
        );
        
    @classmethod
    def from_json(cls, data):
        return cls.from_dict(data);
    
    @classmethod
    def from_xml(cls, data):
        return cls.from_dict(data);
    
    @classmethod
    def from_csv(cls, data):
        return cls.from_dict(data);
    
    def to_csv(self):
        return f"{self.city},{self.region},{self.country},{self.location.to_csv()}";
    
    def to_json(self):
        return self.to_dict();

if __name__ == "__main__":
    print(Location(0., 0., ZoneInfo("America/Sao_Paulo")).__str__());
    print(Location(0., 0., None).__str__());
    print(Location(0., 0.).__str__())
    
    print(GeoLocation(0., 0., ZoneInfo("America/Sao_Paulo"), 900., 0.78).__str__());
    print(GeoLocation(0., 0., None).__str__());
    print(GeoLocation(0., 0.).__str__())
    
    SP = (CityData("São Paulo", "São Paulo", "Brazil", GeoLocation(0., 0., ZoneInfo("America/Sao_Paulo"))));
    print(SP);
    print(SP.to_csv());