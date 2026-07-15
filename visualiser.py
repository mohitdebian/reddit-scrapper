import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "post_history.csv"
OUTPUT_IMAGE = "score_trajectories.png"

def plot_data():
    """Reads the CSV and plots score trajectories for each post."""
    try:
        # Read the CSV data
        df = pd.read_csv(CSV_FILE)
        
        # Convert timestamp strings into datetime objects for better plotting
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    except Exception as e:
        print("Error reading CSV file:", e)
        return

    # Set up the plot figure size
    plt.figure(figsize=(10, 6))
    
    # Get all unique post titles
    unique_titles = df['title'].unique()
    
    # Loop through each title and add a line to the plot
    for title in unique_titles:
        # Filter data for just this post
        post_data = df[df['title'] == title]
        
        # Plot time on X axis and score on Y axis
        x_values = post_data['timestamp']
        y_values = post_data['score']
        
        # Truncate title for legend if it's too long
        legend_title = title
        if len(legend_title) > 30:
            legend_title = legend_title[:30] + "..."
            
        plt.plot(x_values, y_values, marker='o', label=legend_title)
        
    # Add chart labels and title
    plt.title('Reddit Post Score Trajectories Over Time')
    plt.xlabel('Time')
    plt.ylabel('Score')
    
    # Add grid and legend
    plt.grid(True)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    # Make layout fit nicely so legend is not cut off
    plt.tight_layout()
    
    # Save the figure to a file
    try:
        plt.savefig(OUTPUT_IMAGE)
        print("Graph saved as", OUTPUT_IMAGE)
    except Exception as e:
        print("Error saving image:", e)
        
    # Show the plot window
    plt.show()

# Run the visualizer
if __name__ == "__main__":
    plot_data()
