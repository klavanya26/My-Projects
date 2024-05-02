class PermitIssuer:
    def __init__(self):
        self.permits = {}

    def create_permit_application(self):
        permit_id = input("Enter permit ID: ")
        organizer_name = input("Enter organizer's name: ")
        demonstration_purpose = input("Enter demonstration purpose: ")
        location = input("Enter location: ")
        expected_attendance = input("Enter expected attendance: ")

        if permit_id not in self.permits:
            self.permits[permit_id] = {
                "Organizer's Name": organizer_name,
                "Demonstration Purpose": demonstration_purpose,
                "Location": location,
                "Expected Attendance": int(expected_attendance),
                "Status": "Pending"
            }
            print(f"Permit application with ID {permit_id} created successfully.")
        else:
            print("Permit application with the same ID already exists.")

    def read_permit_application(self, permit_id):
        if permit_id in self.permits:
            permit_details = self.permits[permit_id]
            print("Permit Application Details:")
            for key, value in permit_details.items():
                print(f"{key}: {value}")
        else:
            print("Permit application not found.")

    def update_permit_application(self, permit_id):
        if permit_id in self.permits:
            fields_to_update = {}
            for field in self.permits[permit_id]:
                new_value = input(f"Enter new value for {field} (or press Enter to skip): ")
                if new_value:
                    fields_to_update[field] = new_value
        
            if fields_to_update:
                for field, new_value in fields_to_update.items():
                    self.permits[permit_id][field] = new_value
                    print(f"Permit application with ID {permit_id} updated successfully.")
            else:
                print("No fields to update.")
        else:
            print("Permit application not found.")

    def delete_permit_application(self, permit_id):
        if permit_id in self.permits:
            del self.permits[permit_id]
            print(f"Permit application with ID {permit_id} deleted successfully.")
        else:
            print("Permit application not found.")

    def process_demonstration_permits(self, permit_id):
        if permit_id in self.permits:
            self.permits[permit_id]["Status"] = "Approved"
            print(f"Permit application with ID {permit_id} approved successfully.")
        else:
            print("Permit application not found.")
    
    def monitor_permit_compliance(self, compliance_id):
        if compliance_id not in self.permits:
            print("Record not found")
            return
        
        print(f"Monitoring compliance for permit with ID {compliance_id}.")

        expected_attendance = self.permits[compliance_id]["Expected Attendance"]
        if expected_attendance > 1000:
            print("Special force required")
        else:
            print("Special force not required")


permit_issuer = PermitIssuer()

while True:
    print("**********************")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Process")
    print("6. Monitor")
    print("7. Exit")
    print("Select appropriate option:")
    option = int(input())
    print("**********************")


    if option == 1:
        permit_issuer.create_permit_application()
    elif option == 2:
        permit_id = input("Enter permit ID to read: ")
        permit_issuer.read_permit_application(permit_id)
    elif option == 3:
        permit_id = input("Enter permit ID to update: ")
        permit_issuer.update_permit_application(permit_id)
    elif option == 4:
        permit_id = input("Enter permit ID to delete: ")
        permit_issuer.delete_permit_application(permit_id)
    elif option == 5:
        permit_id = input("Enter permit ID to process: ")
        permit_issuer.process_demonstration_permits(permit_id)
    elif option == 6:
        compliance_id = input("Enter compliance ID to monitor: ")
        permit_issuer.monitor_permit_compliance(compliance_id)
    elif option == 7:
        break
    else:
        print("Enter valid option")
