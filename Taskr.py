"""Taskr is a interface for the `TaskManager` class. It provides a simple way to interact with the `TaskManager` class.	"""

from primitives.Task import ObsidianTask;
from TaskManager import TaskManager;
from datetime import datetime;
from enum import Enum;
from os import listdir;
from os.path import isfile, join;
from typing import List;
import json;
import os;
import shutil;

import logging;
import sys;
import traceback;

class TaskrStatus(Enum):
    """TaskrStatus is a enum that represents the status of the Taskr class."""
    SUCCESS = 1;
    FAILURE = 2;
    WARNING = 3;

class Taskr:
    DEFAULT_TASKR_DIRECTORY:str = ".taskr";
    DEFAULT_TASKR_TASKFILE:str = "tasks.json";
    
    def __init__(self) -> None:
        """Creates a new Taskr object."""
        pass;
    
    def __chkFiles(self) -> TaskrStatus:
        """Checks if the Taskr directory and Taskr task file exists.

        Returns:
            TaskrStatus:        SUCCESS if the directory and file exists, FAILURE otherwise.
        """
        if(os.path.exists(Taskr.DEFAULT_TASKR_DIRECTORY) and os.path.exists(os.path.join(Taskr.DEFAULT_TASKR_DIRECTORY, Taskr.DEFAULT_TASKR_TASKFILE))):
            return TaskrStatus.SUCCESS;
        return TaskrStatus.FAILURE;
    
    def __createTaskrDirectory(self) -> TaskrStatus:
        """Creates the Taskr directory.

        Returns:
            TaskrStatus:        SUCCESS if the directory was created, FAILURE otherwise.
        """
        try:
            os.mkdir(Taskr.DEFAULT_TASKR_DIRECTORY);
            return TaskrStatus.SUCCESS;
        except Exception as e:
            logging.error(f"Error creating Taskr directory: {e}");
            return TaskrStatus.FAILURE;
        
    def __createTaskrTaskFile(self) -> TaskrStatus:
        """Creates the Taskr task file.

        Returns:
            TaskrStatus:        SUCCESS if the file was created, FAILURE otherwise.
        """
        try:
            with open(os.path.join(Taskr.DEFAULT_TASKR_DIRECTORY, Taskr.DEFAULT_TASKR_TASKFILE), "w") as f:
                f.write(json.dumps(TaskManager().to_dict()));
            return TaskrStatus.SUCCESS;
        except Exception as e:
            logging.error(f"Error creating Taskr task file: {e}");
            return TaskrStatus.FAILURE;

    def __loadTaskrTaskFile(self) -> TaskManager:
        """Loads the Taskr task file.

        Returns:
            TaskManager:        The TaskManager object loaded from the Taskr task file.
        """
        try:
            with open(os.path.join(Taskr.DEFAULT_TASKR_DIRECTORY, Taskr.DEFAULT_TASKR_TASKFILE), "r") as f:
                return TaskManager.from_dict(json.loads(f.read()));
        except Exception as e:
            logging.error(f"Error loading Taskr task file: {e}");
            return TaskManager();

    def __saveTaskrTaskFile(self, task_manager:TaskManager) -> TaskrStatus:
        """Saves the Taskr task file.

        Args:
            task_manager (TaskManager): The TaskManager object to save.

        Returns:
            TaskrStatus:        SUCCESS if the file was saved, FAILURE otherwise.
        """
        try:
            with open(os.path.join(Taskr.DEFAULT_TASKR_DIRECTORY, Taskr.DEFAULT_TASKR_TASKFILE), "w") as f:
                f.write(json.dumps(task_manager.to_dict()));
            return TaskrStatus.SUCCESS;
        except Exception as e:
            logging.error(f"Error saving Taskr task file: {e}");
            return TaskrStatus.FAILURE;
        
    def add_task(self, task:ObsidianTask) -> TaskrStatus:
        """Adds a task to the Taskr task file.

        Args:
            task (ObsidianTask): The task to add.

        Returns:
            TaskrStatus:        SUCCESS if the task was added, FAILURE otherwise.
        """
        try:
            status = self.__chkFiles();
            if(status == TaskrStatus.FAILURE):
                status = self.__createTaskrDirectory();
                if(status == TaskrStatus.SUCCESS):
                    status = self.__createTaskrTaskFile();
            if(status == TaskrStatus.SUCCESS):
                task_manager = self.__loadTaskrTaskFile();
                task_manager.add_task(task);
                status = self.__saveTaskrTaskFile(task_manager);
            return status;
        except Exception as e:
            logging.error(f"Error adding task: {e}");
            return TaskrStatus.FAILURE;
        
    def remove_task(self, task:ObsidianTask) -> TaskrStatus:
        """Removes a task from the Taskr task file.

        Args:
            task (ObsidianTask): The task to remove.

        Returns:
            TaskrStatus:        SUCCESS if the task was removed, FAILURE otherwise.
        """
        try:
            status = self.__chkFiles();
            if(status == TaskrStatus.FAILURE):
                status = self.__createTaskrDirectory();
                if(status == TaskrStatus.SUCCESS):
                    status = self.__createTaskrTaskFile();
            if(status == TaskrStatus.SUCCESS):
                task_manager = self.__loadTaskrTaskFile();
                task_manager.remove_task(task);
                status = self.__saveTaskrTaskFile(task_manager);
            return status;
        except Exception as e:
            logging.error(f"Error removing task: {e}");
            return TaskrStatus.FAILURE;
        
    def complete_task(self, task:ObsidianTask) -> TaskrStatus:
        """Completes a task in the Taskr task file.

        Args:
            task (ObsidianTask): The task to complete.

        Returns:
            TaskrStatus:        SUCCESS if the task was completed, FAILURE otherwise.
        """
        try:
            status = self.__chkFiles();
            if(status == TaskrStatus.FAILURE):
                status = self.__createTaskrDirectory();
                if(status == TaskrStatus.SUCCESS):
                    status = self.__createTaskrTaskFile();
            if(status == TaskrStatus.SUCCESS):
                task_manager = self.__loadTaskrTaskFile();
                task_manager.complete_task(task);
                status = self.__saveTaskrTaskFile(task_manager);
            return status;
        except Exception as e:
            logging.error(f"Error completing task: {e}");
            return TaskrStatus.FAILURE;
        
    def uncomplete_task(self, task:ObsidianTask) -> TaskrStatus:
        """Uncompletes a task in the Taskr task file.

        Args:
            task (ObsidianTask): The task to uncomplete.

        Returns:
            TaskrStatus:        SUCCESS if the task was uncompleted, FAILURE otherwise.
        """
        try:
            status = self.__chkFiles();
            if(status == TaskrStatus.FAILURE):
                status = self.__createTaskrDirectory();
                if(status == TaskrStatus.SUCCESS):
                    status = self.__createTaskrTaskFile();
            if(status == TaskrStatus.SUCCESS):
                task_manager = self.__loadTaskrTaskFile();
                task_manager.uncomplete_task(task);
                status = self.__saveTaskrTaskFile(task_manager);
            return status;
        except Exception as e:
            logging.error(f"Error uncompleting task: {e}");
            return TaskrStatus.FAILURE;
    
    def getAllTasks(self) -> List[ObsidianTask]:
        """Gets all tasks from the Taskr task file.

        Returns:
            List[ObsidianTask]:        A list of all tasks.
        """
        try:
            status = self.__chkFiles();
            if(status == TaskrStatus.FAILURE):
                status = self.__createTaskrDirectory();
                if(status == TaskrStatus.SUCCESS):
                    status = self.__createTaskrTaskFile();
            if(status == TaskrStatus.SUCCESS):
                task_manager = self.__loadTaskrTaskFile();
                return task_manager.get_tasks();
            return [];
        except Exception as e:
            logging.error(f"Error getting all tasks: {e}");
            return [];
        
