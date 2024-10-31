import datetime;
import Astral as astral;
import Planets as planets;
import Zodiacs as zodiacs;

class ReportBuilder:
    """The `ReportBuilder` superclass is the base class for all report classes.
    It provides the `generate_report` method that should be implemented by all report classes.

    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def generate_report(self):
        """Generates the report.
        
        This method should be implemented by all report classes.
        It should generate the report and return it in a format that can be used by the `ReportSender` class.
        
        @return: The generated report.
        @rtype: str
        """
        raise NotImplementedError;
    
    def getData(self) -> dict:
        """Returns the data associated with the report.
        
        This method should be implemented by all report classes.
        It should return the data associated with the report in a format that can be used by the `ReportSender` class.
        
        @return: The data associated with the report.
        @rtype: dict
        """
        raise NotImplementedError
    
    def setData(self, data:dict) -> None:
        """Sets the data associated with the report.
        
        This method should be implemented by all report classes.
        It should set the data associated with the report from the given data.
        
        @param data: The data to set.
        @type data: dict
        """
        raise NotImplementedError
    
    def addData(self, data:dict) -> None:
        """Adds data to the report.
        
        This method should be implemented by all report classes.
        It should add the given data to the report.
        
        @param data: The data to add.
        @type data: dict
        """
        raise NotImplementedError
    
    def removeData(self, data:dict) -> None:
        """Removes data from the report.
        
        This method should be implemented by all report classes.
        It should remove the given data from the report.
        
        @param data: The data to remove.
        @type data: dict
        """
        raise NotImplementedError
    
    def clearData(self) -> None:
        """Clears the data associated with the report.
        
        This method should be implemented by all report classes.
        It should clear the data associated with the report.
        """
        raise NotImplementedError;
    
    def _setWeekdayData(self, day:datetime) -> None:
        """Sets the data associated with the report for the given day of the week.
        
        This method should be implemented by all report classes.
        It should set the data associated with the report for the given day of the week.
        
        @param day_of_week: The day of the week.
        @type day_of_week: int
        """
        weekday: int = day.weekday();
        
        #   str representation
        self.data["day_of_week"]            = day;
        self.data["day_of_week_str"]        = day.strftime("%A");
        self.data["day_of_week_short_str"]  = day.strftime("%a");
        
        #   as int
        self.data["day_of_week_number"]     = weekday;
        
        #   planetary
        self.data["planet"]                 = planets.Planets.from_weekday(weekday);
        
        #   astral
        self.data["sky_position"]           = astral.SkyPosition(day, self.data["planet"]);
        
        

class PlanetaryDayReport(ReportBuilder):
    """The `PlanetaryDayReport` class is a subclass of the `ReportBuilder` class.
    It provides the `generate_report` method that generates a report about the planetary hours of the given day.
    
    It accepts as constructor parameters
        -   a `PlanetaryHours` list object of `PlanetaryHour` objects
        -   a tuple of datetime or str objects representing the sun rise and sun set times
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def generate_report(self, *args) -> str:
        #   Check if a `PlanetaryHours` list object was provided
        if len(args) == 1 and isinstance(args[0], list):
            planetary_hours = args[0];
        elif len(args) == 1 and isinstance(args[0], tuple):
            #   Check if a tuple of datetime or str objects was provided
            if  isinstance(args[0][0], str) and isinstance(args[0][1], str):
                #   Convert the str objects to datetime objects
                try:
                    args[0] = (datetime.datetime.strptime(args[0][0], "%H:%M:%S"), datetime.datetime.strptime(args[0][1], "%H:%M:%S"));
                except ValueError:
                    raise ValueError("Invalid arguments");
            
            sunrise: datetime = args[0][0];
            sunset: datetime = args[0][1];
            planetary_hours = planets.getPlanetaryHours(sunrise, sunset);
        else:
            raise ValueError("Invalid arguments");
        
        #   Day of the week
        day_str    : str = planetary_hours[0].start.strftime("%Y-%m-%d");
        day_of_week: int = planetary_hours[0].start.weekday();
        
        #   Generate the report
        report: str = "\t" + "-"*56 + "\n";
        report += f"\t\t{day_str}\t\t\t\t\t{self.data['day_of_week_str']} ({self.data["day_planet"]})\n\n";
        report += f"\t\tstart\t-\t end \t\t\tPlanetary Ruler\n" + "\t" + "-"*56 + "\n";
        for planetary_hour in planetary_hours:
            report += f"\t\t{planetary_hour.start:%I:%M} \t-\t {planetary_hour.end:%I:%M}\t\t\t{planetary_hour.planet}\n";
        report += "\t" + "-"*56 + "\n";
        return report;
        
    def __init__(self, day_of_week:datetime) -> None:
        self.data = {};
        self.day_of_week = day_of_week;
        
        self.data["day_of_week"]            = day_of_week;
        self.data["day_of_week_str"]        = day_of_week.strftime("%A");
        self.data["day_of_week_short_str"]  = day_of_week.strftime("%a");
        self.data["day_of_week_number"] = day_of_week.weekday();
        self.data["day_planet"] = planets.Planets.from_weekday(day_of_week.weekday());
        
class ZodiacalSkyReport(ReportBuilder):
    """The `ZodiacalSkyReport` class is a subclass of the `ReportBuilder` class.
    It provides the `generate_report` method that generates a report about the zodiacal sky of the given day.
    
    It accepts as constructor parameters
        -   a `ZodiacalSky` object of `PositionedPlanet` objects
    
    @author nrosenthal
    @version 1.0
    @since 2024-10-29
    """
    def generate_report(self, *args) -> str:
        #   Check if a `ZodiacalSky` object was provided
        if len(args) == 1 and isinstance(args[0], astral.ZodiacalSky):
            zodiacal_sky = args[0];
        else:
            raise ValueError("Invalid arguments");
        
        #   Day of the week
        day_str: str = zodiacal_sky.date.strftime("%Y-%m-%d");
        
        #   Generate the report
        report: str = "\t" + "-"*56 + "\n";
        report += f"\t\t{day_str}\t\t\t\t\t{self.data['day_of_week_str']} ({self.data["day_planet"]})\n\n";
        report += f"\t\tplanet\t-\t end \t\t\tPlanetary Ruler\n" + "\t" + "-"*56 + "\n";
        for zodiacal_planet in zodiacal_sky.planets:
            report += f"\t\t{zodiacal_planet.start:%I:%M} \t-\t {zodiacal_planet.end:%I:%M}\t\t\t{zodiacal_planet.planet}\n";
        report += "\t" + "-"*56 + "\n";
        return report;
    
    def __init__(self, day: datetime) -> None:
        self.data = {};
        self.day = day;
        
        self.data["day_of_week"]            = day;
        self.data["day_of_week_str"]        = day.strftime("%A");
        self.data["day_of_week_short_str"]  = day.strftime("%a");
        self.data["day_of_week_number"]     = day.weekday();

    
    
if __name__ == "__main__":
    print(PlanetaryDayReport(datetime.datetime(2024, 10, 30)).generate_report((datetime.datetime(2024,10,30,6,0,0), datetime.datetime(2024,10,30,18,0,0))));