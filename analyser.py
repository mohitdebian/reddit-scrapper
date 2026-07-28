import pandas as pd

CSV_FILE = "post_history.csv"
OUTPUT_FILE = "growth_analysis.txt"

def analyze_data():
    """Reads the CSV, groups by title, analyzes growth, and saves to file."""
    try:
        # Read the CSV data into a pandas DataFrame
        df = pd.read_csv(CSV_FILE)
    except Exception as e:
        print("Error reading CSV file:", e)
        return

    # Open text file to write analysis
    try:
        file = open(OUTPUT_FILE, mode='w', encoding='utf-8')
    except Exception as e:
        print("Error creating output file:", e)
        return
        
    # Get all unique post titles
    unique_titles = df['title'].unique()
    
    # Analyze each post
    for title in unique_titles:
        # Filter the DataFrame to only show rows for this specific title
        post_data = df[df['title'] == title]
        
        # Get scores as a simple list for easy calculation
        scores = post_data['score'].tolist()
        
        if len(scores) < 2:
            continue # We need at least 2 data points for growth analysis
            
        first_score = scores[0]
        last_score = scores[-1]
        
        # Calculate Absolute and Percentage Growth
        absolute_growth = last_score - first_score
        if first_score != 0:
            percentage_growth = (absolute_growth / first_score) * 100
        else:
            percentage_growth = 0
            
        # Calculate simple acceleration if we have 3 or more points
        acceleration = 0
        if len(scores) >= 3:
            first_diff = scores[1] - scores[0]
            last_diff = scores[-1] - scores[-2]
            acceleration = last_diff - first_diff
            
        # Calculate consistency using pandas standard deviation
        consistency = post_data['score'].std()
        
        # Classify post based on acceleration and growth
        classification = "Stable Growth"
        if acceleration > 5:
            classification = "Late Accelerator"
        elif acceleration < -5:
            classification = "Early Peaker"
            
        # Create the analysis text block
        result_text = "\n" + "-"*40 + "\n"
        result_text += "Post: " + title + "\n"
        result_text += "First Score: " + str(first_score) + "\n"
        result_text += "Last Score: " + str(last_score) + "\n"
        result_text += "Absolute Growth: " + str(absolute_growth) + "\n"
        result_text += "Percentage Growth: " + str(round(percentage_growth, 2)) + "%\n"
        if len(scores) >= 3:
            result_text += "Acceleration: " + str(acceleration) + "\n"
        result_text += "Consistency (Std Dev): " + str(round(consistency, 2)) + "\n"
        result_text += "Classification: " + classification + "\n"
        
        # Print to console
        print(result_text)
        
        # Write to file
        file.write(result_text)
        
    file.close()
    print("\nAnalysis saved to", OUTPUT_FILE)

# Run the analyzer
if __name__ == "__main__":
    analyze_data()
