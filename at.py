import json
import requests
import time
from colorama import Fore, Style, init

init(autoreset=True)

def print_help(topic):
    helps = {
        "base_url": [
            "http://localhost:5000",
            "https://api.mycompany.com",
            "https://jsonplaceholder.typicode.com"
        ],
        "method": ["GET", "POST", "PUT", "DELETE", "PATCH"],
        "route": ["/api/users", "/api/login", "/status"],
        "header": ['{"Accept": "application/json"}', '{"Authorization": "Bearer xyz"}'],
        "body": ['{}', '{"username": "max", "password": "secret"}'],
        "count": ["e.g. 1", "e.g. 5", "Any positive number"]
    }
    print(Fore.MAGENTA + f"Help: Possible options for {topic}:" + Style.RESET_ALL)
    for item in helps.get(topic, []):
        print("  " + item)

def input_with_help(prompt, topic, default=None):
    while True:
        inp = input(Fore.BLUE + prompt + (f" (default: {default})" if default else "") + " (? for help): " + Style.RESET_ALL).strip()
        if inp == "?":
            print_help(topic)
            continue
        if inp == "" and default is not None:
            return default
        return inp

def input_json_with_help(prompt):
    while True:
        raw = input(Fore.BLUE + prompt + " (JSON, empty = {} | ? for help): " + Style.RESET_ALL).strip()
        if raw == "?":
            # Choose which help topic depending on prompt text
            if "Header" in prompt:
                print_help("header")
            else:
                print_help("body")
            continue
        if raw == "":
            return {}
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            print(Fore.RED + "Invalid JSON, please try again." + Style.RESET_ALL)

def main():
    print(Fore.GREEN + "=== Automated API Testing Tool (at) ===" + Style.RESET_ALL)

    base_url = input_with_help("Base URL", "base_url", "http://localhost:5000")
    method = input_with_help("HTTP Method (GET, POST, PUT, DELETE, PATCH)", "method", "POST").upper()
    route = input_with_help("Route (e.g. /api/users)", "route", "/")
    headers = input_json_with_help("Enter Headers")
    body = input_json_with_help("Enter Body")

    while True:
        count_str = input(Fore.BLUE + "Number of requests (? for help): " + Style.RESET_ALL).strip()
        if count_str == "?":
            print_help("count")
            continue
        if count_str.isdigit() and int(count_str) > 0:
            count = int(count_str)
            break
        print(Fore.RED + "Please enter a positive integer." + Style.RESET_ALL)

    url = base_url.rstrip("/") + route

    for i in range(count):
        print(Fore.YELLOW + f"\nSending request {i+1} to {url} ..." + Style.RESET_ALL)
        start = time.time()
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, params=body)
            else:
                response = requests.request(method, url, headers=headers, json=body)
        except Exception as e:
            print(Fore.RED + f"Request error: {e}" + Style.RESET_ALL)
            continue
        duration = time.time() - start
        print(Fore.CYAN + f"Status: {response.status_code} ({duration:.3f}s)" + Style.RESET_ALL)
        try:
            print(json.dumps(response.json(), indent=2))
        except Exception:
            print(response.text)

if __name__ == "__main__":
    main()