class App:
    def __init__(self):
        self.interface = Taskr();

    def present(self):
        print("Welcome to Taskr! Please choose an option:");
        print("1. Add Task");
        print("2. Remove Task");
        print("3. Complete Task");
        print("4. Uncomplete Task");
        print("5. Get All Tasks");
        print("6. Exit");
        
    def select(self):
        return input("Option: ");
    
    def add_task(self):
        name = input("Name: ");
        description = input("Description: ");
        priority = int(input("Priority: "));
        due_date = datetime.strptime(input("Due Date (YYYY-MM-DD): "), "%Y-%m-%d");
        completed = False;
        tags = input("Tags (separated by comma): ").split(",");
        task = ObsidianTask(name, description, priority, due_date, completed, tags);
        status = self.interface.add_task(task);
        if(status == TaskrStatus.SUCCESS):
            print("Task added successfully!");
        else:
            print("Error adding task!");
            
    def remove_task(self):
        name = input("Name: ");
        task = self.interface.get_task(name);
        if(task != None):
            status = self.interface.remove_task(task);
            if(status == TaskrStatus.SUCCESS):
                print("Task removed successfully!");
            else:
                print("Error removing task!");
        else:
            print("Task not found!");
            
    def complete_task(self):
        name = input("Name: ");
        task = self.interface.get_task(name);
        if(task != None):
            status = self.interface.complete_task(task);
            if(status == TaskrStatus.SUCCESS):
                print("Task completed successfully!");
            else:
                print("Error completing task!");
        else:
            print("Task not found!");
            
    def uncomplete_task(self):
        name = input("Name: ");
        task = self.interface.get_task(name);
        if(task != None):
            status = self.interface.uncomplete_task(task);
            if(status == TaskrStatus.SUCCESS):
                print("Task uncompleted successfully!");
            else:
                print("Error uncompleting task!");
        else:
            print("Task not found!");
            
    def get_all_tasks(self):
        tasks = self.interface.getAllTasks();
        if(len(tasks) > 0):
            for task in tasks:
                print(task);
        else:
            print("No tasks found!");
            
    def run(self):
        while True:
            self.present();
            option = self.select();
            if(option == "1"):
                self.add_task();
            elif(option == "2"):
                self.remove_task();
            elif(option == "3"):
                self.complete_task();
            elif(option == "4"):
                self.uncomplete_task();
            elif(option == "5"):
                self.get_all_tasks();
            elif(option == "6"):
                break;
            else:
                print("Invalid option!");
    
        
if __name__ == '__main__':
    App().run();
    
    a = TaskManager();