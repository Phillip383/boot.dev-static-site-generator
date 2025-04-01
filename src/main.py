from generation import *
from constants import *

def main():
    copy_dir(STATIC_DIR, PUBLIC_DIR)
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_PATH, PUBLIC_DIR)

if __name__ == "__main__":
    main()
