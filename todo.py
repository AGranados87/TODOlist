def main():
    tasks = []

    while True:

        print("\n-----TO DO LIST-----")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = int(input("Choose an option, choom: "))

        if choice == 1:
            print()
            numbertask = int(input("How many tasks would you like to add? "))
            for i in range(numbertask):
                task = input("Enter the task: ")
                tasks.append({"Task: ": task, "done": False})
                print("Task added!")

        elif choice == 2:
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "done" if task["done"] else "Not Done!"
                print(f"{index + 1}. {task['Task: ']} - {status}")

        elif choice == 3:
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == 4:
            print("Exiting the TO-DO list.")
            break

        else:
            print("Invalid task. Try again!")


main()