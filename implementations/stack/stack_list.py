"""
Implementing stack ADT using python built-in list structure

"""


"""
Stack without class
- stack is simply a list
- all operations are functions with stack as an argument
"""

# create empty stack
def create_stack():
    stack = []
    return stack

# check if stack is empty
def is_empty(stack):
    return len(stack) == 0

# check size of stack
def check_size(stack):
    return len(stack)

# push item into stack
def push(stack, item):
    stack.append(item)
    print(f"Pushed new item {item} into stack")

# pop item out
def pop(stack):
    if is_empty(stack):
        print("Cannot pop an empty stack!")
        return None
    return stack.pop()

# get the top item
def peak(stack):
    if is_empty(stack):
        print("Stack is empty without top item!")
        return None
    return stack[-1]

# Testing
stack = create_stack()
print(is_empty(stack))
push(stack, 3)
push(stack, 'hello')
push(stack, True)
push(stack, [1,2,3])
print(stack)
print(check_size(stack))
pop(stack)
pop(stack)
print(stack)
print(check_size(stack))
print(peak(stack))
print(check_size(stack))
pop(stack)
pop(stack)
print(peak(stack))
pop(stack)
print("Size of stack", check_size(stack))