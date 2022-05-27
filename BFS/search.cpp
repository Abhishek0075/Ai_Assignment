#include <iostream>
using namespace std;
const int m =100;
class search
{
	public:
	int linear_search_iterative(int A[m],int key,int L);
	int rec_linear_search(int A[m],int key,int L);
};

int search::rec_linear_search(int A[m],int key,int L)
{
	if (L>0)
	{
		if (A[L] == key)
		{
			return L;
		}
		else
		{
			return rec_linear_search(A,key,L-1);
		}
	}
	return -1;
}

int search::linear_search_iterative(int A[m],int key,int L)
{
	int pos = -1;
	for (pos = 0;pos<L;pos++)
	{
		if (A[pos] == key)
		{
			return pos;
		}
	}
	return -1;
}

int main()
{
	search X;
	int L[9] = {1,3,5,6,7,8,9,8,6};
	cout<<X.linear_search_iterative(L,12,9)<<endl;
	cout<<X.rec_linear_search(L,9,9)<<endl;
}
