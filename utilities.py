from uuid import uuid4

# Variables
UUID_MAX_LENGTH = 60

# Functions
def generateID(data):
    """
    Returns a JSON Object with UUID
    """
    return data | {"_id": str(uuid4())}


def string_to_tuple(string):
    """
    Converts a string to tuple
    """
    return (string, string)


def list_to_iterable_tuple_list(list):
    """
    Converts a list to a list of tuples
    """
    items = []
    for item in list:
        items.append(string_to_tuple(item))
    return items
