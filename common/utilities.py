from uuid import uuid4
from env import env

# http://127.0.0.1:8000
# Variables
UUID_MAX_LENGTH = 60

# Functions
def generateID():
    """
    Returns a UUID
    """
    return str(uuid4())


def appendID(data):
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


def createURL(path, query_params={}):
    """
    Returns the Host URL
    """
    query_string = ""
    if query_params:
        query_string = "?"
        for param in query_params:
            query_string = f"{query_string}{'&' if len(query_string) != 1 else ''}{param}={query_params[param]}"
    return f'{env("HOST")}/{path}{query_string}'
