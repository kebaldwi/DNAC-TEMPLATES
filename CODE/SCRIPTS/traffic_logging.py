import requests
import json
import csv
import datetime
import os
from pdfkit import from_file

# Get credentials from environment variables
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
OWNER = os.getenv('OWNER')
REPO = os.getenv('REPO')

def get_traffic_insights():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/traffic/views"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Failed to fetch traffic insights. Status code: {response.status_code}")
        return None

def log_traffic_insights(traffic_insights):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    views = traffic_insights['count']
    unique_visitors = traffic_insights['uniques']

    log_entry = [timestamp, views, unique_visitors]

    # Append the log entry to CSV file
    csv_file_path = "CODE/TRAFFIC/traffic_log.csv"
    file_exists = os.path.isfile(csv_file_path)

    with open(csv_file_path, "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write header only if file didn't exist before
        if not file_exists:
            writer.writerow(["Timestamp", "Views", "Unique Visitors"])
        writer.writerow(log_entry)

def save_page_as_pdf():
    session = requests.Session()
    session.auth = (OWNER, ACCESS_TOKEN)

    url = f"https://github.com/{OWNER}/{REPO}/graphs/traffic"
    html_filename = "traffic_report.html"

    with open(html_filename, "w") as html_file:
        response = session.get(url)
        html_file.write(response.text)

    pdf_filename = "traffic_report.pdf"
    from_file(html_filename, pdf_filename)

# Get traffic insights
traffic_data = get_traffic_insights()

if traffic_data:
    log_traffic_insights(traffic_data)
    print("Traffic insights logged successfully.")