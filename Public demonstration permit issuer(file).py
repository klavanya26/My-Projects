class PermitIssuer:
    def __init__(self):
        self.file_path = "fileDataStore.txt"
        self.permits = self.convertFileToDictionary()

    def convertFileToDictionary(self):
        try:
            with open(self.file_path, "r") as fileObj:
                return eval(fileObj.read())["store"]
        except FileNotFoundError:
            return []

    def insertIntoFile(self, currList):
        with open(self.file_path, "w") as fileObj:
            obj = {"store": currList}
            fileObj.write(str(obj))

    def isRecordPresentInDatabase(self, id):
        result = [-1, None]
        index = 0
        for obj in self.permits:
            if obj['permit_id'] == id:
                result[0] = index
                result[1] = obj
                break
            index += 1
        return result

    def create_permit_application(self):
        permit_id = input("Enter permit ID: ")
        organizer_name = input("Enter organizer's name: ")
        demonstration_purpose = input("Enter demonstration purpose: ")
        location = input("Enter location: ")
        expected_attendance = input("Enter expected attendance: ")

        result = self.isRecordPresentInDatabase(permit_id)
        print(result)
        if result[0] == -1:
            record = {
                "permit_id": permit_id,
                "Organizer's Name": organizer_name,
                "Demonstration Purpose": demonstration_purpose,
                "Location": location,
                "Expected Attendance": int(expected_attendance),
                "Status": "Pending"
            }
            self.permits.append(record)
            self.insertIntoFile(self.permits)
            print(f"Permit application with ID {permit_id} created successfully.")
        else:
            print("Permit application with the same ID already exists.")

    def read_permit_application(self, permit_id):
        for permit in self.permits:
            if permit['permit_id'] == permit_id:
                print("Permit Application Details:")
                for key, value in permit.items():
                    print(f"{key}: {value}")
                return
        print("Permit application not found.")

    def update_permit_application(self, permit_id):
        result = self.isRecordPresentInDatabase(permit_id)
        if result[0] != -1:
            fields_to_update = {}
            for field in result[1]:
                new_value = input(f"Enter new value for {field} (or press Enter to skip): ")
                if new_value:
                    fields_to_update[field] = new_value
        
            if fields_to_update:
                for field, new_value in fields_to_update.items():
                    result[1][field] = new_value
                self.insertIntoFile(self.permits)
                print(f"Permit application with ID {permit_id} updated successfully.")
            else:
                print("No fields to update.")
        else:
            print("Permit application not found.")

    def delete_permit_application(self, permit_id):
        result = self.isRecordPresentInDatabase(permit_id)
        if result[0] != -1:
            del self.permits[result[0]]
            self.insertIntoFile(self.permits)
            print(f"Permit application with ID {permit_id} deleted successfully.")
        else:
            print("Permit application not found.")

    def process_demonstration_permits(self, permit_id):
        result = self.isRecordPresentInDatabase(permit_id)
        if result[0] != -1:

            self.permits[result[0]]["Status"] = "Approved"
            self.insertIntoFile(self.permits)
            print(f"Permit application with ID {permit_id} approved successfully.")
        else:
            print("Permit application not found.")
    
    def monitor_permit_compliance(self, compliance_id):
        for permit in self.permits:
            if permit['permit_id'] == compliance_id:
                print(f"Monitoring compliance for permit with ID {compliance_id}.")
                expected_attendance = permit["Expected Attendance"]
                if expected_attendance > 1000:
                    print("Special force required")
                else:
                    print("Special force not required")
                return
        print("Record not found")

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
