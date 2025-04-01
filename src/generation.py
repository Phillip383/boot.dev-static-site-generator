import os
import shutil
from markdowntohtml import extract_title, markdown_to_html_node

def copy_dir(source, destination):
    source_dir_content = os.listdir(source)
    # Remove the old content from the destination if it exists
    if os.path.exists(destination):
        shutil.rmtree(destination)

    # make the directory if one doesn't already exist.
    os.mkdir(destination)

    for d in source_dir_content:
        current_path = os.path.join(source, d)
        print(f"Copying: {current_path} to {destination}")
        if os.path.isdir(current_path):
            os.mkdir(os.path.join(destination, d))
            copy_dir(current_path, os.path.join(destination, d))
        else:
            #copy the file to the destination.
            shutil.copy(current_path, destination)

def generate_page(from_path, template_path, dest_path, base_path):
    dest_path = dest_path.replace(".md", ".html")
    print(f"From {from_path} to {dest_path} using {template_path}")
    
    md_file = open(from_path)
    html_file = open(template_path)
    
    markdown_doc = md_file.read()
    html_doc = html_file.read()
    
    md_file.close()
    html_file.close()

    html_doc = html_doc.replace("{{ Title }}", extract_title(markdown_doc))
    html_doc = html_doc.replace("{{ Content }}", markdown_to_html_node(markdown_doc).to_html())
    
    if base_path != "/":
        html_doc = html_doc.replace("href=\"/", f"href=\"{base_path}/")
        html_doc = html_doc.replace("src=\"/", f"src=\"{base_path}/")

    if os.path.exists(dest_path):
        dest_file = open(dest_path)
        dest_file.write(html_doc)
        dest_file.close()
    else:
        #create the directories leading up to the destination.
        if os.path.exists(dest_path[0:dest_path.rfind("/")]) == False:
            dirs = dest_path[0:dest_path.rfind("/")]
            os.makedirs(dirs)
        
        dest_file = open(dest_path, 'w')
        dest_file.write(html_doc)
        dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    contents = os.listdir(dir_path_content)
    for i in range(len(contents)):
        current_content_path = os.path.join(dir_path_content, contents[i])
        current_dest_path = os.path.join(dest_dir_path, contents[i])
        if os.path.isdir(current_content_path):
            generate_pages_recursive(current_content_path, template_path, current_dest_path, base_path)
        else:
            generate_page(current_content_path, template_path, current_dest_path, base_path)
