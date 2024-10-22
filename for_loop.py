
# Alexander J. Jackson
# for_loop.py

def main():
	if len(list1) == len(list2):
		print("These list are the same length")
		compare_list(list1, list2)
	else:
		print("These list do not match")


def compare_list(l_1, l_2):
	count = 2
	# If y doesn't equal x in second loop, program ends & prints "False"
	for x in l_1:
		count -= 1
		if count == 0:
			print("False")
			quit
		for y in l_2:
			if y == x:
				count += 1
			else:
				pass
	print("True")


list1 = [1, 2, 3]
list2 = [3, 1, 2]

	

main()
