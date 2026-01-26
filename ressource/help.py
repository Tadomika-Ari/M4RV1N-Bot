def my_help() -> str:
    help_str = "-- /help --\n" \
    "to print all possible commands and the required role to use it\n" \
    "role required: None\n\n" \
    "-- /hello --\n" \
    "to print hello to the user\n" \
    "role required: None\n\n" \
    "-- /bio --\n" \
    "to print the marvin bio\n" \
    "role required: None\n\n" \
    "-- /create_tournament --\n" \
    "to create a tournament and stock it in a file\n" \
    "parameters: title (str), description (str), time (DD/MM/YY)"
    "role required: Organisateur\n\n"
    return help_str