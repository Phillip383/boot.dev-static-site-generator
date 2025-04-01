from generation import *
from constants import *
import sys
def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = str(sys.argv[1])
    print(f"BASE_PATH: {base_path}")
    copy_dir(STATIC_DIR, PUBLIC_DIR)
    generate_pages_recursive(CONTENT_DIR, TEMPLATE_PATH, PUBLIC_DIR, base_path)

if __name__ == "__main__":
    main()
