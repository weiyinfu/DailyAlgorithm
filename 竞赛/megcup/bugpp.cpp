#include <bits/stdc++.h>
#include <unistd.h>

using namespace std;
//此题很显然是求解大型线性方程组，特点是方程有无数个解，需要找到和最小的一组正解
//记录图形
const int dx[13] = {0, 0, 0, 0,  0,  0,  0, 1, 2, 3, -1, -2, -3};
const int dy[13] = {0, 1, 2, 3, -1, -2, -3, 0, 0, 0,  0,  0,  0};

//记录长宽
const int n = 2000;

//为啥是6000维
bitset<6001> gauss[6000];
bitset<6001> gauss_veri[6000];
int ans[6000];
vector<int> freevars;//自由变量
vector<int> nonfuck[20];//最多有20个自由向量？

//消元
int elimination()
{
	for (int i = 0;i < n*3;i++) gauss_veri[i] = gauss[i];
	int cnt = 0;
	for (int i = 0;i < n * 3;i++) {
		int pick = -1;
		for (int j = i;j < n * 3;j++) {
			if (gauss[j].test(i)) {
				pick = j;
				break;
			}
		}
		if (pick == -1) {
			// assert(0);
			continue;
		}
		cnt++;
		if (pick != i) {
			swap(gauss[i], gauss[pick]);
		}
		for (int j = 0;j < n * 3;j++) {
			if (j == i) continue;
			if (gauss[j].test(i)) {
				gauss[j] ^= gauss[i];
			}
		}
	}
	fprintf(stderr, "Non free vars: %d\n", cnt);
	for (int i = n * 3 - 1;i >= 0;i--) {
		if (gauss[i].test(i)) {
			ans[i] = gauss[i].test(n * 3);
			for (int j = 0;j < n * 3;j++) {
				if (j == i) continue;
				if (gauss[i].test(j)) {
					assert(j >= i);
					ans[i] ^= ans[j];
				}
			}
		} else {
			fprintf(stderr, "Free var %d...\n", i);
			freevars.push_back(i);
			ans[i] = 0;
			for (int j = 0;j < n*3;j++) {
				if (gauss[j].test(i)) {
					assert(j < i);
					nonfuck[freevars.size()-1].push_back(j);
				}
			}
		}
	}
	for (int i = 0;i < n*3;i++) {
		int t = 0;
		for (int j = 0;j < n*3;j++) {
			if (gauss_veri[i].test(j)) t ^= ans[j];
		}
		if (t != gauss_veri[i].test(n*3)) {
			fprintf(stderr, "FUCK\n");
			exit(0);
		}
		assert(t == gauss_veri[i].test(n*3));
	}
	return 0;
}

int respread(int msk)
{
	for (int i = 0;i < 12;i++) {
		if (((msk >> i) & 1) != ans[freevars[i]]) {
			ans[freevars[i]] ^= 1;
			for (auto x : nonfuck[i]) {
				ans[x] ^= 1;
			}
		}
	}
	for (int i = 0;i < n*3;i++) {
		int t = 0;
		for (int j = 0;j < n*3;j++) {
			if (gauss_veri[i].test(j)) t ^= ans[j];
		}
		if (t != gauss_veri[i].test(n*3)) {
			fprintf(stderr, "FUCK\n");
			exit(0);
		}
		assert(t == gauss_veri[i].test(n*3));
	}
	return 0;
}

char logo[4444444];
char mat[2000][2000];
bitset<6001> expr[2000][2000];
// char extra[2000][2000];

int finalans[2000][2000];
bitset<6001> ansbit;// int reconstruct()// {


int reconstruct()
{
	for (int x = 0; x < 3; x++) {
		for (int y = 0; y < n; y++) {
			finalans[x][y] = ans[x * n + y];
		}
	}
	for (int x = 3;x < n;x++) {
		for (int y = 0;y < n;y++) {
			int t = 0;
			for (int k = 0;k < 13;k++) {
				int nx = x - 3 + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				if (nx == x && ny == y) continue;
				assert(nx < x);
				t ^= finalans[nx][ny];
			}
			if (mat[x - 3][y]) t ^= 1;
			finalans[x][y] = t;
		}
	}
	return 0;
}


