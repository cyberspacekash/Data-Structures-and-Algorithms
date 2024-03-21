class Node:
    def __init__(self, char=None):
        self.char = char
        self.left = None
        self.right = None

def decodeHuffman(root, s):
    decoded_string = ""
    curr = root
    for i in s:
        if i == '0':
            curr = curr.left
        else:
            curr = curr.right
        if curr.char:
            decoded_string += curr.char
            curr = root
    return decoded_string

# creation of manual huffmann tree given in question
root = Node()
root.left = Node("A")
root.right = Node()
root.right.left = Node('R')
root.right.right = Node()
root.right.right.left = Node()
root.right.right.right = Node("B")
root.right.right.left.left = Node("C")
root.right.right.left.right = Node("D")

#given codeword
encoded_string = "1100010011000100"

decoded_string = decodeHuffman(root, encoded_string)
print(decoded_string)