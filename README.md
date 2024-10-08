# football_field_chart
Python script to generate simple M&amp;A Valuation football field chart

# Football Field Chart Generator

This Python script generates a football field chart to visualize valuation ranges for different metrics of a company. It uses matplotlib for chart creation and tkinter for user input.

## Features

- Interactive user input for company details and metrics
- Customizable valuation ranges for each metric
- Clear visualization of valuation ranges using a football field chart
- Automatic adjustment of chart layout and scaling

## Requirements

- Python 3.x
- matplotlib
- numpy
- tkinter (usually comes pre-installed with Python)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries:

```
## Usage

1. Run the script:

```
2. Follow the prompts to enter:
   - Company name
   - Metrics (comma-separated)
   - Units for valuation (e.g., "$ Millions")
   - Minimum and maximum values for each metric

3. The script will generate and display the football field chart based on your input.

## Example

Input:
- Company Name: TechCorp Inc.
- Metrics: P/E Ratio, EV/EBITDA, P/B Ratio
- Units: $ Millions
- Values:
  - P/E Ratio: 15, 25
  - EV/EBITDA: 8, 12
  - P/B Ratio: 2, 4

Output:
A football field chart showing the valuation ranges for TechCorp Inc. based on the provided metrics and values.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
