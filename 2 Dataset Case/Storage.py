import json
import os
from Organizations import Organization
from Datasets import Dataset

class Storage:
    def __init__(self, org_file="organizations.json", dts_file="datasets.json"):
        self.org_file = org_file
        self.dts_file = dts_file

    def load_organizations(self):
        if not os.path.exists(self.org_file):
            return []
        try:
            with open(self.org_file, "r") as f:
                data = json.load(f)
        except:
            print("Error reading organization file — starting empty.")
            return []

        organizations = [Organization.from_dict(d) for d in data]
        if organizations:
            last_id = max(int(org.org_id[3:]) for org in organizations)
            Organization.next_id = last_id + 1
        return organizations

    def save_organizations(self, organizations):
        with open(self.org_file, "w") as f:
            json.dump([org.to_dict() for org in organizations], f, indent=4)

    def load_datasets(self, organizations):
        if not os.path.exists(self.dts_file):
            return []
        try:
            with open(self.dts_file, "r") as f:
                data = json.load(f)
        except:
            print("Error reading dataset file — starting empty.")
            return []

        return [Dataset.from_dict(d, organizations) for d in data]

    def save_datasets(self, datasets):
        with open(self.dts_file, "w") as f:
            json.dump([d.to_dict() for d in datasets], f, indent=4)