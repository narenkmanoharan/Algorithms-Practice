tree_height = int(input("Please enter the height of the tree: "))
stump_val = tree_height
hashes, spaces = 1,tree_height
while tree_height != 0:
	for x in range(spaces):
		print(' ', end = '')
	for y in range(hashes):
		print('#', end = '')
	print()
	hashes += 2
	spaces -= 1
	tree_height -= 1
stump_thickness = stump_val/4
stump_start_val = int(stump_val/3)
for i in range(stump_start_val):
	for i in range(int(stump_val) - int(stump_val/10)):
		print(' ', end = '')
	for _ in range(int(stump_thickness)):
		print('#', end='')
	print()

