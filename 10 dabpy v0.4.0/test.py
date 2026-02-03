from dabpy import *
from IPython.display import display

# Replace with your token and optional view (WHOS or HIS-Central)
token = "his_central-c3b9e0a1-5a3a-4182-8e20-5bd2bd98b3a4"  # replace with your actual token
view = "his-central" # replace with 'whos' or 'his-central'
client = DABClient(token=token, view=view)

# ----------------------------
# 2. DOWNLOAD DATA OBSERVATIONS (APPLICABLE ONLY FOR HIS-CENTRAL SERVER *AT THE MOMENT*)
# ----------------------------
'''--------- 00 DEFINE THE CONSTRAINTS ---------'''
# 00.1: Define bounding box coordinates (or you can use from previous one)
south_2 = 41.777
west_2 = 12.392
north_2 = 41.832
east_2 = 12.456
# 00.2: Create New DownloadConstraints
download_constraints = DownloadConstraints(
    bbox = (south_2, west_2, north_2, east_2),
    # if use from previous define constraints --> base_constraints = constraints,
    asynchDownloadName = "download_example_last-try-3" # Name the downloaded file is mandatory
)
download_id = "alun.putra@edu.unifi.it:ac3d9db5-1096-4aec-8aa0-eeb3b4879b65"
delete_resp = client.delete_download(download_id)
print(delete_resp)