
def markdown_to_blocks(document):
    blocks = document.split("\n\n")
    for i in range(len(blocks)):
        lines = blocks[i].strip().split("\n")
        lines = [line.strip() for line in lines]
        blocks[i] = "\n".join(lines)
    return blocks

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
