#include<iostream>
using namespace std;
class search{
    public:
      int linear_search(int arr[10],int n,int key){
          int position;
          if (n>0){
        	  if(arr[n]==key){
        		  position=n;
        		  return n;
        	  }else{
        	      return (linear_search(arr,n-1,key));
        	  }
          }else{
              return (-1);
          }
       }
};

int main(){
    search A;
    int key;
	int a[10]={10,9,4,3,2,11,5,7,2,1};
	cout<<"Enter the key to be searched "<<endl;
	cin>>key;
	cout<<"Result : "<<endl;
	cout<<A.linear_search(a,10,key);
	return 0;
}

