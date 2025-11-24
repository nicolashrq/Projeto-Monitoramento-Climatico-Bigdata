def save_json(path, data):
    import json
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
