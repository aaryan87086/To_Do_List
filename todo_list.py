tasks = []
while True:
    print("\n1. ✅ Add Task")
    print("2. 🔍 View Task")
    print("3. ❌ Delete Task")
    print("4. 🚪 Exit")

    choice = input("Enter Your Choice :")

    if choice == "1":
        task = input("Enter New Task :")
        tasks.append(task)
        print(tasks)
        print("Task Added Successfully")
    
    elif choice == "2":
        if not tasks:
            print("No task Available")
        else:
            print("\nYour Tasks :")
            for i , task in enumerate(tasks):
                print(i+1 ,"-",task)

    elif choice == "3":
        if not tasks:
            print("No tasks to delete")
        else:
            print("\n Your Tasks")
            for i, task in enumerate(tasks):
                print(i+1 , "-" , task)
            delete_num = int(input("Enter Number of Task to delete"))
