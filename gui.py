# import tkinter as tk
# from tkinter import filedialog, messagebox
# from tkinter import ttk
# from tkinter.font import Font


# class RoundedButton(tk.Canvas):
#     def __init__(
#         self, parent, text, command=None, radius=20, padding=(10, 10), *args, **kwargs
#     ):
#         tk.Canvas.__init__(self, parent, *args, **kwargs)
#         self.radius = radius
#         self.command = command
#         self.padding = padding
#         self.text = text

#         # Calculate the required width and height based on text length and padding
#         font = Font(size=14)
#         text_width = font.measure(text)
#         self.width = text_width + 2 * (radius + padding[0])
#         self.height = 2 * (radius + padding[1] + font.metrics("ascent"))
#         self.config(
#             width=self.width,
#             height=self.height,
#             bg=parent.cget("bg"),
#             highlightthickness=0,
#         )

#         # Draw rounded rectangle
#         self.round_rect = self.create_rounded_rect(
#             0, 0, self.width, self.height, radius=self.radius
#         )
#         self.text_item = self.create_text(
#             self.width / 2, self.height / 2, text=text, font=font, fill="#FFFFFF"
#         )

#         self.bind("<ButtonPress-1>", self._on_press)
#         self.bind("<ButtonRelease-1>", self._on_release)

#     def create_rounded_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
#         points = [
#             x1 + radius,
#             y1,
#             x1 + radius,
#             y1,
#             x2 - radius,
#             y1,
#             x2 - radius,
#             y1,
#             x2,
#             y1,
#             x2,
#             y1 + radius,
#             x2,
#             y1 + radius,
#             x2,
#             y2 - radius,
#             x2,
#             y2 - radius,
#             x2,
#             y2,
#             x2 - radius,
#             y2,
#             x2 - radius,
#             y2,
#             x1 + radius,
#             y2,
#             x1 + radius,
#             y2,
#             x1,
#             y2,
#             x1,
#             y2 - radius,
#             x1,
#             y2 - radius,
#             x1,
#             y1 + radius,
#             x1,
#             y1 + radius,
#             x1,
#             y1,
#         ]

#         return self.create_polygon(
#             points, smooth=True, **kwargs, outline="#000000", fill="#000000"
#         )

#     def _on_press(self, event):
#         self.itemconfig(self.round_rect, fill="#333333")

#     def _on_release(self, event):
#         self.itemconfig(self.round_rect, fill="#000000")
#         if self.command:
#             self.command()


# class OrigamiApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Origami Design Uploader")
#         self.root.geometry("600x700")  # Increased height further
#         self.root.configure(bg="#FFFFFF")

#         self.uploaded_file = None
#         self.download_location = None

#         self.create_widgets()

#     def create_widgets(self):
#         # Main Frame
#         main_frame = tk.Frame(self.root, bg="#FFFFFF")
#         main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

#         # Title label
#         title_label = ttk.Label(
#             main_frame,
#             text="Upload Your Origami Design",
#             font=("Helvetica", 14),
#             background="#FFFFFF",
#         )
#         title_label.pack(pady=20)

#         # Upload button
#         upload_button = RoundedButton(
#             main_frame,
#             text="Upload JSON File",
#             command=self.upload_file,
#             radius=15,
#         )
#         upload_button.pack(pady=20)

#         # Display selected file path
#         self.file_label = ttk.Label(
#             main_frame, text="No file selected", font=("Helvetica", 12), background="#FFFFFF"
#         )
#         self.file_label.pack(pady=10)

#         # Download location button
#         download_button = RoundedButton(
#             main_frame,
#             text="Select Download Location",
#             command=self.select_download_location,
#             radius=15,
#         )
#         download_button.pack(pady=20)

#         # Display selected download path
#         self.download_label = ttk.Label(
#             main_frame, text="No location selected", font=("Helvetica", 12), background="#FFFFFF"
#         )
#         self.download_label.pack(pady=10)

#         # Spacer
#         tk.Frame(main_frame, height=20, bg="#FFFFFF").pack()

#         # Run button (always visible)
#         self.run_button = tk.Button(
#             main_frame,
#             text="Run",
#             command=self.run_process,
#             bg="lightblue",
#             fg="black",
#             font=("Helvetica", 12, "bold"),
#             padx=30,
#             pady=15,
#         )
#         self.run_button.pack(pady=30)
#         self.run_button.config(state='disabled')  # Initially disabled

