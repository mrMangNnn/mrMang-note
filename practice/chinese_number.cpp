/********************************************************************
    > File Name: liangzai.cpp
    > Author: Liang zai
    > Created Time: 2020年06月09日 星期二 15时20分32秒
 *******************************************************************/
/* 将输入的阿拉伯数字串转换为汉字数字串输出 */

#include<iostream>
#include<string.h>

using namespace std;
	
void help()
{
	cout << "请输入一个数字:" << endl;
}

void figure(int x)
{
	const char* a[10] = {"零","一","二","三","四","五","六","七","八","九"};
	cout << a[x];
}

void digit(int x)
{
	if (x == 2)
	{
		cout << "十";
	}else if (x == 3)
	{
		cout << "百";
	}else if (x == 4)
	{
		cout << "千";
	}else if (x == 5)
	{ 
		cout << "万";
	}
}

int even_zero(int *x, int *max, int *j)
{
	if(*max == 0)
	{
		return 0;
	}
	if (*x/ *max != 0)
	{
		return 1;
	}
	while(*max > 0)
	{
		if (*j == 5)
		{
			digit(5);
		}
		if ((*x/ *max) == 0)
		{
			(*j)--;
			*x = *x% *max;
			*max = *max/10;
		}else
		{
			(*j)++;
			return 2;
		}
	}
	return 0;
}

void chinese(int x)
{
	int l=0, max=1, t=x;
	for (int y=x; y>0; y/=10)
	{
		l++;
	}
	for (int t=1; t<l; t++)
	{
		max*=10;
	}
	for (int j=l; j>0; j--)
	{
		int ret = even_zero(&t, &max, &j);
		if (ret == 1)
		{
			if (l == 6 && t/max == 1 && j == 6)
			{

			}else
			{
				figure(t/max);
			}
			j > 5 ? digit(j-4) : digit(j);
			t = t%max;
			max/=10;
		}else if (ret == 2)
		{
			figure(0);		
		}
	}
}

int main()
{
	help();
	int a;
	cin >> a;
	chinese(a);

	return 0;
}
