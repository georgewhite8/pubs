import pandas as pd
pubs = pd.read_csv('pubs_coordinates.csv')
pubs[['Pub', 
      'Area', 
      'latitude', 
      'longitude', 
      'Location',
      'Atmos',
      'Drinks',
      'Value',
      'Facilities',
      'Total'
      ]].to_json('pubs.json', orient='records')

print(pubs)

import json

# Load single-line JSON
with open('pubs.json', 'r') as file:
    data = json.load(file)

# Save it prettified
with open('pubs_pretty.json', 'w') as file:
    json.dump(data, file, indent=4)


