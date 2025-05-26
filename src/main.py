import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    # content_root_dir is dir_path_content
    # we start from the top of the content tree
    generate_pages_recursive(
        dir_path_content,       # current dir to process (start at root)
        dir_path_content,       # root of content (used to calculate relative paths)
        template_path,          # template file
        dir_path_public         # destination root
    )

main()
