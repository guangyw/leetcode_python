def iterative_inorder(root):
    inorder_vals = []
    nodes_to_visit = []

    if (root == None):
        return inorder_vals

    node_ptr = root

    while node_ptr != None or len(nodes_to_visit) != 0:
        while node_ptr != None:
            nodes_to_visit.append(node_ptr)
            node_ptr = node_ptr.left

        node_ptr = nodes_to_visit.pop()
        inorder_vals.append(node_ptr.val)
        node_ptr = node_ptr.right

    return inorder_vals

