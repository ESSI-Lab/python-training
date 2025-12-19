import requests
import pandas as pd
from IPython.display import display
from tabulate import tabulate
import sys

# ================= CONFIG =================
token = 'whos-2bbd201b-9908-44b6-ad5c-e3b9a6e3bcda'
view = 'whos'
baseURL = 'https://whos.geodab.eu/gs-service/services/essi/token/'
apiURL = baseURL + token + '/view/' + view + '/om-api/'

def obfuscate_token(text, token):
    """Hide the token for safe printing"""
    return text.replace(token, "***")

# ================ CONSTRAINTS ================
# Feature-level constraints
feature_constraints = {
    "west": 22.438,
    "south": 60.347,
    "east": 23.012,
    "north": 60.714,
    "observedProperty": None,
    "ontology": None
}

# Observation-level constraints
observation_constraints = {
    "observedProperty": None,  # Can filter by property if desired
    "phenomenonTimeBegin": "1943-07-01T00:00:00Z",
    "phenomenonTimeEnd": "2025-12-17T09:45:19Z",
    "ontology": "whos"
}

# =================== FEATURES ===================
features_url = apiURL + "features"
response = requests.get(features_url, params=feature_constraints)
print("Retrieving features:", obfuscate_token(response.url, token))

if response.status_code != 200:
    raise Exception(f"Feature request failed: {response.status_code}")

feature_data = response.json()

# Extract feature IDs
feature_ids = [f["id"] for f in feature_data.get("results", [])]

# Optional: create DataFrame for feature info
features_list = []
for f in feature_data.get("results", []):
    coordinates = f['shape']['coordinates']
    params = {p['name']: p['value'] for p in f['parameter']}
    features_list.append({
        "Name": f["name"],
        "ID": f["id"],
        "Coordinates": f"{coordinates[0]}, {coordinates[1]}",
        "Source": params.get("source", ""),
        "Identifier": params.get("identifier", ""),
        "Country": params.get("country", "")
    })

df_features = pd.DataFrame(features_list)

# Display features nicely
if 'ipykernel' in sys.modules:
    display(df_features)
else:
    print(tabulate(df_features, headers='keys', tablefmt='grid'))

# ================= OBSERVATIONS ==================
observations_list = []

for feature_id in feature_ids:
    obs_url = apiURL + "observations"
    params = {
        "feature": feature_id,
        "phenomenonTimeBegin": observation_constraints["phenomenonTimeBegin"],
        "phenomenonTimeEnd": observation_constraints["phenomenonTimeEnd"],
        "observedProperty": observation_constraints["observedProperty"] or ""
    }
    response = requests.get(obs_url, params=params)
    print("Retrieving observations:", obfuscate_token(response.url, token))

    if response.status_code != 200:
        print(f"Observation request failed for feature {feature_id}: {response.status_code}")
        continue

    obs_data = response.json()
    for obs in obs_data.get("member", []):
        params_dict = {p['name']: p['value'] for p in obs['parameter']}
        result_meta = obs['result'].get('defaultPointMetadata', {})
        observations_list.append({
            "Feature ID": obs['featureOfInterest']['href'],
            "Source": params_dict.get("source", ""),
            "Observed Property Definition": params_dict.get("observedPropertyDefinition", ""),
            "Observed Property": obs['observedProperty']['title'],
            "Phenomenon Time Begin": obs['phenomenonTime']['begin'],
            "Phenomenon Time End": obs['phenomenonTime']['end'],
            "Observation ID": obs['id'],
            "Observation Type": obs.get('type', ""),
            "Unit of Measurement": result_meta.get("uom", ""),
        })

df_observations = pd.DataFrame(observations_list)

# Display observations nicely
if 'ipykernel' in sys.modules:
    display(df_observations)
else:
    print(tabulate(df_observations, headers='keys', tablefmt='grid'))
