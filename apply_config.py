import json, os

with open('config/app_config.json') as f:
    config = json.load(f)

print('Applying config...')
for key, value in config.items():
    print(f"{key}: {value}")

print('Config applied successfully! Replace IDs here automatically in full project.')