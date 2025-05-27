import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    # content_root_dir is dir_path_content
    # we start from the top of the content tree
    generate_pages_recursive(
        dir_path_content,       # current dir to process
        dir_path_content,       # root of content  
        template_path,          # template file
        dir_path_public,        # destination directory - you're missing this!
        basepath                # basepath
    )

main()
