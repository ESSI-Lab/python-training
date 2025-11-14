from Datasets import Dataset
from Organizations import Organization
from Storage import Storage
import Module as mo

storage = Storage()
organizations = storage.load_organizations()
datasets = storage.load_datasets(organizations)

while True:
    print("\nChoose between these options:")
    print("1. Edit Organizations")
    print("2. Edit Datasets")
    print("3. Save")
    print("4. Exit")
    option = input("Write the option you want: ").strip()

    if option == "1":
        while True:
            print("\nChoose between these options:")
            print("1. Add New Organization")
            print("2. Show Organizations")
            print("3. Update Organization")
            print("4. Delete Organization")
            print("0. Back to Main Menu")
            sub_option = input("Write the option you want: ").strip()

            if sub_option == "1":
                print("\nEnter organization details:")
                name = input("Name: ").strip()
                email = input("Email: ").strip()
                role = input("Role (Publisher / Originator): ").strip()

                if not name or not email or not role:
                    print("All fields are required.")
                else:
                    org = Organization(name, email, role)
                    mo.add_org(organizations, org)

            elif sub_option == "2":
                mo.show_org_details(organizations)

            elif sub_option == "3":
                mo.update_org(organizations)

            elif sub_option == "4":
                mo.remove_org(organizations)

            elif sub_option == "0":
                break

            else:
                print("Invalid option, please try again.")

    elif option == "2":
        while True:
            print("\nChoose between these options:")
            print("1. Add New Dataset")
            print("2. Show Datasets")
            print("3. Update Datasets")
            print("4. Delete Datasets")
            print("0. Back to Main Menu")
            sub_option = input("Write the option you want: ").strip()

            if sub_option == "1":
                if not organizations:
                    print("\nNo organizations found. Please add one first.")
                    continue

                print("\nEnter dataset details:")
                name = input("Name: ").strip()
                observed = input("Observed Property: ").strip()
                year = input("Year: ").strip()

                print("\nAvailable Organizations:")
                for org in organizations:
                    print(f"{org.org_id}: {org.name} ({org.role})")

                org_id = input("Enter Organization ID for this dataset: ").strip()
                organization = next((o for o in organizations if o.org_id == org_id), None)

                if organization is None:
                    print("Invalid Organization ID. Dataset not added.")
                    continue

                dataset = Dataset(name, observed, year, organization)
                organization.add_dataset(dataset)
                mo.add_dts(datasets, dataset)

            elif sub_option == "2":
                mo.show_dts_details(datasets)

            elif sub_option == "3":
                mo.update_dts(datasets, organizations)

            elif sub_option == "4":
                mo.remove_dts(datasets)

            elif sub_option == "0":
                break

            else:
                print("Invalid option, please try again.")

    elif option == "3":
        storage.save_organizations(organizations)
        storage.save_datasets(datasets)
        print("Data saved successfully. Goodbye!")

    elif option == "4":
        break

    else:
        print("Invalid option, please try again.")
