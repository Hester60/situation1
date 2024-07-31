""""
Main file
"""

from types import MappingProxyType
from operations import addition, subtraction, division, multiplication

# Immutable dictionary
OPERATION_TYPE = MappingProxyType({
    0: 'addition',
    1: 'subtraction',
    2: 'multiplication',
    3: 'division',
})

# Mapping of operation and associated function
OPERATION_FUNCTIONS = {
    'addition': addition,
    'subtraction': subtraction,
    'multiplication': multiplication,
    'division': division,
}


def get_operation_choice():
    """
    Ask user to select an operation.

    Returns:
        Operation type (division, subtraction...).
    """
    print("Select the type of the operation by pressing the number:")

    for code, name in OPERATION_TYPE.items():
        print(f"{code}: {name}")

    try:
        user_input = int(input())
        if user_input in OPERATION_TYPE:
            return OPERATION_TYPE[user_input]
        else:
            print("Invalid selection. Please enter an existing number.")
            return get_operation_choice()
    except ValueError:
        print("Invalid selection. Please enter an existing number.")
        return get_operation_choice()


def ask_for_number(is_first_number=False):
    """
    Ask user to enter a number

    Args:
        is_first_number (bool): set "first" or "second" into the prompt.

    Returns:
        The selected number.
    """
    number_name = 'first'

    if not is_first_number:
        number_name = 'second'

    try:
        selected_number = int(input(f"Enter the {number_name} number: "))
        return selected_number
    except ValueError:
        print("Invalid selection. Please enter a number.")
        return ask_for_number(is_first_number)


def init():
    """
    Start the calculator in an infinite loop.
    """
    print("Welcome. Press CTRL+C to stop.\n")

    while True:
        selected_operation = get_operation_choice()
        print(f"You've selected: {selected_operation}")

        a = ask_for_number(True)
        b = ask_for_number()

        operation_function = OPERATION_FUNCTIONS[selected_operation]
        result = operation_function(a, b)
        print(f"The result is: {result}\n")


if __name__ == '__main__':
    try:
        init()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
