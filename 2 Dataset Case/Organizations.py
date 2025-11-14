class Organization:
    next_id = 1

    def __init__(self, name, email, role):
        self.org_id = f"ORG{Organization.next_id:04d}"
        Organization.next_id += 1
        self.name = name
        self.email = email
        self.role = role
        self.datasets = []

    def add_dataset(self, dataset):
        self.datasets.append(dataset)

    def describe(self):
        print(f"Organization ID: {self.org_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")
        print(f"Datasets: {len(self.datasets)}")
        if self.datasets:
            for d in self.datasets:
                print(f"  - {d.name}")
        else:
            print("No datasets yet.")

    def to_dict(self):
        return {
            "org_id": self.org_id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
        }

    def from_dict(data):
        org = Organization(data["name"], data["email"], data["role"])
        org.org_id = data.get("org_id", f"ORG{Organization.next_id:04d}")
        if "org_id" in data and data["org_id"].startswith("ORG"):
            try:
                num = int(data["org_id"][3:])
                if num >= Organization.next_id:
                    Organization.next_id = num + 1
            except:
                pass
        return org