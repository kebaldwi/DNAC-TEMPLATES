import csv
from jinja2 import Environment, FileSystemLoader

with open("TRAFFIC/traffic_log.csv", mode='r') as file:
    traffic_file = csv.reader(file)
    traffic = [line for line in traffic_file]

headers = traffic.pop(0)
xaxis = []
views = []
unique = []
for line in traffic:
    xaxis.append(line[0].split()[0])
    views.append(line[1])
    unique.append(line[2])

# Create a Jinja environment
env = Environment(loader=FileSystemLoader('.'))

# Load the template
template = env.get_template('TRAFFIC/mermaid.j2')

rendered_template = template.render(xaxis=xaxis, views=views, unique=unique)

with open('TRAFFIC/readme.md', 'w') as f:
    f.write(rendered_template)
