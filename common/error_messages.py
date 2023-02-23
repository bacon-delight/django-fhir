def generate_error_message(data_definition=None):
    return (
        f"Provided value doesn't adhere to {data_definition}"
        if data_definition
        else "Invalid Value"
    )


def error_message_invalid_choice(data_definition=None):
    return (
        "invalid_choice",
        generate_error_message(data_definition=data_definition)
        if data_definition
        else "Invalid Choice",
    )
