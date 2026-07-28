# Reddit Post Growth Tracker

A simple Python project that tracks the score growth of "hot" posts on Reddit (`r/technology`), analyzes their trajectory, and generates a visual graph.

This project is beginner-friendly and built using functional programming constructs without advanced python tricks.

## Libraries Used
- `requests` (for fetching Reddit JSON data)
- `pandas` (for data manipulation and analysis)
- `matplotlib` (for generating graphs)
- `time`, `datetime`, `csv`, `os` (built-in libraries)

## Installation Steps

1. Make sure you have Python installed.
2. Clone or download this project.
3. Open a terminal or command prompt in the project directory.
4. Install the required libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Testing During Development

By default, the tracker runs every 1800 seconds (30 minutes). If you want to test the project quickly without waiting 3 hours:
1. Open `tracker.py` in your text editor.
2. Find the variable `POLL_INTERVAL_SECONDS = 1800`.
3. Change it to `POLL_INTERVAL_SECONDS = 10`.
4. Run `tracker.py` for about a minute. This will fetch new data every 10 seconds and generate enough rows in the CSV file for you to analyze and visualize.

## How to Run the Project

The project is split into three separate tools. You should run them in this order:

### 1. Data Tracker
Run the tracker to start fetching data. Keep it running to collect more data. Press `Ctrl+C` to stop it.
```bash
python tracker.py
```
This will create a `post_history.csv` file and append data to it.

### 2. Data Analyser
Once you have collected data for a while (at least a few data points per post), run the analyser.
```bash
python analyser.py
```
This reads the CSV file and outputs statistics (absolute growth, percentage growth, acceleration, and consistency). It also saves these results to `growth_analysis.txt`.

### 3. Data Visualiser
To see a graph of how the posts are growing, run the visualiser.
```bash
python visualiser.py
```
This opens a window showing a line chart of the scores over time. It will also save the graph as `score_trajectories.png`.
