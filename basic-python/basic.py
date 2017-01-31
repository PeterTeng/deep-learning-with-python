type(10) #=> <class 'int'>
type("Hello") #=> <class 'str'>

# Set variable
x = 1
x = 100

y = 3.14

print(x * y) #=> 314.0

type(x * y) #=> <class 'float'>

# List
l = [1, 2, 3, 4, 5, 100]
l[0] #=> 1

l[:3] #=> [1, 2, 3]

# Dictionary
d = {"name": "Peter"}
d["height"] = 180

print(d) #=> {'name': 'Peter', 'height': 180}

# Boolean
crazy = True
funny = False

type(funny) #=> <class 'bool'>

not crazy #=> Flase

crazy and funny #=> False

crazy or funny #=> True

# Usage of (if)
if crazy:
    print("Is crazy!!!")
else:
    print("Is not crazy")

# Loop
for i in [1, 2, 3]:
    print(i)

# Function
def hello(arg):
    print("Hello, " + arg + "!!!")

hello("deep learning")
