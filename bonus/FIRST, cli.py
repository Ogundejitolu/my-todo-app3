from bonus.functions import get_todos, write_todos
import time
now = time.strftime("%H:%M:%S %Y-%m-%d ")
print("The time is", now)
while True:
    user_action = input("Enter add, show, edit, remove or exit: ")
    user_action = user_action.strip()
    user_action = user_action.strip('.')
    user_action = user_action.strip('-')

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)
        user_action = user_action[4:]
        message = f'{user_action.capitalize()} was added to the list.'
        print(message)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index + 1}.{items}"
            print(row.capitalize())
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:])
            todos = get_todos()
            user_number = todos[number - 1].strip('\n')
            message = f'{user_number.capitalize()} is going to be edited.'
            print(message)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            message = f'{todos} is the edited list.'
            print(message)

            write_todos(todos)
        except IndexError:
            print('Number to be edited is unavailable')
    elif user_action.startswith("remove"):
        try:
            number = int(user_action[6:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)

            message = f'{todo_to_remove.capitalize()} was removed from the list'
            print(message)
        except IndexError:
            print('There is no todo with that number')

    elif user_action.startswith("exit"):
        break
    else:
        print('INVALID COMMAND!!!')
        print("Try again.")
print("Bye")
