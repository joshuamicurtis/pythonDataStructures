from stack import stack

print "Testing stack.py"

print "Initializing stack1"
stack1 = stack()

print "Pushing values 1, 2, 4, 8 to stack1"
stack1.push(1)
stack1.push(2)
stack1.push(4)
stack1.push(8)
print "Pop values from the top of the stack"
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print "Is the stack empty?"
print(stack1.is_empty())
print "Try to pop an empty stack"
stack1.pop()
print "push 42 to the stack"
stack1.push(42)
print "Is the stack empty?"
print(stack1.is_empty())
