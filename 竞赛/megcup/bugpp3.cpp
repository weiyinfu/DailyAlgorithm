#include <bits/stdc++.h>
using namespace std;
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)

int n;
int a[2007][2007];
typedef bitset<6007> bs;

bs (*b)[2007];
int bx[6007], by[6007], bn = 0;
bs l[6007]; int ln = 0;

int c[2007][2007], d[2007][2007];

void modi(int x, int y, bs &c)
{
	if(x >= n || y < 0 || y >= n)
		return;
	b[x][y] ^= c;
}

void modj(int x, int y)
{
	if(x >= n || y < 0 || y >= n)
		return;
	d[x][y] ^= 1;
}

int zv[6007];

int main()
{
	cin >> n;
	g(i, 0, n) g(j, 0, n) cin >> a[i][j];
	// n = 101;
	// g(i, 0, n) g(j, 0, n) a[i][j] = 1;
	b = new bs[2007][2007];
	g(i, 0, 3) g(j, 0, n)
	{
		++bn; bx[bn] = i; by[bn] = j;
	}
	g(i, 0, 3 + 4) g(j, 0, n) f(bi, 1, bn)
		if((i == bx[bi] && abs(j - by[bi]) <= 3) || (j == by[bi] && abs(i - bx[bi]) <= 3))
			b[i][j].set(bi);
	g(i, 0, n - 3) g(j, 0, n)
	{
		bs &c = b[i][j];
		if(a[i][j])
			c[0] = !c[0];
		modi(i + 1, j, c);
		modi(i + 2, j, c);
		modi(i + 3, j - 3, c);
		modi(i + 3, j - 2, c);
		modi(i + 3, j - 1, c);
		modi(i + 3, j, c);
		modi(i + 3, j + 1, c);
		modi(i + 3, j + 2, c);
		modi(i + 3, j + 3, c);
		modi(i + 4, j, c);
		modi(i + 5, j, c);
		modi(i + 6, j, c);
	}
	g(i, n - 3, n) g(j, 0, n)
	{
		if(a[i][j])
			b[i][j][0] = !b[i][j][0];
		l[++ln] = b[i][j];
	}
	printf("ln = %d, bn = %d, should equal\n", ln, bn);
	zv[0] = 0;
	vector<int> free;
	f(i, 1, ln)
	{
		zv[i] = zv[i - 1] + 1;
		restart:;
		printf("\rgauss %d    ", i);
		if(!l[i][zv[i]])
		{
			f(j, i + 1, ln)
			{
				if(l[j][zv[i]])
				{
					swap(l[i], l[j]);
					goto found;
				}
			}
			printf("line not found for %d, free %d\n", i, zv[i]);
			free.push_back(zv[i]++);
			if(zv[i] > ln)
			{
				f(j, i, ln)
					zv[j] = zv[i];
				break;
			}
			goto restart;
			found:;
		}
		f(j, i + 1, ln)
			if(l[j][zv[i]])
				l[j] ^= l[i];
	}
	printf("\n\n");
	h(i, ln, 1) if(zv[i] <= ln)
	{
		printf("\rgauss back %d    ", i);
		g(j, 1, i)
			if(l[j][zv[i]])
				l[j] ^= l[i];
	}
	int tans = 233333333;
	int fs = free.size();
	int tm = (1 << fs);
	g(cm, 0, tm)
	{
		int fc[fs];
		memset(c, 0, sizeof(c));
		g(j, 0, fs){
			c[bx[free[j]]][by[free[j]]] = fc[j] = (cm >> j & 1);
		}
		f(i, 1, ln) if(zv[i] <= ln)
		{
			c[bx[zv[i]]][by[zv[i]]] = l[i][0];
			g(j, 0, fs) if(l[i][free[j]] && fc[j])
				c[bx[zv[i]]][by[zv[i]]] ^= 1;
		}
		memset(d, 0, sizeof(d));
		int ans = 0;
		f(bi, 1, bn)
		{
			if(c[bx[bi]][by[bi]])
				++ans;
			g(i, 0, 3 + 4) g(j, 0, n)
				if((i == bx[bi] && abs(j - by[bi]) <= 3) || (j == by[bi] && abs(i - bx[bi]) <= 3))
					d[i][j] ^= c[bx[bi]][by[bi]];
		}
		g(i, 0, n - 3) g(j, 0, n)
		{
			if(a[i][j] != d[i][j])
			{
				++ans;
				modj(i, j);
				modj(i + 1, j);
				modj(i + 2, j);
				modj(i + 3, j - 3);
				modj(i + 3, j - 2);
				modj(i + 3, j - 1);
				modj(i + 3, j);
				modj(i + 3, j + 1);
				modj(i + 3, j + 2);
				modj(i + 3, j + 3);
				modj(i + 4, j);
				modj(i + 5, j);
				modj(i + 6, j);
			}
		}
		g(i, 0, n) g(j, 0, n) if(a[i][j] != d[i][j]) printf("wtf? %d %d\n", i, j);
		tans = min(tans, ans);
		printf("%d,%d | %d,%d\n", cm, tm, ans, tans);
	}
	printf("%d is the best answer\n", tans);
	return 0;
}
