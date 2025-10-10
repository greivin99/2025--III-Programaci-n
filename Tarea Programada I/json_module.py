import csv
import json
import os

def csv_to_json(csv_path, json_filename=None, campos=None, indent=2):
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        if campos:
            dataset = [
                {campo: row[campo] for campo in campos if campo in row}
                for row in reader
            ]
        else:
            dataset = [row for row in reader]
    
    json_path = json_filename or os.path.basename(csv_path).replace('.csv', '.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=indent, ensure_ascii=False)
    
    return json_path