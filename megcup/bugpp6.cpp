#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)

const int SZ = 2000;
bitset<3 * SZ + 5> row[SZ * SZ + 11 * SZ + 5];
int A[SZ + 5][SZ + 5], ans[SZ + 5][SZ + 5];
int isfree[SZ * 10], depend[SZ * 10][15];
#define ENCODE(i, j) ((i - 1) * SZ + j - 1 + 10 * SZ)
int main() {
	freopen("F.in", "r", stdin);
	//READ DATA
	For(i,1,SZ) For(j,1,SZ) scanf("%d", &A[i][j]);
	For(i,1,SZ) For(j,1,SZ) {
		row[ENCODE(i, j)].reset();
		if (i <= 3) {
			row[ENCODE(i, j)][(i - 1) * SZ + j - 1] = 1;
		} else {
			//last one to save (i - 3, j)
			For(x,max(1, i - 6), i - 1) row[ENCODE(i, j)] ^= row[ENCODE(x, j)];
			For(x,max(1, j - 3), min(SZ, j + 3)) if (x != j) row[ENCODE(i, j)] ^= row[ENCODE(i - 3, x)];
			row[ENCODE(i, j)].set(3 * SZ, row[ENCODE(i, j)][3 * SZ] ^ A[i - 3][j]);
		}
	}
	int rc = 0;
	For(i,1,SZ) For(j,1,SZ) {
		row[rc].reset();
		For(x,max(1,i - 3), min(SZ, i + 3)) row[rc] ^= row[ENCODE(x, j)];
		For(x,max(1,j - 3), min(SZ, j + 3)) if (x != j) row[rc] ^= row[ENCODE(i, x)];
		row[rc].set(3 * SZ, row[rc][3 * SZ] ^ A[i][j]);
		++rc;
	}
	vector<int> free;
	int max_col = 0;
	For(i,0,3 * SZ - 1) {
		cerr << i << endl;
		if (!row[i][i]) {
			For(j,0,i - 1) if (!row[j][j] && row[j][i]) {
				swap(row[i], row[j]);
				break ;
			}
			For(j,i + 1,rc - 1) if (row[j][i]) {
				swap(row[i], row[j]);
				break ;
			}
		}
		if (!row[i][i]) {
			free.push_back(i);
			if (row[i][3 * SZ]) {
				puts("No solution");
				return 0;
			}
			continue ;
		}
		For(j,0,rc - 1) if (j != i && row[j][i]) {
			row[j] ^= row[i];
		}
	}
	For(i,0,3 * SZ - 1) {	
		ans[i / SZ + 1][i % SZ + 1] = row[i][3 * SZ];
	}
	for (auto &x : free) isfree[x] = true;
	For(i,0,3 * SZ - 1) if (!isfree[i]) {
		int id = 0;
		for (auto x: free) {
			if (row[i][x]) depend[i][id] = true;
			++id;
		}
	}
	For(i,0,3 * SZ - 1) {
		printf("%d ", (int)row[i][3 * SZ]);
		for (int j = 0; j < free.size(); ++j) if (depend[i][j]) {
			printf("%d ", j);
		}
		puts("");
	}
	cout << free.size() << endl;
	for (auto x: free) printf("%d ", x); puts("");
	
	int out = 1e9;
	for (int S = 0; S < (1 << free.size()); ++S) {
		for (int i = 0; i < 3 * SZ; ++i) {
			if (isfree[i]) {
				for (int j = 0; j < free.size(); ++j) if (free[j] == i) {
					ans[i / SZ + 1][i % SZ + 1] = S >> j & 1;
				}
			} else {
				ans[i / SZ + 1][i % SZ + 1] = row[i][3 * SZ];
				for (int j = 0; j < free.size(); ++j) if (depend[i][j]) {
					ans[i / SZ + 1][i % SZ + 1] ^= (S >> j & 1);
				}
			}
		}
		int cur = 0;
		For(i,4,SZ) For(j,1,SZ) {
			int c = A[i - 3][j];
			For(x,max(1, i - 6), i - 1) c ^= ans[x][j];
			For(x,max(1, j - 3), min(SZ, j + 3)) if (x != j) c ^= ans[i - 3][x];
			ans[i][j] = c;
		}
		For(i,1,SZ) For(j,1,SZ) if (ans[i][j]) ++cur;
		out = min(out, cur);
	}

	cout << out << endl;


	//For(i,1,3 * SZ) {
	//	For(j,0,3 * SZ) printf("%d ", row[i][j]);
	//	puts("");
	//}

	return 0;
}