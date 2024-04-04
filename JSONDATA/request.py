import json
from requests import get

# Github link of the JSON data
github_link = 'https://raw.githubusercontent.com/mutemip/dictionary-data/master/data.json'

response = get(github_link)

# Print response from status code and content for debugging
print("Response Status Code:", response.status_code)
print("Response Content:", response.text)

#check if the request was successful
if response.status_code == 200:
    # Parse JSON data into python 
    data_dict = json.loads(response.text)
    print("Data loaded successfully into dictionary:", data_dict)
else:
    print("Failed to fetch JSON data from Github")    
    
    
    