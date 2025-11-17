from flask import Blueprint, render_template, current_app, request, redirect, url_for
import json
import os

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/organizations", methods=["GET", "POST"])
def organizations():
    json_path = os.path.join(current_app.root_path, "organizations.json")

    with open(json_path, "r") as f:
        organizations = json.load(f)

    # Command to delete
    delete_org_id = request.args.get("org_id")
    command = request.args.get("command")
    if command == "delete" and delete_org_id:
        updated_organizations = []
        for org in organizations:
            if org["org_id"] != delete_org_id:
                updated_organizations.append(org)
        organizations = updated_organizations
        with open(json_path, "w") as f:
            json.dump(organizations, f, indent=4)
        return redirect(url_for("pages.organizations"))

    # To add data
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        role = request.form.get("role", "").strip()
        if not name or not email or not role:
            return "<p>Error: All fields must be filled in!</p><p><a href='/organizations'>Back</a></p>"
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
        return redirect(url_for("pages.organizations"))

    #Body of HTML
    body = "<h1>Organizations</h1>"
    body += '<p><a href="/">Back to Home</a></p>'
    body += '<h2>List of the Organizations</h2>'
    #The table list
    body += "<table>"
    body += "<thead><tr><th>ID</th><th>Name</th><th>Email</th><th>Role</th><th>Manage</th></tr></thead><tbody>"
    for org in organizations:
        delete_url = f"/organizations?command=delete&org_id={org['org_id']}"
        body += "<tr>"
        body += f"<td>{org['org_id']}</td>"
        body += f"<td>{org['name']}</td>"
        body += f"<td>{org['email']}</td>"
        body += f"<td>{org['role']}</td>"
        body += (f"<td>"
                 f"<button onclick=\"if(confirm('Are you sure you want to delete {org['name']}?')){{location.href='{delete_url}'}}\">Delete</button>"
                 f"</td>")
        body += "</tr>"
    body += "</tbody></table>"
    #Add form
    body += """
    <h2>Add New Organization</h2>
    <form method="post">
        <table>
            <tr>
                <td><label for="name">Name:</label></td>
                <td><input type="text" id="name" name="name"></td>
            </tr>
            <tr>
                <td><label for="email">Email:</label></td>
                <td><input type="email" id="email" name="email"></td>
            </tr>
            <tr>
                <td><label for="role">Role:</label></td>
                <td><select id="role" name="role">
                    <option value="Publisher">Publisher</option>
                    <option value="Originator">Originator</option>
                    </select></td>
            </tr>
            <tr>
                <td colspan="2">
                    <input type="submit" value="Add Organization"
                        onclick="if(!this.form.name.value.trim() || !this.form.email.value.trim() || !this.form.role.value.trim()){alert('Error: All fields must be filled in!'); return false;}">
                </td>
            </tr>
        </table>
    </form>
    """

    # Use external CSS only
    html = f"<html><head><title>Flask Project - Organizations</title>" \
           f"<link rel='stylesheet' href='{url_for('static', filename='styles.css')}'>" \
           f"</head><body>{body}</body></html>"
    return html

@bp.route("/datasets", methods=["GET", "POST"])
def datasets():
    datasets_path = os.path.join(current_app.root_path, "datasets.json")
    orgs_path = os.path.join(current_app.root_path, "organizations.json")

    with open(datasets_path, "r") as f:
        datasets = json.load(f)
    with open(orgs_path, "r") as f:
        organizations = json.load(f)

    # Command to delete
    delete_name = request.args.get("delete")
    command = request.args.get("command")
    if command == "delete" and delete_name:
        new_datasets = []
        for dts in datasets:
            if dts["name"] != delete_name:
                new_datasets.append(dts)
        datasets = new_datasets
        with open(datasets_path, "w") as f:
            json.dump(datasets, f, indent=4)
        return redirect(url_for("pages.datasets"))

    #Add dataset
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        observed = request.form.get("observed", "").strip()
        year = request.form.get("year", "").strip()
        organization_id = request.form.get("organization_id", "").strip()

        if not name or not observed or not year or not organization_id:
            return "<p>Error: All fields are required!</p><p><a href='/datasets'>Back</a></p>"

        new_data = {
            "name": name,
            "observed": observed,
            "year": year,
            "organization_id": organization_id
        }

        datasets.append(new_data)
        with open(datasets_path, "w") as f:
            json.dump(datasets, f, indent=4)
        return redirect(url_for("pages.datasets"))

    #Body of HTML
    body = "<h1>Datasets</h1>"
    body += '<p><a href="/">Back to Home</a></p>'
    body += '<h2>List of the Datasets</h2>'
    #The table list
    body += "<table>"
    body += "<thead><tr><th>Dataset Name</th><th>Observed Data</th><th>Year</th><th>Org_ID</th><th>Manage</th></tr></thead><tbody>"
    for dts in datasets:
        delete_url = f"/datasets?command=delete&delete={dts['name']}"
        body += "<tr>"
        body += f"<td>{dts['name']}</td>"
        body += f"<td>{dts['observed']}</td>"
        body += f"<td>{dts['year']}</td>"
        body += f"<td>{dts['organization_id']}</td>"
        body += (f"<td>"
                 f"<button onclick=\"if(confirm('Are you sure you want to delete {dts['name']}?')){{location.href='{delete_url}'}}\">Delete</button>"
                 f"</td>")
        body += "</tr>"
    body += "</tbody></table>"

    #Add form
    body += """
    <h2>Add New Dataset</h2>
    <form method="post">
        <table>
            <tr>
                <td><label for="name">Dataset Name:</label></td>
                <td><input type="text" id="name" name="name"></td>
            </tr>
            <tr>
                <td><label for="observed">Observed Data:</label></td>
                <td><input type="text" id="observed" name="observed"></td>
            </tr>
            <tr>
                <td><label for="year">Year:</label></td>
                <td><input type="number" id="year" name="year"></td>
            </tr>
            <tr>
                <td><label for="organization_id">Organization ID:</label></td>
                <td><select id="organization_id" name="organization_id">
    """
    for org in organizations:
        body += f"<option value='{org['org_id']}'>{org['org_id']} — {org['name']}</option>"
    body += """
                    </select></td>
            </tr>
            <tr>
                <td colspan="2">
                    <input type="submit" value="Add Datasets"
                        onclick="if(!this.form.name.value.trim() || !this.form.observed.value.trim() || !this.form.year.value.trim()){alert('Error: All fields must be filled in!'); return false;}">
                </td>
            </tr>
        </table>
    </form>
    """

    style = """
    <style>
        table { border-collapse: collapse; width: 80%; margin: 20px 0; }
        th, td { border: 1px solid #333; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
    </style>
    """

    html = f"<html><head><title>Flask Project - Datasets</title>{style}</head><body>{body}</body></html>"
    return html