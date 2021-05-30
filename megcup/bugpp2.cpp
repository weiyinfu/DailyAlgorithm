#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 2010

using namespace std;

bool sts[6][MaxN][3 * MaxN];

int n, m;
int mat[MaxN][MaxN], sta[MaxN];//定义图、栈
bool nowk[3 * MaxN], nowl[MaxN][3 * MaxN];
bool is_free[MaxN * 3];
bool use[MaxN * 3];
bool bases[MaxN * 3][MaxN * 3];
bool col[MaxN][MaxN];

int Ans = ~0u >> 1;//MAX_VALUE

void calc() {
	for (int i = 3 * m - 1; i >= 0; --i) {
		if (is_free[i]) {
			use[i] = bases[i][3 * m];
			for (int j = i + 1; j < 3 * m; ++j) {
				if (bases[i][j])
					use[i] ^= use[j];
			}
		}
	}
	// self-check
	for (int i = 0; i < 3 * m; ++i) {
		if (is_free[i]) {
			bool nx = 0;
			for (int j = 0; j < 3 * m; ++j) {
				if (bases[i][j]) {
					nx ^= use[j];
				}
			}
			if (nx != bases[i][3 * m]) {
				printf("gan!\n");
				while(1);
			}
		}
	}
	for (int i = 1; i <= 3; ++i)
		for (int j = 1; j <= m; ++j) {
			col[i][j] = use[(i - 1) * m + j - 1];
		}
	for (int i = 1; i <= n - 3; ++i) {
		for (int j = 1; j <= m; ++j) {
			bool nx = col[i][j];
			for (int k = -3; k <= 2; ++k) {
				if (i + k >= 1 && i + k <= n)
					nx ^= col[i + k][j];
			}
			for (int k = -3; k <= 3; ++k) {
				if (j + k >= 1 && j + k <= m)
					nx ^= col[i][j + k];
			}
			nx ^= mat[i][j];
			col[i + 3][j] = nx;
		}
	}
	int cnt = 0;
	/*
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			bool nx = col[i][j];
			for (int k = -3; k <= 3; ++k) {
				if (i + k >= 1 && i + k <= n)
					nx ^= col[i + k][j];
				if (j + k >= 1 && j + k <= m)
					nx ^= col[i][j + k];
			}
			if (nx != mat[i][j]) {
				printf("wrong! %d %d\n", i, j);
				while(1);
			}
		}
	}
	*/
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			cnt += col[i][j];
		}
	}
	printf("find a solution cnt = %d Ans = %d\n", cnt, Ans);
	if (cnt < Ans) {
		Ans = cnt;
	}
}

void dfs(int now) {
	if (now == 3 * m) {
		calc();
		return;
	}

	if (is_free[now] == 0) {
		use[now] = 0;
		dfs(now + 1);
		use[now] = 1;
		dfs(now + 1);
	}
	else {
		dfs(now + 1);
	}
}

int main() {
	scanf("%d%d", &n, &m);//输入长度和宽度
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) {
			scanf("%d", &mat[i][j]);
			mat[i][j] ^= 1;
		}
	
	for (int i = 3; i < 6; ++i)
		for (int j = 0; j < m; ++j)
			sts[i][j][(i - 3) * m + j] = true;

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			// calc (i + 3, j) from i, j
			//nowk表示第三行的状态
			for (int k = 0; k <= 3 * m; ++k)
				nowk[k] = sts[3][j - 1][k];
			//暂存下当前的
			for (int l = 0; l < 6; ++l) {
				for (int k = 0; k <= 3 * m; ++k)
					nowk[k] ^= sts[l][j - 1][k];
			}
			for (int l = -3; l <= 3; ++l) {
				if (j + l < 1 || j + l > m)
					continue;
				for (int k = 0; k <= 3 * m; ++k)
					nowk[k] ^= sts[3][j - 1 + l][k];
			}
			for (int k = 0; k <= 3 * m; ++k)
				nowl[j - 1][k] = nowk[k];
			//对下一行的影响
			nowl[j - 1][3 * m] ^= mat[i][j];
		}
		//处理前四行，滚动
		for (int j = 0; j <= 4; ++j) {
			for (int k = 0; k < m; ++k) {
				for (int l = 0; l <= 3 * m; ++l) {
					sts[j][k][l] = sts[j + 1][k][l];
				}
			}
		}
		//复制第五行
		for (int j = 0; j < m; ++j)
			for (int k = 0; k <= 3 * m; ++k)
				sts[5][j][k] = nowl[j][k];
	}

	printf("begin calc!\n");
	int ans = 0;

	for (int i = 3; i < 6; ++i) {
		for (int j = 0; j < m; ++j) {
			bool flag = false;
			for (int k = 0; k <= 3 * m; ++k) {
				if (is_free[k] && sts[i][j][k]) {
					for (int l = 0; l <= 3 * m; ++l)
						sts[i][j][l] ^= bases[k][l];
				}
				if ((!is_free[k]) && sts[i][j][k]) {
					is_free[k] = 1;
					for (int l = 0; l <= 3 * m; ++l)
						bases[k][l] = sts[i][j][l];
					flag = true;
					break;
				}
			}
			if (flag)
				++ans;
			else {
				for (int k = 0; k <= 3 * m; ++k) {
					if (sts[i][j][k] != 0) {
						puts("ha?");
						while(1);
					}
				}
			}
		}
	}


	printf("%d\n", ans);

	dfs(0);

	printf("%d!\n", Ans);

	return 0;
}