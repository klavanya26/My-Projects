import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='user',
            database='railway_db'
        )
        return connection
    except mysql.connector. Error as err:
        print(f"Error: {err}")
        return None

def add_train(train_number, name, type, capacity):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO trains (train_number, name, type, capacity) VALUES (%s, %s, %s, %s)"
            values = (train_number, name, type, capacity)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            print("Train added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            connection.close()

def get_trains():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM trains"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            connection.close()
    return []

def update_train(train_id, train_number, name, type, capacity):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "UPDATE trains SET train_number = %s, name = %s, type = %s, capacity = %s WHERE id = %s"
            values = (train_number, name, type, capacity, train_id)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            print("Train updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            connection.close()

def delete_train(train_id):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM trains WHERE id = %s"
            values = (train_id,)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            print("Train deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            connection.close()

def main():
    while True:
        print("\nRailway Management System Menu:")
        print("1. Add a train")
        print("2. View all trains")
        print("3. Update a train")
        print("4. Delete a train")
        print ("5. Exit")
        
        choice = input ("Enter your choice (1-5): ")
        
        if choice == '1':
            train_number = input ("Enter train number: ")
            name = input ("Enter train name: ")
            type = input ("Enter train type: ")
            capacity = int (input ("Enter train capacity: "))
            add_train (train_number, name, type, capacity)
        
        elif choice == '2':
            trains = get_trains ()
            print ("\nTrains in the system:")
            for train in trains:
                print(train)
        
        elif choice == '3':
            train_id = int (input ("Enter the ID of the train to update: "))
            train_number = input ("Enter new train number: ")
            name = input ("Enter new name: ")
            type = input ("Enter new type: ")
            capacity = int (input ("Enter new capacity: "))
            update_train (train_id, train_number, name, type, capacity)
        
        elif choice == '4':
            train_id = int (input ("Enter the ID of the train to delete: "))
            delete_train(train_id)
        
        elif choice == '5':
            print ("Exiting the program.")
            break
        
        else:
            print ("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main ()
