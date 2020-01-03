n = int(input())

parent_list = [-1] * n
right_list = [-1] * n
child_list = [-1] * n
depth_list = [0] * n

for i in range(n):
    node, _, *children = map(int, input().split())
    for index, child in enumerate(children):
        # parent
        parent_list[child] = node
        # right
        if 0 <= index < len(children) - 1:
            right_list[child] = children[index+1]
        # child
        if 0 == index:
            child_list[node] = child

def set_depth(node, depth):
    depth_list[node] = depth
    right_node = right_list[node]
    child_node = child_list[node]
    if right_node != -1:
        set_depth(right_node, depth)
    if child_node != -1:
        set_depth(child_node, depth+1)

set_depth(0, 0)

print(parent_list)
print(right_list)
print(child_list)
print(depth_list)


for node in range(n):
    parent = parent_list[node]
    mat_depth = max(depth_list)
    node_child = []
    child = child_list[node]
    while child != -1:
        node_child.append(child)
        child = right_list[child]

    if depth_list[node] == 0:
        status = "root"
    elif child_list[node] == -1:
        status = "leaf"
    else:
        status = "internal node"

    print("node {:>2}: parent = {:>2}, depth = {}, {:>13}, {}".
          format(node, parent, depth_list[node], status, node_child))