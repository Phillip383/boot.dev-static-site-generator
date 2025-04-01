from generation import *
from constants import STATIC_DIR, PUBLIC_DIR

def main():
    copy_dir(STATIC_DIR, PUBLIC_DIR)
    generate_page('content/index.md', 'template.html', 'public/index.html')

if __name__ == "__main__":
    main()
