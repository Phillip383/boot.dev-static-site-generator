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

def generate_page(from_path, template_path, dest_path):
    print(f"From {from_path} to {dest_path} using {template_path}")
    
    md_file = open(from_path)
    html_file = open(template_path)
    
    markdown_doc = md_file.read()
    html_doc = html_file.read()
    
    md_file.close()
    html_file.close()

    html_doc = html_doc.replace("{{ Title }}", extract_title(markdown_doc))
    html_doc = html_doc.replace("{{ Content }}", markdown_to_html_node(markdown_doc).to_html())

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


