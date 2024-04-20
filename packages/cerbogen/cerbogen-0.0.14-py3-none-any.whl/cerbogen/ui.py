import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cerbogen import binbeats

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot import Plot

def generate_binaural_beats():
    base_f = float(base_entry.get())
    diff = float(diff_entry.get())
    duration = int(duration_entry.get())
    output_file = output_bin_entry.get()
    selected_format = format_combobox.get()

    binbeats.reset()
    binbeats.steady(base_f, diff, duration)
    binbeats.save(output_file, format=selected_format)
    messagebox.showinfo("Binaural Beats Generator", f"Binaural beats file '{output_file}' generated successfully!")

def generate_power_nap():
    base_f = float(power_nap_base_entry.get())
    start_diff = float(power_nap_start_diff_entry.get())
    goto_d = float(power_nap_goto_d_entry.get())
    exit_time = int(power_nap_exit_time_entry.get())
    stay_duration = int(power_nap_stay_duration_entry.get())
    selected_format = power_nap_format_combobox.get()

    binbeats.reset()
    binbeats.power_nap(base_f, start_diff, goto_d, exit_time, stay_duration)
    output_file = output_entry.get()
    binbeats.save(output_file, format=selected_format)
    messagebox.showinfo("Power Nap Generator", f"Power nap file '{output_file}' generated successfully!")

def plot_line():
    base_f = float(base_entry.get())
    diff = float(diff_entry.get())
    duration = int(duration_entry.get())
    binbeats.reset()
    binbeats.steady(base_f, diff, duration)
    Plot.plot_line(binbeats.diffrence, binbeats.timeline)

def plot_waveform():
    output_file = output_bin_entry.get()
    Plot.plot_waveform(output_file)

def plot_power_nap():
    base_f = float(power_nap_base_entry.get())
    start_diff = float(power_nap_start_diff_entry.get())
    goto_d = float(power_nap_goto_d_entry.get())
    exit_time = int(power_nap_exit_time_entry.get())
    stay_duration = int(power_nap_stay_duration_entry.get())
    binbeats.reset()
    binbeats.power_nap(base_f, start_diff, goto_d, exit_time, stay_duration)
    Plot.line_progression(binbeats.diffrence, binbeats.timeline)


def check_update():
    pass

def update():
    pass


# Main window
root = tk.Tk()
root.title("CerboGen")

# RESOLUTION
root.geometry("340x700")  # Set initial window size

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to place the window on the left side, touching the top
x_pos = 0
y_pos = 0

# Set the position of the window
root.geometry("+{}+{}".format(x_pos, y_pos))


# Set the icon for the window
root.iconbitmap("./data/img/logo.ico")

# Lock window resizing
root.resizable(False, False)

# Theremin-style background
background_color = "#2c3e50"
root.configure(bg=background_color)

#  ------------------------------------------------------------------------------------------------

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Settings menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Nothing Here", )

# Update menu
update_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Update", menu=update_menu)
update_menu.add_command(label="Check for updates", command=check_update)
update_menu.add_command(label="Update", command=update)

#  ------------------------------------------------------------------------------------------------

# Binaural Beats Generator UI

binaural_frame = ttk.Frame(root, padding=10)
binaural_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ns")


# Binaural Beats Generator Heading
binaural_heading = ttk.Label(binaural_frame, text="Binaural Beats Generator", font=("Helvetica", 14, "bold"), background=background_color, foreground="white")
binaural_heading.grid(row=0, column=0, columnspan=2, pady=5)

base_label = ttk.Label(binaural_frame, text="Base Frequency:", background=background_color, foreground="white")
base_entry = ttk.Entry(binaural_frame)
base_label.grid(row=1, column=0, padx=5, pady=5)
base_entry.grid(row=1, column=1, padx=5, pady=5)

diff_label = ttk.Label(binaural_frame, text="Difference:", background=background_color, foreground="white")
diff_entry = ttk.Entry(binaural_frame)
diff_label.grid(row=2, column=0, padx=5, pady=5)
diff_entry.grid(row=2, column=1, padx=5, pady=5)

duration_label = ttk.Label(binaural_frame, text="Duration (mins):", background=background_color, foreground="white")
duration_entry = ttk.Entry(binaural_frame)
duration_label.grid(row=3, column=0, padx=5, pady=5)
duration_entry.grid(row=3, column=1, padx=5, pady=5)

