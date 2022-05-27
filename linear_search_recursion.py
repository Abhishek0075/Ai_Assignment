class search:
    def linear_search(self,arr,n,key):
        n=n-1
        if (n>=0):
            if(arr[n]==key):
                position=n
                return (position+1)
            else:
                return (self.linear_search(arr,n,key))
        
        else:
            return (-1)
A=search()
a=[10,9,4,3,2,11,5,7,2,1]
print("Enter the key to be searched ")
key=int(input("Enter the number to be searched : "))
print("Result : ")
print("The position of ",key," is at ",end="")
print(A.linear_search(a,10,key))


