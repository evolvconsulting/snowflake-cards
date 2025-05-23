import json
import csv
from uuid import uuid4


def assign_ids_and_flatten(hierarchy, parent_id=None):
    # List to store flattened data
    flat_data = []

    for node in hierarchy:
        # Generate a unique ID for the current node
        node_id = str(uuid4())

        # Create the row for CSV
        row = {
            "id": node_id,
            "parentId": parent_id if parent_id else "",
            "name": node["name"],
            "title": node["title"],
            "type": node["type"],
        }
        flat_data.append(row)

        # Recursively process children
        if "children" in node and node["children"]:
            child_data = assign_ids_and_flatten(node["children"], node_id)
            flat_data.extend(child_data)

    return flat_data


def json_to_csv_hierarchy(json_file_path, csv_file_path):
    # Read JSON file
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        hierarchy = json.load(json_file)

    # Flatten the hierarchy and assign IDs
    flat_data = assign_ids_and_flatten(hierarchy)

    # Write to CSV file
    with open(csv_file_path, "w", encoding="utf-8", newline="") as csv_file:
        fieldnames = ["id", "parentId", "name", "title", "type"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flat_data)


# Example usage
if __name__ == "__main__":
    json_file_path = "public/hierarchy.json"
    csv_file_path = "public/hierarchy.csv"
    json_to_csv_hierarchy(json_file_path, csv_file_path)