format_label = ttk.Label(binaural_frame, text="Format:", background=background_color, foreground="white")
format_combobox = ttk.Combobox(binaural_frame, values=["wav", "mp3", "flac", "ogg", "m4a", "aiff", "au", "raw"])
format_combobox.current(0)  # Set the default selection to "wav"
format_label.grid(row=4, column=0, padx=5, pady=5)
format_combobox.grid(row=4, column=1, padx=5, pady=5)

output_bin_label = ttk.Label(binaural_frame, text="Output File Name:", background=background_color, foreground="white")
output_bin_entry = ttk.Entry(binaural_frame)
output_bin_label.grid(row=5, column=0, padx=5, pady=5)
output_bin_entry.grid(row=5, column=1, padx=5, pady=5)

# Add Plot Bin Beats Button
plot_binaural_button = ttk.Button(binaural_frame, text="Plot Bin Beats", command=plot_line)
plot_binaural_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Generate Bin Beats
binaural_button = ttk.Button(binaural_frame, text="Generate Binaural Beats", command=generate_binaural_beats)
binaural_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# ------------------------------------------------------------------------------------------------------------

# Power Nap Generator UI
power_nap_frame = ttk.Frame(root, padding=10)
power_nap_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Power Nap Generator Heading
power_nap_heading = ttk.Label(power_nap_frame, text="Power Nap Generator", font=("Helvetica", 14, "bold"), background=background_color, foreground="white")
power_nap_heading.grid(row=0, column=0, columnspan=2, pady=5)

power_nap_base_label = ttk.Label(power_nap_frame, text="Base Frequency:", background=background_color, foreground="white")
power_nap_base_entry = ttk.Entry(power_nap_frame)
power_nap_base_label.grid(row=1, column=0, padx=5, pady=5)
power_nap_base_entry.grid(row=1, column=1, padx=5, pady=5)

power_nap_start_diff_label = ttk.Label(power_nap_frame, text="Start Difference:", background=background_color, foreground="white")
power_nap_start_diff_entry = ttk.Entry(power_nap_frame)
power_nap_start_diff_label.grid(row=2, column=0, padx=5, pady=5)
power_nap_start_diff_entry.grid(row=2, column=1, padx=5, pady=5)

power_nap_goto_d_label = ttk.Label(power_nap_frame, text="Go To Difference:", background=background_color, foreground="white")
power_nap_goto_d_entry = ttk.Entry(power_nap_frame)
power_nap_goto_d_label.grid(row=3, column=0, padx=5, pady=5)
power_nap_goto_d_entry.grid(row=3, column=1, padx=5, pady=5)

power_nap_exit_time_label = ttk.Label(power_nap_frame, text="Start/Exit Time (mins):", background=background_color, foreground="white")
power_nap_exit_time_entry = ttk.Entry(power_nap_frame)
power_nap_exit_time_label.grid(row=4, column=0, padx=5, pady=5)
power_nap_exit_time_entry.grid(row=4, column=1, padx=5, pady=5)

power_nap_stay_duration_label = ttk.Label(power_nap_frame, text="Stay Duration (mins):", background=background_color, foreground="white")
power_nap_stay_duration_entry = ttk.Entry(power_nap_frame)
power_nap_stay_duration_label.grid(row=5, column=0, padx=5, pady=5)
power_nap_stay_duration_entry.grid(row=5, column=1, padx=5, pady=5)

power_nap_format_label = ttk.Label(power_nap_frame, text="Format:", background=background_color, foreground="white")
power_nap_format_combobox = ttk.Combobox(power_nap_frame, values=["wav", "mp3", "flac", "ogg", "m4a", "aiff", "au", "raw"])
power_nap_format_combobox.current(0)  # Set the default selection to "wav"
power_nap_format_label.grid(row=6, column=0, padx=5, pady=5)
power_nap_format_combobox.grid(row=6, column=1, padx=5, pady=5)

output_label = ttk.Label(power_nap_frame, text="Output File Name:", background=background_color, foreground="white")
output_entry = ttk.Entry(power_nap_frame)
output_label.grid(row=7, column=0, padx=5, pady=5)
output_entry.grid(row=7, column=1, padx=5, pady=5)

# Add Plot Power Nap Button
plot_power_nap_button = ttk.Button(power_nap_frame, text="Plot Power Nap", command=plot_power_nap)
plot_power_nap_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Save Power Nap Button
power_nap_button = ttk.Button(power_nap_frame, text="Save Power Nap", command=generate_power_nap)
power_nap_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
