from primitives.Task import Task;

class TaskManager:
    __slots__ = ['tasks'];
    
    def __init__(self):
        self.tasks = [];
        
    def add_task(self, task:Task):
        self.tasks.append(task);
        self.tasks.sort(key=lambda x: x.priority);
        
    def remove_task(self, task:Task):
        self.tasks.remove(task);
        
    def complete_task(self, task:Task):
        task.completed = True;
        
    def uncomplete_task(self, task:Task):
        task.completed = False;
        
    def get_tasks(self):
        return self.tasks;
    
    def get_task(self, name:str):
        for task in self.tasks:
            if(task.name == name):
                return task;
        return None;
    
    def to_dict(self):
        return {
            "tasks": [task.to_dict() for task in self.tasks]
        };
        
    @staticmethod
    def from_dict(data):
        task_manager = TaskManager();
        for task_data in data["tasks"]:
            task_manager.add_task(Task.from_dict(task_data));
        return task_manager;
    
    def __str__(self):
        return "\n".join([str(task) for task in self.tasks]);
    
    def __repr__(self):
        return self.__str__();
    
    def __len__(self):
        return len(self.tasks);
    
    def __getitem__(self, index):
        return self.tasks[index];
    
    def __iter__(self):
        return iter(self.tasks);
    
    def __contains__(self, task:Task):
        return task in self.tasks;
    