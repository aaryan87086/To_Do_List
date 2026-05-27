import sqlite3

conn = sqlite3.connect("to_do.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tasks TEXT,
    status TEXT
)
""")
conn.commit()

while True:
    print("\n1. ✅ Add Task")
    print("2. 🔍 View Task")
    print("3. ❌ Delete Task")
    print("4. 🚪 Exit")

    choice = input("Enter Your Choice :")

    if choice == "1":
        task = input("Enter New Task :")
        cursor.execute("""INSERT INTO tasks(tasks,status) VALUES(?,?)""", (task , "Pending"))
        conn.commit()
        print("Task Added Successfully")
    
    elif choice == "2":
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        if not rows:
            print("No Task Available!")
        else:
            print("\nYour Tasks: \n")

            for row in rows:
                print(row[0], "-" , row[1], "-" ,row[2])

    elif choice == "3":
        cursor.execute("SELECT * FROM tasks")
        rows =  cursor.fetchall()


        if not rows:
            print("No tasks to delete")
        else:
            print("\n Your Tasks")
            
            for row in rows:
                print(row[0], "-" , row[1])

            delete_id = int(input("Enter Number of Task to delete :"))
            cursor.execute("DELETE FROM tasks WHERE id = ?", (delete_id,))
            conn.commit()
            print("Task Deleted Successfully")
     
    elif choice == "4":
        print("GoodBye!")
        conn.close()
        break

    else:
        print("Invalid Choice! Please enter 1-4. ")