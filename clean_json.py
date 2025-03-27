import json
import pandas as pd

# Open the JSONL file and load it line by line
input_path = input("Enter the path to the JSONL file: ")

with open(f"{input_path}eval_predictions.jsonl", "r") as file:
    data = [json.loads(line) for line in file]

# Flatten the JSON structure
flattened_data = []
for item in data:
    # Flatten the nested 'predicted_scores' into separate columns
    flat_item = item.copy()
    predicted_scores = flat_item.pop('predicted_scores', [])
    for i, score in enumerate(predicted_scores):
        flat_item[f'predicted_score_{i}'] = score
    flattened_data.append(flat_item)

# Convert to a DataFrame
df = pd.DataFrame(flattened_data)

# Save the DataFrame to a CSV file
output_file_name = input("Enter the name of the output file: ")
df.to_csv(f"{input_path}{output_file_name}.csv", index=False)