#     def upload_file(self):
#         file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
#         if file_path:
#             self.uploaded_file = file_path
#             self.file_label.config(text=f"Selected File: {file_path}")
#             self.check_run_button_state()

#     def select_download_location(self):
#         download_path = filedialog.askdirectory()
#         if download_path:
#             self.download_location = download_path
#             self.download_label.config(text=f"Download Location: {download_path}")
#             self.check_run_button_state()

#     def check_run_button_state(self):
#         if self.uploaded_file and self.download_location:
#             self.run_button.config(state='normal')
#         else:
#             self.run_button.config(state='disabled')

#     def run_process(self):
#         messagebox.showinfo("Process Started", f"Running the process...\n\nFile: {self.uploaded_file}\nDownload Location: {self.download_location}")
#         # Add your actual processing logic here

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = OrigamiApp(root)
#     root.mainloop()


import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.font import Font
import subprocess
import re
import os
import shutil
from multiprocessing import Pool
import itertools
import time
import random
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.font import Font
import os
import itertools
import time
import random
from multiprocessing import Pool, cpu_count
import subprocess
import re
import shutil
import threading


class RoundedButton(tk.Canvas):
    def __init__(
        self, parent, text, command=None, radius=20, padding=(10, 10), *args, **kwargs
    ):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.radius = radius
        self.command = command
        self.padding = padding
        self.text = text

        # Calculate the required width and height based on text length and padding
        font = Font(size=14)
        text_width = font.measure(text)
        self.width = text_width + 2 * (radius + padding[0])
        self.height = 2 * (radius + padding[1] + font.metrics("ascent"))
        self.config(
            width=self.width,
            height=self.height,
            bg=parent.cget("bg"),
            highlightthickness=0,
        )

        # Draw rounded rectangle
        self.round_rect = self.create_rounded_rect(
            0, 0, self.width, self.height, radius=self.radius
        )
        self.text_item = self.create_text(
            self.width / 2, self.height / 2, text=text, font=font, fill="#FFFFFF"
        )

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def create_rounded_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius,
            y1,
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]

        return self.create_polygon(
            points, smooth=True, **kwargs, outline="#000000", fill="#000000"
        )

    def _on_press(self, event):
        self.itemconfig(self.round_rect, fill="#333333")

    def _on_release(self, event):
        self.itemconfig(self.round_rect, fill="#000000")
        if self.command:
            self.command()


