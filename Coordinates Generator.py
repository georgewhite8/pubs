
import pandas as pd
from geopy.geocoders import GoogleV3

# Load your data
geolocator = GoogleV3(api_key='AIzaSyBt9WxiiPWb-ZD0WR14pf5ZzhuxKP2iD_s')
pubs = pd.read_csv('C:/Users/Georg/OneDrive/Documents/Pub Project/PUBS - London.csv')

# Add combined name column to enable searching

pubs['combined'] = pubs['Pub'] + " " + pubs['Area']
# Add latitude and longitude columns
def geocode(combined):
    try:
        location = geolocator.geocode(combined)
        return location.latitude, location.longitude
    except:
        return None, None

pubs['latitude'], pubs['longitude'] = zip(*pubs['Pub'].apply(geocode))
pubs.to_csv('C:/Users/Georg/OneDrive/Documents/Pub Project/pubs_coordinates.csv', index=False)

print(pubs)