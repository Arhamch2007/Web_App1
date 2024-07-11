def get_todos(filepath='chores.txt'):
    with open(filepath, 'r') as file:
        chores = file.readlines()
    return chores


def write_todos(chores_arg, filepath='chores.txt'):
    with open(filepath, 'w') as file:
            file.writelines(chores_arg)

