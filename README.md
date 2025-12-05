# CS50 Python Course

This repository contains all problem sets for the CS50 Python course, organized by sets (set0 through set8).

## Environment Setup

This project uses a consolidated virtual environment managed by `uv` instead of separate environments for each problem set.

### Dependencies

The consolidated environment includes all libraries used across different problem sets:

- **emoji** (>=2.14.1) - For emoji handling
- **fpdf2** (>=2.8.3) - For PDF generation
- **inflect** (>=7.5.0) - For natural language inflection
- **pillow** (>=11.3.0) - For image processing
- **pyfiglet** (>=1.0.3) - For ASCII art text
- **python-dotenv** (>=1.1.1) - For environment variable management
- **requests** (>=2.32.4) - For HTTP requests
- **tabulate** (>=0.9.0) - For table formatting
- **validators** (>=0.35.0) - For data validation

### Development Dependencies

- **pylint** (>=3.3.7) - Code linting
- **pytest** (>=8.4.1) - Testing framework

### Usage

To activate the environment and work with any problem set:

```bash
# Activate the environment
uv sync

# Run Python files from any set directory
uv run python set4/adieu.py
uv run python set5/test_plates.py
# etc.
```

### Directory Structure

- `set0/` - Problem Set 0
- `set1/` - Problem Set 1
- `set2/` - Problem Set 2
- `set3/` - Problem Set 3
- `set4/` - Problem Set 4
- `set5/` - Problem Set 5
- `set6/` - Problem Set 6
- `set7/` - Problem Set 7
- `set8/` - Problem Set 8
- `finalProject/` - Final Project

Each directory contains the Python files and any additional resources for that problem set.
