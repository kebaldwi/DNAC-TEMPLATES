import csv
from jinja2 import Environment, FileSystemLoader

with open("CODE/TRAFFIC/traffic_log.csv", mode='r') as file:
    traffic_file = csv.reader(file)
    traffic = [line for line in traffic_file]

headers = traffic.pop(0)
xaxis = []
views = []
unique = []

# Initialize total counters and a dictionary to track unique dates
total_views = 0
total_unique = 0
date_tracker = {}

# Build Data line by line
for line in traffic:
    date = line[0].split()[0]
    view_count = int(line[1])
    unique_count = int(line[2])

    # Check if the date is already in the tracker
    if date not in date_tracker:
        date_tracker[date] = {'views': 0, 'unique': 0}

    # Always use highest views and unique counts for that date
    if date_tracker[date]['views'] < view_count:
        date_tracker[date]['views'] = view_count
    if date_tracker[date]['unique'] < unique_count:
        date_tracker[date]['unique'] = unique_count

# Prepare the data for rendering
for date, counts in date_tracker.items():
    xaxis.append(date)
    views.append(counts['views'])
    unique.append(counts['unique'])
    
    # Update total counts
    total_views += counts['views']
    total_unique += counts['unique']
    
# Create a Jinja environment
env = Environment(loader=FileSystemLoader('.'))

# Load the template
template = env.get_template('CODE/SCRIPTS/mermaid_v2.j2')

rendered_template = template.render(xaxis=xaxis, views=views, unique=unique, total_views=total_views, total_unique=total_unique)

with open('CODE/TRAFFIC/README.md', 'w') as f:
    f.write(rendered_template)