class OrigamiApp:
    def __init__(self, root):
        self.root = root

        self.picture = "Logo.png"
        self.root.title("Origami Design Uploader")

        self.root.geometry("600x700")
        self.root.configure(bg="#FFFFFF")

        self.uploaded_file = None
        self.download_location = None

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#FFFFFF")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        title_label = ttk.Label(
            main_frame,
            text="Upload Your Origami Design",
            font=("Helvetica", 14),
            background="#FFFFFF",
        )
        title_label.pack(pady=20)

        upload_button = RoundedButton(
            main_frame, text="Upload JSON File", command=self.upload_file, radius=15
        )
        upload_button.pack(pady=20)

        self.file_label = ttk.Label(
            main_frame,
            text="No file selected",
            font=("Helvetica", 12),
            background="#FFFFFF",
        )
        self.file_label.pack(pady=10)

        download_button = RoundedButton(
            main_frame,
            text="Select Download Location",
            command=self.select_download_location,
            radius=15,
        )
        download_button.pack(pady=20)

        self.download_label = ttk.Label(
            main_frame,
            text="No location selected",
            font=("Helvetica", 12),
            background="#FFFFFF",
        )
        self.download_label.pack(pady=10)

        tk.Frame(main_frame, height=20, bg="#FFFFFF").pack()

        self.run_button = tk.Button(
            main_frame,
            text="Run",
            command=self.run_process,
            bg="lightblue",
            fg="black",
            font=("Helvetica", 12, "bold"),
            padx=30,
            pady=15,
        )
        self.run_button.pack(pady=30)
        self.run_button.config(state="disabled")

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.uploaded_file = file_path
            self.file_label.config(text=f"Selected File: {os.path.basename(file_path)}")
            self.check_run_button_state()

    def select_download_location(self):
        download_path = filedialog.askdirectory()
        if download_path:
            self.download_location = download_path
            self.download_label.config(
                text=f"Download Location: {os.path.basename(download_path)}"
            )
            self.check_run_button_state()

    def check_run_button_state(self):
        if self.uploaded_file and self.download_location:
            self.run_button.config(state="normal")
        else:
            self.run_button.config(state="disabled")

    def run_process(self):
        self.run_button.config(state="disabled")
        self.show_results_window()

    def show_results_window(self):
        self.results_window = tk.Toplevel(self.root)
        self.results_window.title("Optimization Results")
        self.results_window.geometry("500x300")
        self.results_window.configure(bg="#FFFFFF")

        self.total_combinations_label = ttk.Label(
            self.results_window,
            text="Calculating...",
            font=("Helvetica", 12),
            background="#FFFFFF",
        )
        self.total_combinations_label.pack(pady=10)

        self.num_cores_label = ttk.Label(
            self.results_window, text="", font=("Helvetica", 12), background="#FFFFFF"
        )
        self.num_cores_label.pack(pady=10)

        self.estimated_runtime_label = ttk.Label(
            self.results_window,
            text="Estimating...",
            font=("Helvetica", 12),
            background="#FFFFFF",
        )
        self.estimated_runtime_label.pack(pady=10)

        threading.Thread(target=self.run_optimization).start()

    def run_optimization(self):
        valid_params = self.get_valid_params()
        total_combinations = len(valid_params)
        num_cores = cpu_count()

        self.total_combinations_label.config(
            text=f"Total number of valid parameter combinations: {total_combinations}"
        )
        self.num_cores_label.config(text=f"Number of CPU cores: {num_cores}")

        self.estimated_runtime_label.config(text="Estimating runtime...")
        self.results_window.update()  # Force update of the window

        estimated_runtime = self.estimate_runtime(valid_params, sample_size=10)

        self.estimated_runtime_label.config(
            text=f"Estimated total runtime: {estimated_runtime:.2f} seconds ({estimated_runtime/3600:.2f} hours)"
        )
        self.results_window.update()  # Update the window to show the estimated runtime

        # Add a slight delay to ensure the user can see the estimated runtime
        self.root.after(1000, lambda: self.ask_to_proceed(valid_params))

    def show_final_results(self, best_params, best_energy, total_time, total_params):
        for widget in self.results_window.winfo_children():
            widget.destroy()

        ttk.Label(
            self.results_window,
            text="Optimization Complete",
            font=("Helvetica", 14, "bold"),
            background="#FFFFFF",
        ).pack(pady=10)
        ttk.Label(
            self.results_window,
            text=f"Best parameters: nsol={best_params[0]}, npermute={best_params[1]}, "
            f"minlength={best_params[2]}, maxlength={best_params[3]}, dontbreak={best_params[4]}",
            font=("Helvetica", 12),
            background="#FFFFFF",
            wraplength=450,
        ).pack(pady=5)
        ttk.Label(
            self.results_window,
            text=f"Best Gibbs free energy: {best_energy}",
            font=("Helvetica", 12),
            background="#FFFFFF",
        ).pack(pady=5)
        ttk.Label(
            self.results_window,
            text=f"Total number of combinations: {total_params}",
            font=("Helvetica", 12),
            background="#FFFFFF",
        ).pack(pady=5)
        ttk.Label(
            self.results_window,
            text=f"Total run time: {total_time:.2f} seconds ({total_time/3600:.2f} hours)",
            font=("Helvetica", 12),
            background="#FFFFFF",
        ).pack(pady=5)
        ttk.Label(
            self.results_window,
            text=f"Average time per run: {total_time/total_params:.2f} seconds",
            font=("Helvetica", 12),
            background="#FFFFFF",
        ).pack(pady=5)

    def get_valid_params(self):
        nsol_values = [1, 2, 3, 4, 5, 10, 20, 30]
        npermute_values = [0, 1, 2, 5, 10, 20, 30]
        minlength_values = [20, 21, 22, 23, 24]
        maxlength_values = [60, 61, 62, 63, 64]
        dontbreak_values = [20, 21, 22, 23, 24]

        valid_params = [
            (nsol, npermute, minlength, maxlength, dontbreak)
            for nsol, npermute, minlength, maxlength, dontbreak in itertools.product(
                nsol_values,
                npermute_values,
                minlength_values,
                maxlength_values,
                dontbreak_values,
            )
            if minlength >= dontbreak and minlength < maxlength
        ]

        return valid_params

    def estimate_runtime(self, valid_params, sample_size=10):
        total_combinations = len(valid_params)

        sample_params = random.sample(
            valid_params, min(sample_size, total_combinations)
        )

        sample_times = []
        for params in sample_params:
            result = self.run_autobreak(params)
            if result[1] is not None:  # Check if the time is not None
                sample_times.append(result[1])

        if not sample_times:
            messagebox.showerror(
                "Error", "All sample runs failed. Please check your setup."
            )
            return 0

        avg_time_per_run = sum(sample_times) / len(sample_times)

        num_cores = cpu_count()
        estimated_total_time = (total_combinations * avg_time_per_run) / num_cores

        return estimated_total_time

    def run_full_optimization(self, valid_params):
        # Update the results window
        self.results_window.title("Optimization in Progress")
        for widget in self.results_window.winfo_children():
            widget.destroy()

        progress_label = ttk.Label(
            self.results_window,
            text="Optimization in progress...",
            font=("Helvetica", 12),
            background="#FFFFFF",
        )
        progress_label.pack(pady=10)

        progress_bar = ttk.Progressbar(
            self.results_window, length=400, mode="determinate"
        )
        progress_bar.pack(pady=10)

        # Start the optimization in a separate thread
        threading.Thread(
            target=self.optimize_parameters, args=(valid_params, progress_bar)
        ).start()

    def ask_to_proceed(self, valid_params):
        proceed = messagebox.askyesno(
            "Proceed with Optimization",
            "Do you want to proceed with the full optimization?",
        )
        if proceed:
            self.run_full_optimization(valid_params)
        else:
            self.results_window.destroy()
            messagebox.showinfo(
                "Optimization Cancelled", "The optimization process has been cancelled."
            )

    def optimize_parameters(self, valid_params, progress_bar):
        total_params = len(valid_params)
        best_energy = float("inf")
        best_params = None
        total_time = 0

        for i, params in enumerate(valid_params):
            energy, run_time, _ = self.run_autobreak(params)
            if energy is not None and energy < best_energy:
                best_energy = energy
                best_params = params
            total_time += run_time

            # Update progress
            progress = (i + 1) / total_params * 100
            self.root.after(0, progress_bar.config, {"value": progress})

        # Show final results
        self.show_final_results(best_params, best_energy, total_time, total_params)

    def run_autobreak(self, params):
        start_time = time.time()
        nsol, npermute, minlength, maxlength, dontbreak = params

        run_dir = os.path.join(
            self.download_location,
            f"run_{nsol}_{npermute}_{minlength}_{maxlength}_{dontbreak}",
        )
        os.makedirs(run_dir, exist_ok=True)

        cmd = [
            "python",
            "autobreak_main.py",
            "-i",
            self.uploaded_file,
            "-o",
            run_dir,
            "--rule",
            "xstap.all3",
            "--func",
            "dG:50",
            "--nsol",
            str(nsol),
            "--minlength",
            str(minlength),
            "--maxlength",
            str(maxlength),
            "--verbose",
            "1",
            "--npermute",
            str(npermute),
            "--writeall",
            "--sequence",
            "yk_p7560.txt",
            "--dontbreak",
            str(dontbreak),
            "--seed",
            "0",
            "--score",
            "sum",
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            match = re.search(
                r"Final Gibbs Free Energy of the best solution: ([-\d.]+)",
                result.stdout,
            )
            if match:
                energy = float(match.group(1))
                run_time = time.time() - start_time
                return energy, run_time, params
            else:
                print(f"Error: Couldn't extract Gibbs free energy for {params}")
                return None, time.time() - start_time, params
        except subprocess.CalledProcessError as e:
            print(f"Error running autobreak_main.py for {params}: {e}")
            return None, time.time() - start_time, params
        finally:
            shutil.rmtree(run_dir, ignore_errors=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = OrigamiApp(root)
    root.mainloop()
