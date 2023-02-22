def create_search_options(params):
    options = {}

    if params["active"]:
        options["active"] = True if params["active"] == "true" else False
    if params["gender"]:
        options["gender"] = params["gender"]

    return options
