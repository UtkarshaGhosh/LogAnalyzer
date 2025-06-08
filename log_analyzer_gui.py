import tkinter as tk
from tkinter import messagebox
import daily_log_updater

def run_analysis():
    try:
        daily_log_updater.main()
        messagebox.showinfo("Success", "Log analysis completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("System Log Analyzer")
root.geometry("300x150")

tk.Label(root, text="Log Analyzer").pack(pady=10)
tk.Button(root, text="Run Analysis", command=run_analysis).pack(pady=20)

root.mainloop()
