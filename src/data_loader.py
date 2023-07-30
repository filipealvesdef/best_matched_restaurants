import csv
import os
from .domain import Restaurant, Cuisine

def load_data_from_csv():
    tables = [
        { 'filename': 'restaurants.csv', 'class': Restaurant },
        { 'filename': 'cuisines.csv', 'class': Cuisine },
    ]
    data = []

    for entity_mapping in tables:
        filename = entity_mapping['filename']
        cls = entity_mapping['class']
        filepath = os.path.join('data', filename)

        with open(filepath) as f:
            reader = csv.DictReader(f)
            for id, row in enumerate(reader, start=1):
                for k, v in row.items():
                    # convert all columns to integer, except 'name'
                    if k != 'name':
                        row[k] = int(v)

                # create 'id' field if not exists on table (e.g. restaurants)
                if 'id' not in row:
                    row['id'] = id

                data.append(cls(**row))
    return data
