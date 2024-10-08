# Import necessary libraries
import matplotlib.pyplot as plt  # For creating charts and plots
import numpy as np  # For numerical operations and array handling
import tkinter as tk
from tkinter import simpledialog

def create_football_field_chart(metrics, values, company_name, units):
    """
    Create a football field chart to visualize valuation ranges for different metrics.
    
    :param metrics: List of metric names
    :param values: List of value ranges for each metric (list of lists)
    :param company_name: Name of the company being analyzed
    :param units: Units for the valuation (e.g., "$ Millions")
    """
    # Create a new figure and axis object with specified size
    fig, ax = plt.subplots(figsize=(12, 6))

    # Create horizontal bars representing value ranges
    y_pos = np.arange(len(metrics))  # Generate y-positions for each metric
    ax.barh(y_pos,  # Y-coordinates for bars
            [max(v) - min(v) for v in values],  # Width of each bar (range)
            left=[min(v) for v in values],  # Starting point of each bar
            height=0.5,  # Height of each bar
            color='lightgray')  # Color of the bars

    # Add metric names to the y-axis
    ax.set_yticks(y_pos)  # Set the positions of y-axis ticks
    ax.set_yticklabels(metrics)  # Label the y-axis ticks with metric names

    # Calculate x-axis limits with padding for better visualization
    all_values = [val for sublist in values for val in sublist]  # Flatten the values list
    x_min, x_max = min(all_values), max(all_values)  # Find overall min and max
    padding = (x_max - x_min) * 0.1  # Calculate 10% padding
    ax.set_xlim(x_min - padding, x_max + padding)  # Set x-axis limits with padding

    # Add value labels with padding
    text_padding = padding * 0.5  # Adjust this value to increase/decrease text padding
    for i, (metric, value_range) in enumerate(zip(metrics, values)):
        # Add minimum value label
        ax.text(min(value_range) - text_padding, i, f'${min(value_range):.1f}',
                va='center', ha='right', fontweight='bold')
        # Add maximum value label
        ax.text(max(value_range) + text_padding, i, f'${max(value_range):.1f}',
                va='center', ha='left', fontweight='bold')

    # Customize the chart appearance
    ax.set_xlabel(f'Valuation ({units})')  # Set x-axis label with units
    ax.set_title(f'Valuation Football Field Chart - {company_name}')  # Set chart title
    ax.spines['top'].set_visible(False)  # Remove top spine
    ax.spines['right'].set_visible(False)  # Remove right spine
    ax.spines['left'].set_visible(False)  # Remove left spine

    # Adjust layout to prevent clipping and show the plot
    plt.tight_layout()
    plt.show()

def get_user_input():
    """
    Create a system window that prompts the user for metrics, values, company name, and units.
    
    :return: tuple containing metrics, values, company name, and units
    """
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt for company name
    company_name = simpledialog.askstring("Input", "Enter the company name:")

    # Prompt for metrics
    metrics_input = simpledialog.askstring("Input", "Enter metrics (comma-separated):")
    metrics = [m.strip() for m in metrics_input.split(',')]

    # Prompt for units
    units = simpledialog.askstring("Input", "Enter units (e.g., $ Millions):")

    # Prompt for values
    values = []
    for metric in metrics:
        value_input = simpledialog.askstring("Input", f"Enter min and max values for {metric} (comma-separated):")
        min_val, max_val = map(float, value_input.split(','))
        values.append([min_val, max_val])

    return metrics, values, company_name, units

# Get user input
metrics, values, company_name, units = get_user_input()

# Call the function to create and display the chart
create_football_field_chart(metrics, values, company_name, units)
