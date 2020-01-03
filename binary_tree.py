class binary_tree():
    def __init__(self):
        self.parent = -1 
        self.left = -1
        self.right = -1
        self.height = -1

def get_sibling(node: int) -> int:
    if T[node].parent == -1:
        return -1
    
    parent = T[node].parent
    left = T[parent].left
    right = T[parent].right

    if left == node:
        return right
    else:
        return left
        
def get_degree(node: int) -> int:
    ans = 0
    ans += 1 if T[node].left != -1 else 0
    ans += 1 if T[node].right != -1 else 0
    return ans

def get_depth(node: int) -> int:
    depth = 0
    parent = T[node].parent
    while parent != -1:
        depth += 1
        parent = T[parent].parent    
    return depth

def get_height(node: int) -> int:
    left_height, right_height = 0, 0
    if T[node].left != -1:
        left_height = get_height(T[node].left) + 1
    if T[node].right != -1:
        right_height = get_height(T[node].right) + 1
    return max(left_height, right_height)

def get_status(node: int) -> int:
    if T[node].parent == -1:
        return "root"
    elif T[node].left == -1 and T[node].right == -1:
        return "leaf"
    else:
        return "internal node"

def preorder(node: int) -> None:
    if node == -1:
        return
    
    print(node)
    preorder(T[node].left)
    preorder(T[node].right)

def inorder(node: int) -> None:
    if node == -1:
        return
    
    inorder(T[node].left)
    print(node)
    inorder(T[node].right)

def postorder(node: int) -> None:
    if node == -1:
        return
    
    postorder(T[node].left)
    postorder(T[node].right)
    print(node)

if __name__ == "__main__":
    n = int(input())
    T = [binary_tree() for _ in range(n)]

    for i in range(n):
        node, left, right = map(int, input().split())
        T[node].left = left
        T[node].right = right

        if left != -1:
            T[left].parent = node
        if right != -1:
            T[right].parent = node

    for i in range(n):
        print("node {}: parent = {:>2}, sibling = {:>2}, degree = {:>2}, "\
              "depth = {:>2}, height = {:>2}, {:>13}".
              format(i, T[i].parent, get_sibling(i), get_degree(i),
                     get_depth(i), get_height(i), get_status(i)))

    print("== preorder == ")
    preorder(0)
    print("== inorder == ")
    inorder(0)
    print("== postorder == ")
    postorder(0)
