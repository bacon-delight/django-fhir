def find_all(collection):
    return list(collection.find({}))


def insert_one(collection, document):
    collection.insert_one(document)
