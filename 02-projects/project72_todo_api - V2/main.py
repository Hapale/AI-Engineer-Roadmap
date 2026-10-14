from todo_repository import TodoRepository
from todo_service import TodoService


repository = TodoRepository()
service = TodoService(repository)

def show_menu():
    print("=============================")
    print("       TODO MANAGER        ")
    print("=============================")
    print()
    print("1. Add Todo")
    print("2. Show Todos")
    print("3. Edit Todo")
    print("4. Search Todo")
    print("5. Delete Todo")
    print("0. Exit")
    print()

while True:

    show_menu()
    choice = input("Choose: ")

    #def choose_todo(service):
        #todos = service.get_all()

        #if not todos:
            #print("No todos found.")
            #return None

        #choice_number = int(input("Choose Todo number: "))

        #if choice_number < 1 or choice_number > len(todos):
            #print("Please choose a valid todo number.")
            #return None

        #return todos[choice_number - 1]

    if choice == "1":

        title = input("Enter Todo title: ")
        description = input("Enter Todo description: ")

        try:
            service.add(title, description)
            print("✓ Todo added successfully.")

        except ValueError as error:
            print(error)

    elif choice == "2":

        todos = service.get_all()

        if not todos :
            print("No todos found.")

        else:

            for index, todo in enumerate(todos, start=1):
                print(f"{index}. {todo.title}")

    elif choice == "3":

        try:

            choice_number = int(input("Choose Todo's number:"))
            todos = service.get_all()
            if choice_number < 1 or choice_number > len(todos):
                print("Please choose a valid todo number.")
            else:
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                selected_todo = todos[choice_number - 1]
                selected_todo.set_title(new_title)
                selected_todo.set_description(new_description)
                print("✓ Todo edited successfully.")

        except ValueError as error:
            print(error)

    elif choice == "4":

        try:

            todo = input("Enter keyword : ")
            results = service.search(todo)
            if not results :
                print ("Not found")
            else:

                for index, todo in enumerate(results, start=1):
                    print(f"{index}. {todo.title}")
                    print(f"   {todo.description}")
        
        
        except ValueError as error:
            print(error)
            



    elif choice == "5":

        try:

            choice_number = int(input("Choose Todo's number:"))
            todos = service.get_all()
            if choice_number < 1 or choice_number > len(todos):
                print("Please choose a valid todo number.")
            else:
                todo = todos[choice_number - 1]
                service.delete(todo)
                print("✓ Todo deleted successfully.")

        except ValueError as error:
            print(error)


    elif choice == "0":
        break
    else:
            print("Invalid choice")