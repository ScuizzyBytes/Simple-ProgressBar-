import customtkinter as ctk
import psutil
import threading

class CPUUsageMonitor:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("CPU Usage Monitor")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.cpu_label = ctk.CTkLabel(self.root, text="CPU Usage: 0%")
        self.ProgressBar = ctk.CTkProgressBar(self.root, width=200)
        self.gpu_label = ctk.CTkLabel(self.root, text="GPU Usage: 0%")
        self.gpu_progress = ctk.CTkProgressBar(self.root, width=200)
        self.ProgressBar.grid(row=1, column=0, padx=10, pady=10)
        self.cpu_label.grid(row=0, column=0, padx=10, pady=10)
        self.gpu_label.grid(row=2, column=0, padx=10, pady=10)
        self.gpu_progress.grid(row=3, column=0, padx=10, pady=10)
        self.root.attributes('-alpha', 0.9)

        threading.Thread(target=self.update_cpu_usage, daemon=True).start()

    def update_cpu_usage(self):
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            gpu_usage = psutil.virtual_memory().percent

            self.cpu_label.configure(text=f"CPU Usage: {cpu_usage}%")
            self.ProgressBar.set(cpu_usage / 100)
            self.gpu_label.configure(text=f"GPU Usage: {gpu_usage}%")
            self.gpu_progress.set(gpu_usage / 100)

            if cpu_usage > 80 and gpu_usage > 80:
                self.ProgressBar.configure(progress_color="red")
                self.gpu_progress.configure(progress_color="red")
            else:
                self.ProgressBar.configure(progress_color="green")
                self.gpu_progress.configure(progress_color="green")

root = CPUUsageMonitor()
root.root.mainloop()


    
