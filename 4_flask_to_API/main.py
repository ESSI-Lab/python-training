from flask import Flask, jsonify, request, current_app, render_template
import json
import os

app = Flask(__name__)

def get_json_path():
    return os.path.join(current_app.root_path, "organizations.json")

@app.route("/")
def index():
    return render_template("organizations.html")

# GET: to read data
@app.route("/organizations", methods=["GET"])
def get_organizations():
    json_path = get_json_path()
    with open(json_path, "r") as f:
        organizations = json.load(f)
    return jsonify(organizations)

# POST: to add data
@app.route("/organizations", methods=["POST"])
def add_organization():
    json_path = get_json_path()
    with open(json_path, "r") as f:
        organizations = json.load(f)

    data = request.get_json()
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    role = data.get("role", "").strip()
    if not name or not email or not role:
        return jsonify({"error": "All fields must be filled in!"}), 400
    # Auto-generate org_id like ORGXXXX
    if organizations:
        last_id = max(int(org["org_id"][3:]) for org in organizations)
    else:
        last_id = 0
    new_id = f"ORG{last_id + 1:04d}"

    new_org = {
        "org_id": new_id,
        "name": name,
        "email": email,
        "role": role
    }

    organizations.append(new_org)
    with open(json_path, "w") as f:
        json.dump(organizations, f, indent=4)

    return jsonify({"message": "Organization added", "data": new_org, "all_data": organizations})

# DELETE: to remove data
@app.route("/organizations/<org_id>", methods=["DELETE"])
def delete_organization(org_id):
    json_path = get_json_path()
    with open(json_path, "r") as f:
        organizations = json.load(f)

    updated_organizations = []
    for org in organizations:
        if org["org_id"] != org_id:
            updated_organizations.append(org)

    with open(json_path, "w") as f:
        json.dump(updated_organizations, f, indent=4)

    return jsonify({"message": f"Organization {org_id} deleted", "data": updated_organizations})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
