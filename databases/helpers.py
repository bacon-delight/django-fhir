def create_search_options(params):
    """
    Create search options with respect to query parameters
    """
    # Return Options
    options = {}

    keys = params.keys()
    if "active" in keys:
        options.update({"active": True if params["active"] == "true" else False})
    if "gender" in keys:
        options.update({"gender": params["gender"]})
    if "address-city" in keys:
        options.update({"address": {"$elemMatch": {"city": params["address-city"]}}})
    if "address-state" in keys:
        options.update({"address": {"$elemMatch": {"state": params["address-state"]}}})

    return options
