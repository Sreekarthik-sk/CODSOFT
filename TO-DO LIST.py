import tkinter as tk
from tkinter import messagebox
import os
TASK_FILE = 'tasks.txt'
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            for line in file:
                task, completed = line.strip().split(' | ')
                tasks.append({'task': task, 'completed': completed == 'True'})
    return tasks
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['completed']}\n")
def update_task_listbox():
    listbox_tasks.delete(0, tk.END)  # Clear the listbox
    for idx, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        listbox_tasks.insert(tk.END, f"{idx + 1}. [{status}] {task['task']}")
def add_task():
    task_description = entry_task.get()
    if task_description:
        tasks.append({'task': task_description, 'completed': False})
        entry_task.delete(0, tk.END)  
        update_task_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty.")
def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        tasks[task_index]['completed'] = True
        update_task_listbox()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")
def remove_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        tasks.pop(task_index)
        update_task_listbox()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")
app = tk.Tk()
app.title("To-Do List Application")
tasks = load_tasks()
label_task = tk.Label(app, text="Enter task:")
label_task.pack(pady=10)
entry_task = tk.Entry(app, width=40)
entry_task.pack(pady=10)
button_add = tk.Button(app, text="Add Task", width=20, command=add_task)
button_add.pack(pady=10)
button_complete = tk.Button(app, text="Complete Task", width=20, command=complete_task)
button_complete.pack(pady=10)
button_remove = tk.Button(app, text="Remove Task", width=20, command=remove_task)
button_remove.pack(pady=10)
listbox_tasks = tk.Listbox(app, height=10, width=50)
listbox_tasks.pack(pady=10)
update_task_listbox()
app.mainloop()