char pg[2000][2000];

int validate()
{
	memset(pg, 0, sizeof(pg));
	for (int x = 0; x < n;x++) {
		for(int y = 0;y < n;y++) {
			for (int k = 0;k < 13;k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				pg[x][y] ^= finalans[nx][ny];
				if (x == 0 && y == 3) {
					// printf("[%d][%d] = %d\n", nx, ny, finalans[nx][ny]);
				}
			}
		}
	}
	int wcnt = 0;
	for (int x = 0; x < n;x++) {
		for(int y = 0;y < n;y++) {
			if (pg[x][y] != mat[x][y]) {
				printf("Wrong Answer @ %d, %d, should be %d instead of %d\n", x, y, mat[x][y], pg[x][y]);
				if (wcnt++ > 2) exit(0);
			}
		}
	}
}

int debug(int x, int y)
{
	printf("v%d =", x * 2000 + y);
	for (int i = 0;i < 6000;i++) {
		if (expr[x][y].test(i)) printf(" v%d", i);
	}
	printf(" %d", expr[x][y].test(3*n));
	puts("");
}

vector<pair<int,int>> affected[20];

int main(void)
{
	scanf("%s", logo);

	for (int i = 0; i < n; i++) {
		for (int j = 0;j < n;j++) {
			mat[i][j] = logo[i * n + j] - '0';
		}
	}

	for (int x = 0;x < 3;x++) {
		for (int y = 0;y < n;y++) {
			expr[x][y].set(x * n + y);
		}
	}

	for (int x = 3;x < n;x++) {
		if (x % 100 == 0) fprintf(stderr, "%d\n", x);
		for (int y = 0;y < n;y++) {
			// [x-3][y]
			for (int k = 0;k < 13;k++) {
				int nx = x - 3 + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				if (nx == x && ny == y) continue;
				assert(nx < x);
				expr[x][y] ^= expr[nx][ny];
				// extra[x][y] ^= extra[nx][ny];
			}
			// extra[x][y] ^= mat[x - 3][y];
			if (mat[x - 3][y]) expr[x][y].flip(n * 3);
		}
	}
	// debug(3, 3);

	for (int x = n-3;x < n;x++) {
		fprintf(stderr, "%d\n", x);
		for (int y = 0;y < n;y++) {
			for (int k = 0;k < 13;k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
				gauss[(x - (n-3)) * n + y] ^= expr[nx][ny];
			}
			if (mat[x][y]) gauss[(x - (n-3)) * n + y].flip(n * 3);
		}
	}
	fprintf(stderr, "Solving...\n");
	elimination();
	reconstruct();
	fprintf(stderr, "Solved.\n");


	// Brute force below
	int fvl = freevars.size();
	int minans = ~0U>>1;
	int whoami = 0;
	bool master = false;
	for (int i = 0;i < 7;i++) {
		if(fork()) {
			master = true;
		} else {
			whoami = i;
			master = false;
			break;
		}
	}

	if (master) whoami = 7;
	int all = (1 << fvl);
	int piece = all / 8;
	int mskbegin = piece * whoami;
	int mskend = mskbegin + piece;

	for (int msk = mskbegin; msk < mskend; msk++) {
		// validate();
		// printf("first valid ok\n");
		respread(msk);
		reconstruct();
		// validate();
		int cnt = 0;
		for (int i = 0;i < n;i++) for(int j = 0;j < n;j++) cnt += finalans[i][j];
		printf("%d Ans: %d\n", msk-mskbegin, cnt);
		minans = min(minans, cnt);
		printf("Minans: %d\n", minans);
	}
	printf("Final minans: %d\n", minans);
	validate();
	return 0;
}