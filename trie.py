# Enter your code here. Read input from STDIN. Print output to STDOUT
class TrieNode():
    def __init__(self, char):
        self.character = char
        self.children = {}
        self.endOfWord = False
        
def add(root, word):
    node = root
    for char in word:
        found_in_children = False
        if char in node.children:
            node = node.children[char]
            found_in_children = True
        if not found_in_children:
            new_node = TrieNode(char)
            node.children[char] = new_node    
            node = new_node        
    node.endOfWord = True

def search(root, word):
    node = root
    for char in word:
        if char not in node.children:
            return False
        else: node = node.children[char]
    return node.endOfWord

def searchPrefix(root, prefix):
    node = root
    for char in prefix:
        if char not in node.children:
            return False
        else: node = node.children[char]
    return True
            
    
def printTrie(root):
    if root:
        node = root
        for key in node.children.keys():
            print(node.children[key].character)
            printTrie(node.children[key])
        
root = TrieNode('*')

add(root, "hellomynameis")
add(root, "goodbye")

print(searchPrefix(root, "hello"))

printTrie(root)
