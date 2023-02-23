def create_search_options(params):
    options = {}
    keys = params.keys()

    if "active" in keys:
        options["active"] = True if params["active"] == "true" else False
    if "gender" in keys:
        options["gender"] = params["gender"]
    # if "address-state":

    return options
