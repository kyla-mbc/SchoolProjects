import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import numpy as np

# Function to create the first plot
def plot_simple():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Simple Plot Example')
    plt.show()

# Function to create the second plot
def plot_bar():
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [25, 40, 30, 50]
    plt.bar(categories, values, color='green', alpha=0.7)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Chart Example')
    plt.show()

# Function to create the third plot
def plot_scatter():
    np.random.seed(42)
    x = np.random.rand(10)
    y = np.random.rand(10)
    plt.scatter(x, y, color='red', label='Random Data')
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Scatter Plot Example')
    plt.legend()
    plt.show()

# Function to handle button clicks
def on_button_click(plot_function):
    # Clear previous plots
    plt.clf()
    # Call the appropriate plot function
    plot_function()

# Create the main window
root = tk.Tk()
root.title("GUI Plot")

# Create buttons for each plot
simple_button = ttk.Button(root, text="Simple Plot", command=lambda: on_button_click(plot_simple))
bar_button = ttk.Button(root, text="Bar Chart", command=lambda: on_button_click(plot_bar))
scatter_button = ttk.Button(root, text="Scatter Plot", command=lambda: on_button_click(plot_scatter))

# Place buttons in the window
simple_button.pack(pady=10)
bar_button.pack(pady=10)
scatter_button.pack(pady=10)

# Start the main loop
root.mainloop()
