# Statistical Analysis of API Access Behaviors: Insights into API Access Patterns

## Author

Radley E. Sidwell-Lewis

## Instructions

This README provides instructions for setting up the Python environment needed to run the analysis scripts featured in the abovementioned paper.

## Prerequisites

### 1. Python 3 Installation

Ensure you have Python 3.6 or newer installed on your system.

#### Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

#### If Python 3 is not installed:

**For Windows:**

- Download the installer from [python.org](https://www.python.org/downloads/)
- Run the installer and make sure to check "Add Python to PATH" during installation

**For macOS:**

- Using Homebrew:
  ```bash
  brew install python3
  ```
- Or download from [python.org](https://www.python.org/downloads/)

**For Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**For Linux (Fedora/RHEL/CentOS):**

```bash
sudo dnf install python3 python3-pip
```

## Setting Up the Virtual Environment

### 1. Create a Virtual Environment

Navigate to your project directory in the terminal/command prompt and run:

**On Windows:**

```bash
python -m venv venv
```

**On macOS/Linux:**

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your terminal prompt, indicating the virtual environment is active.

### 3. Install Required Packages

Once your virtual environment is activated, install the required packages:

```bash
pip install -r requirements.txt
```

## Running the code

Each of the 21 figures can be run with:

```bash
# e.g. python figure_{number}.py
python figure_01.py
```

## Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment by simply running:

```bash
deactivate
```
