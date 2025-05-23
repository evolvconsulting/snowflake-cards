import csv
import json


def build_hierarchy(data):
    # Create a dictionary to store nodes by id
    nodes = {
        row["id"]: {
            "name": row["name"],
            "title": row["title"],
            "type": row["type"],
            "children": [],
        }
        for row in data
    }

    # Create the hierarchy
    root = []
    for row in data:
        node = nodes[row["id"]]
        parent_id = row["parentId"]
        if parent_id:  # If there's a parentId, add this node as a child
            if parent_id in nodes:
                nodes[parent_id]["children"].append(node)
        else:  # If no parentId, this is a root node
            root.append(node)

    return root


def csv_to_json_hierarchy(csv_file_path, json_file_path):
    # Read CSV file
    with open(csv_file_path, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Build hierarchy
    hierarchy = build_hierarchy(data)

    # Write to JSON file
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(hierarchy, json_file, indent=2)


# Example usage
if __name__ == "__main__":
    csv_file_path = "../public/hierarchy.csv"
    json_file_path = "../public/hierarchy.json"
    csv_to_json_hierarchy(csv_file_path, json_file_path)
