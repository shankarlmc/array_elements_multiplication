# main function
def max(ar, size):
	# initialize a with first element of array
	a = ar[0]
	# initialize b with second element of array
	b = ar[1]
	# product between a and b
	p = a * b
	for i in range(0, size):
		for j in range (i+1, size):
			if (ar[i] * ar[j] > p):
				a = ar[i]
				b = ar[j]
				p = a * b
	print(f"The pair having maximum product are {a} , {b}.")
	print(f"The maximum product is : {p} ")

# initial array inputs
inp_arr = [1, 2, 3, 4]
# calculate the length of array
arr_size = len(inp_arr)
# calling the function with passing array and array size
max(inp_arr, arr_size)

