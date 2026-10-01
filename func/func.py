def create_user(name="Unknown", *roles, **details):

    user = {
        "name": name,
        "roles": roles,
        "details": details
    }

    return user


result = create_user(
    "ewriq",
    "admin",
    "penci zorna",
    age=31,
    city="tr"
)


print(result)