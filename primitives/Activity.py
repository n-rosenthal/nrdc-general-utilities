from Storable import Storable;

class Activity(Storable):
    def __init__(self, name:str, description:str, timestamps:tuple):
        """
        Creates a new Activity.

        Args:
            name (str): The name of the Activity.
            description (str): A description of the Activity.
            timestamps (tuple): A tuple of two strings representing the start and end times of the Activity in the format %Y-%m-%d %H:%M.
        """
        self.name = name;
        self.description = description;
        self.timestamps = timestamps;
        
    def __str__(self):
        return f" - {self.name} - {self.description} - {self.timestamps[0]} - {self.timestamps[1]}";
    
    def __repr__(self):
        return f"Activity({self.name}, {self.description}, {self.timestamps})";
    
    def xml(self):
        return f"<activity><name>{self.name}</name><description>{self.description}</description><timestamps><beginning>{self.timestamps[0]}</beginning><end>{self.timestamps[1]}</end></timestamps></activity>";
    
    def csv(self):
        return f"\"{self.name}\", \"{self.description}\", \"{self.timestamps[0]}\", \"{self.timestamps[1]}\"";

    def json(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "timestamps": self.timestamps
        };


        return [activity.json() for activity in self.activities];
    
    
class ActivityList(Storable):
    """A list of Activity objects."""
    def __init__(self, activities:list):
        """
        Creates a new ActivityList.

        Args:
            activities (list): A list of Activity objects.
        """
        self.activities = activities;
        
    def __str__(self):
        """
        Returns a string representation of the ActivityList, with each activity on a line, as returned by Activity.__str__.
        """
        return "\n".join([str(activity) for activity in self.activities]);
    
    def __repr__(self):
        return f"ActivityList({self.activities})";
    
    def xml(self):
        return "\n".join([activity.xml() for activity in self.activities]);
    
    def csv(self):
        return "\n".join([activity.csv() for activity in self.activities]);

if __name__ == '__main__':
    activity = Activity("Activity 1", "Description 1", ("2022-01-01 00:00", "2022-01-01 01:00"));
    activity_2 = Activity("Activity 2", "Description 2", ("2022-01-01 01:00", "2022-01-01 02:00"));
    activity_3 = Activity("Activity 3", "Description 3", ("2022-01-01 02:00", "2022-01-01 03:00"));
    
    activity_list = ActivityList([activity, activity_2, activity_3]);
    print(activity_list.xml());
    