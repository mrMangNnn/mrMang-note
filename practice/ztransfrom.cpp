#include "iostream"
#include "string"
#include "vector"

using namespace std;

int main()
{
	string a;
	cin >> a;
	int num;
	cin >> num;
	
	int e = a.size()/((num-1)*2);
	int u = a.size()%((num-1)*2);
	int vertical = (num-1)*e;
	
	if (u<=num && u>0)
	{
		vertical = vertical+1;
	}else if (u>num)
	{
		vertical = vertical+u-num+1;
	}
	
	vector<vector<char> > transform(vertical+1, vector<char>(num,' '));
	
	int k=0,l=2;
	for (int i=0; i<vertical; i++)
	{
		for (int j=0; j<num; j++)
		{
			if (i%(num-1)==0 || i==0)
			{
				transform[i][j] = a[k];
				k++;
				l=2;
			}else
			{
				transform[i][num-l] = a[k];
				l++;
				k++;
				break;
			}
		}
		if (k == a.size())
		{
			break;
		}
	}
	for (int i=0; i<num; i++)
	{
		transform[vertical][i] = ' ';
	}
	
	for (int i=0; i<num; i++)
	{
		for (int j=0; j<vertical; j++)
		{
			cout << transform[j][i];
		}
		cout << endl; 
	}
	
	int count=1;
	for (int i=0; i<num; i++)
	{
		for (int j=0; j<=vertical; j=j+num-1)
		{
			if (i!=0 && i!=num-1 && j>0)
			{
				cout << transform[j-count][i];
				count++;
			}
			if (count>num-2)
			{
				count=1;
			}
			if (transform[j][i]!=' ')
			{
				cout << transform[j][i];
			}
		}
	}
	cout << endl;

	return 0;
}