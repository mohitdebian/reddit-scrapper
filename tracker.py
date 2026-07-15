import requests
import time
import datetime
import csv
import os

# To test this project quickly, change POLL_INTERVAL_SECONDS from 1800 to 10
# This will fetch data every 10 seconds instead of every 30 minutes.
POLL_INTERVAL_SECONDS = 1800 

URL = "https://www.reddit.com/r/technology/hot.json?limit=5"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
CSV_FILE = "post_history.csv"

def fetch_reddit_data():
    """Fetches the top 5 hot posts from the r/technology subreddit."""
    try:
        response = requests.get(URL, headers=HEADERS)
        # Raise an exception if the request failed
        response.raise_for_status() 
        return response.json()
    except Exception as e:
        print("Error fetching data from Reddit:", e)
        return None

def save_to_csv(posts_data):
    """Parses Reddit JSON data and appends it to a CSV file."""
    # Check if we need to write the header (if file does not exist)
    file_exists = os.path.isfile(CSV_FILE)
    
    try:
        # Open in append mode so we don't overwrite old data
        file = open(CSV_FILE, mode='a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        
        # Write the header only if the file is new
        if not file_exists:
            writer.writerow(["timestamp", "title", "score", "comments"])
        
        # Extract and write data for each post
        children = posts_data['data']['children']
        for child in children:
            post = child['data']
            title = post['title']
            score = post['score']
            comments = post['num_comments']
            
            # Get the current time as a readable string
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Write a row to the CSV
            writer.writerow([current_time, title, score, comments])
            
        file.close()
        print("Data successfully saved at", current_time)
        
    except Exception as e:
        print("Error saving to CSV:", e)

def main():
    """Main loop to continuously fetch and save data."""
    print("Starting Reddit Post Growth Tracker...")
    print("Press Ctrl+C to stop.")
    
    while True:
        data = fetch_reddit_data()
        
        if data != None:
            save_to_csv(data)
            
        print("Waiting for", POLL_INTERVAL_SECONDS, "seconds before next fetch...")
        # Wait for the specified interval
        time.sleep(POLL_INTERVAL_SECONDS)

# Run the program
if __name__ == "__main__":
    main()
