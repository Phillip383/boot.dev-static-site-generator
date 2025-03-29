from enum import Enum

class BlockType(Enum):
    paragraph = 0,
    heading = 1,
    code = 2,
    quote = 3,
    unordered_list = 4,
    ordered_list = 5

def markdown_to_blocks(document):
    blocks = document.split("\n\n")
    for i in range(len(blocks)):
        lines = blocks[i].strip().split("\n")
        lines = [line.strip() for line in lines]
        blocks[i] = "\n".join(lines)
    return blocks

def __check_pattern(pattern, lines):
    return [line.startswith(pattern) for line in lines]

def __check_ordered_list(lines) -> bool:
    previous_num = None
    for i in range(len(lines)):
        try:
            current_num = int(lines[i][0])
        except:
            return False
        else:
            if previous_num != None:
                if current_num != previous_num + 1:
                    return False
            previous_num = current_num
    return True

def block_to_block_type(block):
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(headings):
        return BlockType.heading
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.code

    lines = block.split("\n")
    if not False in __check_pattern(">", lines):
        return BlockType.quote

    if not False in __check_pattern("- ", lines):
        return BlockType.unordered_list

    #check for ordered list
    if __check_ordered_list(lines):
        return BlockType.ordered_list

    return BlockType.paragraph

if __name__ == "__main__":
    blocks = markdown_to_blocks(
        """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
 
        """
    )
    for block in blocks:
        print(block)
