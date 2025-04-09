import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("400x500")
        self.root.configure(bg="#f9f9f9")

        self.tasks = []

        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(self.root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f9f9f9", fg="#333")
        title.pack(pady=10)

        self.task_entry = ttk.Entry(self.root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, padx=20, fill='x')

        add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        # Frame for tasks + scrollbar
        task_frame = tk.Frame(self.root, bg="#ffffff", bd=1, relief="sunken")
        task_frame.pack(pady=10, padx=20, fill="both", expand=True)

        canvas = tk.Canvas(task_frame, bg="#ffffff")
        scrollbar = ttk.Scrollbar(task_frame, orient="vertical", command=canvas.yview)
        self.task_list_frame = tk.Frame(canvas, bg="#ffffff")

        self.task_list_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.task_list_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        clear_button = ttk.Button(self.root, text="Clear Completed", command=self.clear_completed)
        clear_button.pack(pady=5)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
            return

        var = tk.BooleanVar()
        task_check = tk.Checkbutton(self.task_list_frame, text=task_text, variable=var,
                                    font=("Helvetica", 12), bg="#ffffff", anchor="w")
        task_check.config(command=lambda v=var, cb=task_check: self.toggle_task(v, cb))
        task_check.pack(fill="x", padx=5, pady=2)

        self.tasks.append((var, task_check))
        self.task_entry.delete(0, tk.END)

    def toggle_task(self, var, checkbox):
        if var.get():
            checkbox.config(fg="gray", font=("Helvetica", 12, "overstrike"))
        else:
            checkbox.config(fg="black", font=("Helvetica", 12))

    def clear_completed(self):
        for var, checkbox in self.tasks[:]:
            if var.get():
                checkbox.destroy()
                self.tasks.remove((var, checkbox))

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
