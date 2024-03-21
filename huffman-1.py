# Define the messages and their relative frequencies
messages = ["M1", "M2", "M3", "M4", "M5", "M6", "M7"]
frequencies = (4,5,7,8,10,12,20)

class Node:
    def __init__(self, freq, message=None):
        self.freq = freq
        self.message = message
        self.left = None
        self.right = None

def construct_tree(messages, frequencies):

    nodes = []
    for i in range(len(messages)):
        node = Node(frequencies[i], messages[i])
        nodes.append(node)

    while len(nodes) > 1 :

        #ascending order
        nodes = sorted(nodes, key=lambda node: node.freq)

        left_node = nodes.pop(0)
        right_node = nodes.pop(0)

        parent_node = Node(left_node.freq + right_node.freq)
        parent_node.left = left_node
        parent_node.right = right_node
        nodes.append(parent_node)

    return nodes[0]

# assign codes
def assign_codes(node, code, codes):
    if node.message:
        codes[node.message] = code
    else:
        assign_codes(node.left, code + "0", codes)
        assign_codes(node.right, code + "1", codes)

# Construct the Huffman tree
root = construct_tree(messages, frequencies)

#driver code
codes = {}
assign_codes(root, "", codes)
for message in messages:
    print(f"{message}: {codes[message]}")