# Logistics Data Analyst Project

This project loads logistics data from PostgreSQL, performs analysis and visualization using Python, and generates a summary report using OpenAI's language model.

## Files

- `logistics_analysis.py`: Loads and analyzes logistics data, generates summary statistics and visualizations.
- `logistics_report.py`: Generates a natural language report using OpenAI based on the analysis.
- `logistics_data.csv`: Sample logistics dataset used for analysis.
- `.env`: Contains the OpenAI API key (this file is excluded from GitHub using `.gitignore`).
- `.gitignore`: Specifies files and folders to exclude from version control, including `.env`.

## How to Use

### 1. Install Required Libraries

Use the following command to install the necessary Python packages:

```bash
pip install pandas matplotlib sqlalchemy openai python-dotenv
```

### 2. Set Up the Environment File

Create a file named `.env` in the project root directory and add your OpenAI API key as shown:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run the Scripts

First, run the data analysis script:

```bash
python logistics_analysis.py
```

Then, run the report generation script:

```bash
python logistics_report.py
```

## Features

- Connects to PostgreSQL to retrieve logistics data.
- Performs aggregation by item and base.
- Visualizes data trends using bar and line charts.
- Uses OpenAI to generate a professional summary report.
