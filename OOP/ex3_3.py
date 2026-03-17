#1
def print_line():
    print("+ - - - - + - - - - +")
def print_row():
    print("|         |         |")
print_line()
for i in range(4):
    print_row()
print_line()
for i in range(4):
    print_row()
print_line()
#2
def print_line():
    print("+ - - - - + - - - - + - - - - + - - - - +")
def print_row():
    print("|         |         |         |         |")
for i in range(4):
    print_line()
    for j in range(4):
        print_row()
print_line()