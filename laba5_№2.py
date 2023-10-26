def action(string):
    string = string.strip().capitalize()
    while string.endswith("?") or string.endswith("!"):
        string = string.rstrip("?")
        string = string.rstrip("!")
    return string + "."


print(action(input()))
