def mask(*args):
    def decorator(func):
        def wrapper():
            client_details = func()
            for field in args:
                replace_field(client_details, field)
            return client_details
        return wrapper
    return decorator


def replace_with_stars(text):
    replaced_string = ""

    for char in text:
        if char == " ":
            replaced_string += " "
        else:
            replaced_string += "*"

    return replaced_string


def replace_field(input_dict, search_term):
    if search_term in input_dict:
        input_dict[search_term] = replace_with_stars(input_dict[search_term])
        return

    for term in input_dict.values():
        if isinstance(term, dict):
            replace_field(term, search_term)
