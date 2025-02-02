import json

def save_to_file(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

def load_from_list():
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    todo = load_from_list()

    print("Welcome to your Todo List!")

    while True:
        print("\nHere are your options: ")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show list")
        print("4. Quit")

        option = input("\nEnter your option: ")

        if option == "1":
            print()

            task_num = int(input("How many tasks do you want to add? "))

            for i in range(task_num):
                task = input("Enter your task: ")
                todo.append(task)
                print(f"Task {task} added")
            save_to_file(todo)

        elif option == "2":
            index = 1
            for list in todo:
                print(f"{index}. {list}")
                index += 1
            remove = int(input("What task do you want to remove?" ))

            if 0 <= remove < len(todo):
                removed_task = todo.pop(remove)
                print(f"Tasked '{removed_task}' deleted")
                save_to_file(todo)
            else:
                print(f"Item '{remove}' is not in list")
        elif option == "3":
            if todo:
                print()
                index = 1 
                for list in todo:
                    print(f"{index}. {list}")
                    index += 1
            else:
                print("\nYour To-Do List is empty.")
        elif option == "4":
            print("Quitting..")
            break
if __name__ == "__main__":
    main()