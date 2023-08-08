import json
from colorama import init, Fore, Style

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def main():
    # Initialize colorama on Windows to enable colored output
    init()

    file_path = "logins.json"
    data = load_json_file(file_path)

    if not data:
        print(f"Failed to load data from {file_path}.")
        return

    print(Fore.GREEN + "JSON Viewer for logins.json")
    print("--------------------------" + Style.RESET_ALL)

    for index, user in enumerate(data, 1):
        print(Fore.GREEN + f"User {index}:")
        print(f"  Username: {user['username']}")
        print(f"  Password: {user['password']}")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
