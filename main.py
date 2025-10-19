import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        self.tasks = []
        
        # Создание элементов интерфейса
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        
        self.listbox = tk.Listbox(
            self.frame,
            width=50,
            height=15,
            selectmode=tk.SINGLE
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Поле ввода
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)
        
        # Кнопки
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Добавить", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Удалить", command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Выполнено", command=self.complete_task).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Выйти", command=root.quit).grid(row=0, column=3, padx=5)
    
    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
    
    def delete_task(self):
        try:
            selected = self.listbox.curselection()[0]
            self.tasks.pop(selected)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Предупреждение", "Выберите задачу для удаления")
    
    def complete_task(self):
        try:
            selected = self.listbox.curselection()[0]
            self.tasks[selected]["completed"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Предупреждение", "Выберите задачу")
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.listbox.insert(tk.END, f"[{status}] {task['task']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
