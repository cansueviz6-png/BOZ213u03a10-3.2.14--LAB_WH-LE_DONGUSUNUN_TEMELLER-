Blocks = int(input("Enter the number of blocks :"))

height = 0
layer = 1

while Blocks >= layer:
     Blocks = Blocks - layer
     height = height + 1
     layer = layer + 1

print("The height of the pramid:", height)

     
