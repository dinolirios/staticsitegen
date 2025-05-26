import os

content_dir = "/home/fachow/workspace/staticsitegen/content"  # replace with your actual content directory path

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                lines = f.readlines()
                has_title = any(line.lstrip().startswith("# ") for line in lines)
            if not has_title:
                print(f"No title found in: {path}")
