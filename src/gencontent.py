import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, content_root_dir, template_path, dest_root_dir, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)

        if os.path.isdir(from_path):
            generate_pages_recursive(from_path, content_root_dir, template_path, dest_root_dir, basepath)

        elif os.path.isfile(from_path) and from_path.endswith(".md"):
            relative_path = os.path.relpath(from_path, content_root_dir)
            name_without_ext = os.path.splitext(relative_path)[0]

            if name_without_ext.endswith("index"):
                dest_dir = os.path.join(dest_root_dir, os.path.dirname(name_without_ext))
            else:
                dest_dir = os.path.join(dest_root_dir, name_without_ext)

            dest_path = os.path.join(dest_dir, "index.html")
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            generate_page(from_path, template_path, dest_path, basepath)



def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    # Apply basepath replacements to the template BEFORE inserting title/content
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Adjust internal asset and link paths in the markdown-generated HTML
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    title = extract_title(markdown_content, from_path)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as to_file:
        to_file.write(template)



def extract_title(md, file_path="(unknown)"):
    lines = md.split("\n")
    for line in lines:
        stripped = line.lstrip()
        print(f"Checking line in {file_path}: '{line.rstrip()}' | Stripped: '{stripped.rstrip()}'")
        
        # Debug: print raw bytes and ord values for the stripped line
        print(f"  Raw bytes: {list(stripped.encode('utf-8'))}")
        print(f"  Unicode codepoints: {[ord(c) for c in stripped]}")

        if stripped.startswith("# "):
            return stripped[2:].strip()
    raise ValueError(f"No title found in: {file_path}")

