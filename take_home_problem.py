import requests, json

api_key = None
with open("./auth.json") as auth_file:
    api_key = json.load(auth_file)["apiKey"]

headers = {
    "apiKey": api_key,
    "Accept": "application/json"
}

target_url = "https://api.myngp.com/v2/broadcastEmails"

response = requests.get(target_url, headers=headers)
email_objects = response.json()["items"]
num_emails = len(email_objects)

for obj in email_objects:
    print(obj["emailMessageId"], obj["name"], sep="\t")

print("\nTotal: {} emails".format(num_emails))