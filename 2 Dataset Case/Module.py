def add_org(organizations, org):
    organizations.append(org)
    print(f"Organization '{org.name}' added successfully with ID {org.org_id}.")

def add_dts(datasets, dts):
    datasets.append(dts)
    print(f"Dataset '{dts.name}' added successfully (Organization: {dts.organization.org_id}).")

def show_org(organizations):
    if not organizations:
        return "No organizations available."
    result = "\nOrganizations:\n"
    for org in organizations:
        result += f"{org.org_id}: {org.name} ({org.role})\n"
    return result

def show_org_details(organizations):
    if not organizations:
        print("\nNo organizations available.")
        return

    print(show_org(organizations), end="")
    choice = input("Enter Organization ID to view details (or 0 to go back): ").strip()

    if choice == "0":
        return

    org = next((o for o in organizations if o.org_id == choice), None)
    if org:
        print()
        org.describe()
    else:
        print("Invalid Organization ID.")

def show_dts(datasets):
    if not datasets:
        return "No datasets available."
    result = "\nDatasets:\n"
    for i, dts in enumerate(datasets, start=1):
        result += f"{i}. {dts.name} (Organization: {dts.organization.org_id})\n"
    return result

def show_dts_details(datasets):
    if not datasets:
        print("\nNo datasets available.")
        return

    print(show_dts(datasets), end="")
    choice = input("Select number to view details (0 to go back): ").strip()

    if not choice.isdigit():
        print("Invalid input. Enter a number.")
        return

    choice = int(choice)
    if choice == 0:
        return
    if 1 <= choice <= len(datasets):
        print()
        datasets[choice - 1].describe()
    else:
        print("Invalid dataset number.")

def update_org(organizations):
    if not organizations:
        print("\nNo organizations available to update.")
        return

    print(show_org(organizations), end="")
    choice = input("Enter Organization ID to update (0 to go back): ").strip()
    if choice == "0":
        return

    org = next((o for o in organizations if o.org_id == choice), None)
    if not org:
        print("Invalid Organization ID.")
        return

    print(f"\nUpdating '{org.name}' (press Enter to keep current value)")
    new_name = input(f"New Name [{org.name}]: ").strip()
    new_email = input(f"New Email [{org.email}]: ").strip()
    new_role = input(f"New Role [{org.role}]: ").strip()

    if new_name:
        org.name = new_name
    if new_email:
        org.email = new_email
    if new_role:
        org.role = new_role

    print(f"Organization '{org.name}' updated successfully.")

def update_dts(datasets, organizations):
    if not datasets:
        print("\nNo datasets available to update.")
        return

    print(show_dts(datasets), end="")
    choice = input("Select dataset number to update (0 to go back): ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return

    choice = int(choice)
    if choice == 0:
        return
    if not (1 <= choice <= len(datasets)):
        print("Invalid number.")
        return

    dts = datasets[choice - 1]
    print(f"\nUpdating '{dts.name}' (press Enter to keep current value)")

    new_name = input(f"New Name [{dts.name}]: ").strip()
    new_observed = input(f"New Observed Property [{dts.observed}]: ").strip()
    new_year = input(f"New Year [{dts.year}]: ").strip()

    print("\nEnter new Organization ID (press Enter to keep current):")
    print(show_org(organizations), end="")
    org_id = input("Organization ID: ").strip()

    if new_name:
        dts.name = new_name
    if new_observed:
        dts.observed = new_observed
    if new_year:
        dts.year = new_year
    if org_id:
        org = next((o for o in organizations if o.org_id == org_id), None)
        if org:
            dts.organization = org
        else:
            print("Invalid Organization ID. Organization not changed.")

    print(f"Dataset '{dts.name}' updated successfully.")

def remove_org(organizations):
    if not organizations:
        print("\nNo organizations available to remove.")
        return

    print(show_org(organizations), end="")
    choice = input("Enter Organization ID to remove (0 to go back): ").strip()
    if choice == "0":
        return

    org = next((o for o in organizations if o.org_id == choice), None)
    if org:
        organizations.remove(org)
        print(f"Organization '{org.name}' removed successfully.")
    else:
        print("Invalid Organization ID.")

def remove_dts(datasets):
    if not datasets:
        print("\nNo datasets available to remove.")
        return

    print(show_dts(datasets), end="")
    choice = input("Select dataset number to remove (0 to go back): ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return

    choice = int(choice)
    if choice == 0:
        return
    if 1 <= choice <= len(datasets):
        removed = datasets.pop(choice - 1)
        print(f"Dataset '{removed.name}' removed successfully.")
    else:
        print("Invalid number.")