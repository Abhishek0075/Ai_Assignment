class search:
	def linear_search_iterative(self,arr,key):
		position=-1
		for i in range(10):
			if(arr[i]==key):
				position=i
				break
		if(position==-1):
			print(key," not in the array")
		else:
			print(key," found at ",(position+1),"th postion")

A=search()
a=[10,9,4,3,2,11,5,7,2,1]
print("The array = ")
for i in range(10):
    print(a[i],end=" ")
print()
print("Enter the key to be searched ")
key=int(input("Enter the number to be searched in the list : "))
print("Result : ")
A.linear_search_iterative(a,key)


