from flask import Flask, render_template, current_app, request
from flask_restx import Api, Resource, fields
import json, os

app = Flask(__name__)
api = Api(app,
          version="1.0",
          title="Organizations API",
          description="Documentation API Example",
          doc="/api/organizations")

# Namespace
ns = api.namespace("Organizations", description="Organizations Operations")

# JSON path helper
def get_json_path():
    return os.path.join(current_app.root_path, "organizations.json")

# HTML frontend
@app.route("/")
def index():
    print(">>> INDEX ROUTE CALLED")
    return "Hello World"

# GET/POST organizations
@ns.route("")
class OrganizationList(Resource):
    @ns.doc("list_organizations")
    def get(self):
        try:
            with open(get_json_path(), "r") as f:
                return json.load(f)
        except:
            return []

    @ns.doc("add_organization")
    def post(self):
        try:
            with open(get_json_path(), "r") as f:
                orgs = json.load(f)
        except:
            orgs = []

        data = request.get_json()
        if not all([data.get("name"), data.get("email"), data.get("role")]):
            api.abort(400, "All fields must be filled in!")

        last_id = max([int(o["org_id"][3:]) for o in orgs], default=0)
        new_id = f"ORG{last_id+1:04d}"
        new_org = {"org_id": new_id, **data}
        orgs.append(new_org)

        with open(get_json_path(), "w") as f:
            json.dump(orgs, f, indent=4)

        return {"message": "Organization added", "data": new_org, "all_data": orgs}, 201

# DELETE organization
@ns.route("/<string:org_id>")
@ns.param("org_id", "Organization ID")
class Organization(Resource):
    def delete(self, org_id):
        try:
            with open(get_json_path(), "r") as f:
                orgs = json.load(f)
        except:
            orgs = []

        updated = [o for o in orgs if o["org_id"] != org_id]
        if len(updated) == len(orgs):
            api.abort(404, f"No organization found with id {org_id}")

        with open(get_json_path(), "w") as f:
            json.dump(updated, f, indent=4)
        return {"message": f"Organization {org_id} deleted", "data": updated}

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)