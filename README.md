# Llama-2 Statistical Analysis

This project performs statistical analysis on CSV files, generates plots, and answers questions using the Llama-2 model.

## Setup

1. Create and activate a virtual environment:
    ```bash
    python -m venv llama2-stat-analysis
    source llama2-stat-analysis/bin/activate  # On Windows, use `llama2-stat-analysis\Scripts\activate`
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run streamlit_app.py
    ```

## Files

- `llama2_stat_analysis/`: Contains the main application logic and functions.
- `streamlit_app.py`: Streamlit application for the user interface.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Usage

Upload a CSV file, view basic statistics, generate plots, and ask questions about the data using the Streamlit interface.
