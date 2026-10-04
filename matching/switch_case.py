command = "start"

match command:
    case "start":
        print("Starting")

    case "stop":
        print("Stopping")

    case "restart":
        print("Restarting")

    case _:
        print("Unknown command")