from dabpy import *
from IPython.display import display

# Replace with your token and optional view (WHOS or HIS-Central)
token = "his_central-c3b9e0a1-5a3a-4182-8e20-5bd2bd98b3a4"  # replace with your actual token
view = "his-central" # replace with 'whos' or 'his-central'
client = DABClient(token=token, view=view)

'''--------- 00 DEFINE THE CONSTRAINTS ---------'''
# 00.1: Define bounding box coordinates (or you can use from previous one)
south_2 = 43.767
west_2 = 11.250
north_2 = 43.781
east_2 = 11.263
# 00.2: Create New DownloadConstraints
download_constraints = DownloadConstraints(
    bbox = (south_2, west_2, north_2, east_2),
    # if use from previous define constraints --> base_constraints = constraints,
    asynchDownloadName = "download_example-FI-3-02022026" # Name the downloaded file is mandatory
)

create_save_resp = client.create_save_download(download_constraints)