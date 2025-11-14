class Dataset:
    def __init__(self, name, observed, year, organization):
        self.name = name
        self.observed = observed
        self.year = year
        self.organization = organization

    def describe(self):
        print(f"Dataset: {self.name}")
        print(f"Observed Property: {self.observed}")
        print(f"Year: {self.year}")
        print(f"Organization: {self.organization.name} ({self.organization.org_id})")

    def to_dict(self):
        return {
            "name": self.name,
            "observed": self.observed,
            "year": self.year,
            "organization_id": self.organization.org_id
        }

    def from_dict(data, organizations):
        org_id = data["organization_id"]
        organization = next((org for org in organizations if org.org_id == org_id), None)
        if organization is None:
            organization = Organization("Unknown", "unknown@email.com", "Unknown")
        return Dataset(data["name"], data["observed"], data["year"], organization)