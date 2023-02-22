from uuid import uuid4


def find_all(collection):
    """
    Returns all documents within the collection
    """
    return list(collection.find({}))


def insert_one(collection, document):
    """
    Insert ONE document into the collection
    """
    collection.insert_one(document)


def find_one(collection, options):
    """
    Finds and retrieves one document from the collection based on options
    """
    document = collection.find_one(options)
    if document:
        return document
    return None


def find_by(collection, options):
    """
    Finds and retrieves multiple document from the collection based on options
    """
    return list(collection.find(options))
