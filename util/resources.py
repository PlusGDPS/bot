from json import load

with open ("config.json", "r") as config_file:
    config_data = load(config_file)
    TOKEN = config_data["token"]
    GITHUB_TOKEN = config_data["github_token"]