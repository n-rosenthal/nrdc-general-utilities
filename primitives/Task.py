from dataclasses import dataclass;
from datetime import datetime;

@dataclass
class Task:
    name            :str;
    description     :str;
    priority        :int;
    due_date        :datetime | None;
    completed       :bool;
    
    def __str__(self):
        if(self.completed):
            return f" - [x] {self.name} - {self.description} - {self.priority} - {self.due_date}";
        else:
            return f" - [ ] {self.name} - {self.description} - {self.priority} - {self.due_date}";
        
    def __repr__(self):
        return self.__str__();

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority.name,
            "due_date": self.due_date,
            "completed": self.completed
        };
        
    @staticmethod
    def from_dict(data):
        return Task(
            data["name"],
            data["description"],
            data["priority"],
            data["due_date"],
            data["completed"]
        );
        
@dataclass
class ObsidianTask(Task):
    """A ObsidianTask is a Task engineered to work with Obsidian."""
    tags: list[str];
    
    PRIORITIES = {
        1: r"⏬️",
        2: r"🔽",
        3: r"🔼",
        4: r"⏫",
        5: r"🔺"
    };
    
    DUE:str = r"📅";
    
    def __str__(self) -> str:
        if(self.completed):
            return f" - [x] {self.PRIORITIES[self.priority]} {self.name} - {self.description} - {self.dueDate}";
        else:
            return f" - [ ] {self.PRIORITIES[self.priority]} {self.name} - {self.description} - {self.dueDate}";
        
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.dueDate,
            "completed": self.completed,
            "tags": self.tags
        };
        
    @staticmethod
    def from_dict(data):
        return ObsidianTask(
            data["name"],
            data["description"],
            data["priority"],
            data["due_date"],
            data["completed"],
            data["tags"]
        );
        
    @property
    def dueDate(self):
        return self.due_date.strftime("%Y-%m-%d") + " 📅";    
    
        
if __name__ == '__main__':
    task = Task("Task 1", "Description 1", 3, datetime.now(), False);
    print(task);
    
    obsidian_task = ObsidianTask("Task 2", "Description 2", 3, datetime.now(), False, ["#tag1", "#tag2"]);
    for ch in str(obsidian_task):
        print(ch, end="");
    