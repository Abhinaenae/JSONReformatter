import os
import json

def prettifyJSONFiles(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                try:
                    json_data = json.load(file)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {file_path}")
                    continue

            # Rewrite the JSON file with prettified contents
            with open(file_path, 'w') as file:
                json.dump(json_data, file, indent=4)
            print(f"Prettified JSON in file: {file_path}")

# Initialize 'folder_path' with the path to folder containing JSON files
folder_path = input("Enter the full path of the folder:\n")
prettifyJSONFiles(folder_path)

