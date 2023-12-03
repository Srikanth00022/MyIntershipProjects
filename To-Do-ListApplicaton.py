#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False  # Default value is False

    def mark_as_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_task_from_input(self):
        description = input("Enter task description: ")
        due_date = input("Enter due date (optional): ")
        priority = input("Enter priority (optional): ")

        new_task = Task(description, due_date, priority)
        self.add_task(new_task)
        print("Task added successfully!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{index}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Status: {status}")

    def mark_task_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            completed_task.mark_as_completed()
            self.completed_tasks.append(completed_task)
            print("Task marked as completed and moved to the completed tasks list.")
        else:
            print("Invalid task index. Please enter a valid task index.")

    def display_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks.")
        else:
            print("Completed Tasks:")
            for index, task in enumerate(self.completed_tasks, start=1):
                print(f"{index}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")

    def update_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task_to_update = self.tasks[task_index - 1]

            new_description = input(f"Enter new description for task '{task_to_update.description}': ")
            new_due_date = input(f"Enter new due date for task '{task_to_update.description}' (optional): ")
            new_priority = input(f"Enter new priority for task '{task_to_update.description}' (optional): ")

            # Update task attributes if user provided new values
            if new_description:
                task_to_update.description = new_description
            if new_due_date:
                task_to_update.due_date = new_due_date
            if new_priority:
                task_to_update.priority = new_priority

            print("Task updated successfully!")
        else:
            print("Invalid task index. Please enter a valid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task.description}' removed from the to-do list.")
        else:
            print("Invalid task index. Please enter a valid task index.")

# Example Usage:
todo_list = ToDoList()

# Adding tasks
task1 = Task("Complete To-Do App", "2023-12-05", "High")
task2 = Task("Prepare for Interview", "2023-12-07", "Medium")

todo_list.add_task(task1)
todo_list.add_task(task2)

# Displaying tasks
todo_list.display_tasks()

# Adding a new task from user input
todo_list.add_task_from_input()

# Displaying tasks after adding a new task
todo_list.display_tasks()

# Marking the first task as completed
todo_list.mark_task_as_completed(1)

# Displaying completed tasks
todo_list.display_completed_tasks()

# Updating the second task
todo_list.update_task(2)

# Displaying tasks after updating
todo_list.display_tasks()

# Removing the third task
todo_list.remove_task(3)

# Displaying tasks after removing
todo_list.display_tasks()


# In[ ]:




