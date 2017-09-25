"""Recursion lecture examples."""


def count_loop():
    """Count to 3, using a while loop."""
    n = 1
    while True:
        if n > 3:
            break

        print n,
        n = n + 1


print "count_loop"
count_loop()


def count_recursive(n=1):
    """Count to 3, using recursion."""

    # BASE CASE
    if n > 3:
        return

    # initial 1 2 3
    print n,
    count_recursive(n + 1)

    # going back out, 3 2 1
    print n,


print "\n\ncount_recursive"
count_recursive()

###########################################################

data = [1, [2, [3], 4], 5]  # => 2 4 6 8 10


def doubler_no_recursion(lst):
    """Print items in list doubled, not using recursion."""

    stack = list(reversed(lst))

    while stack:
        n = stack.pop()
        if isinstance(n, list):
            # If it's a list, add it to stack, reversed
            for inner in reversed(n):
                stack.append(inner)
        else:
            print n * 2,


print "\n\ndoubler_no_recursion"
doubler_no_recursion(data)


def doubler_recursive(lst):
    """Print items in list doubled, using recursion."""

    for n in lst:
        if isinstance(n, list):
            doubler_recursive(n)
        else:
            print n * 2,


print "\n\ndoubler_recursive"
doubler_recursive(data)


def doubler_no_loop(lst):
    """Print items in list doubled, using recursion but no loop."""

    if lst == []:
        return

    n = lst[0]

    if isinstance(n, list):
        doubler_no_loop(n)
    else:
        print n * 2,

    doubler_no_loop(lst[1:])


print "\n\ndoubler_no_loop"
doubler_no_loop(data)

###########################################################

lst = [7, 4, 3, 2]


def lenlist(lst):
    """Return length of list, using recursion."""

    # when list empty (r/t taking first item out of list w/ each recursion)
    if not lst:
        return 0

    # return 1 + 0 during first break = 1, then 2, 3, and ultimately 4
    return 1 + lenlist(lst[1:])


print "\n\nlenlist"
print lenlist(lst)


###########################################################


class Node(object):
    """Tree node."""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []


root = Node("/", [
    Node("Users/", [
        Node("jane/", [Node("resume.txt"), Node("recipes.txt")]),
        Node("jessica/", [Node("server.py")])
    ])
])


def ls(node):
    """List all nodes. Depth 1st search."""

    # print current node
    print node.data

    # print descendants until no children left (when for loop done)
    for child in node.children:
        ls(child)


print "\n\nls\n"
ls(root)


def indent_ls(node, depth=0):
    """List all nodes, indented."""

    print "  " * depth + node.data
    for child in node.children:
        indent_ls(child, depth + 1)


print "\n\nindent_ls\n"
indent_ls(root)
