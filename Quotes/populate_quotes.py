import requests
import json
import os

def fetch_quotes_and_append_to_json(num_quotes, filename):
    quotes = []

    # load existing quotes if the file exists and is not empty
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as file:
            try:
                quotes = json.load(file)
            except json.JSONDecodeError:
                print(f"Error: {filename} contains invalid JSON data.")

    # fetch new quotes and append them to the existing list
    for _ in range(num_quotes):
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            quote = data["content"]
            author = data["author"]
            quotes.append({"quote": quote, "author": author})
        else:
            print("Failed to fetch a quote.")

    # write the combined list of quotes back to the file
    with open(filename, "w") as file:
        json.dump(quotes, file, indent=4)

# example usage:
num_quotes_to_fetch = 1
json_filename = "Quotes/inspirational_from_quotable.json"
fetch_quotes_and_append_to_json(num_quotes_to_fetch, json_filename)
