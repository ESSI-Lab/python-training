from dabpy import WHOSClient, Constraints
from IPython.display import display

# Replace with your WHOS API token and optional view
token = "my-token"
view = "whos"
client = WHOSClient(token=token, view=view)

## 00 DEFINE FEATURE CONSTRAINTS
# Define bounding box coordinates (south, west, north, east), example of Finland.
south = 60.347
west = 22.438
north = 60.714
east = 23.012
# Create feature constraints, only spatial constraints are applied, while the other filters remain optional.
constraints = Constraints(bbox = (south, west, north, east))

# If want to do more filters with the constraint:
'''
constraints = Constraints(
    bbox = (south, west, north, east),
    observedProperty = "example_property",
    ontology = "example_ontology",
    country = "example_country",
    provider = "example_provider",
    etc...
)
'''

## 01 GET FEATURES
# 01.1: Retrieve features matching the previously defined constraints (only bbox).
features = client.get_features(constraints)

# 01.2: (optional: Convert Features to DataFrame if needed).
features_df = client.features_to_df(features)
display(features_df)


## 02 GET OBSERVATIONS
# 02.1: Retrieve observations matching the previously defined constraints (only bbox).
observations = client.get_observations(constraints)

# 02.2: (or retrieve observations from a different constraints).
feature_used = features[4]
feature_id = feature_used.id
feature_constraints = Constraints(feature=feature_id)
observations_feature_indexing = client.get_observations(feature_constraints)

# 02.3: (optional: Convert Observations to DataFrame if needed)
observations_df = client.observations_to_df(observations_feature_indexing)
display(observations_df)


## 03 GET DATA POINTS
# 03.1: Get first observation with data points
obs_with_data = client.get_observation_with_data(observations_feature_indexing[0].id, begin="2025-01-01T00:00:00Z", end="2025-02-01T00:00:00Z")

# 03.2: (optional: Convert Observation Points to DataFrame if needed)
if obs_with_data:
    obs_points_df = client.points_to_df(obs_with_data)
    display(obs_points_df)
else:
    print("No observation data available for the requested time range.")

# 03.3: (optional: Example of Graphical Time-Series)
if obs_with_data:
    client.plot_observation(obs_with_data, "Example of Time-series, custom your own title")
else:
    print("No observation data available for the requested time range.")