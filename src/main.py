import textnode as tn
import os
import shutil

static_dir = "./static"
public_dir = "./public"

def main():
    copy_dir(static_dir, public_dir)

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

if __name__ == "__main__":
    main()