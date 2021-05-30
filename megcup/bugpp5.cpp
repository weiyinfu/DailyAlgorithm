#include <algorithm>
#include <bitset>
#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

const int N = 2000;
const int ROWS = 8;
bitset<N * 3 + 1> e[N * ROWS], a[N * 3];
bool sel[N + 1][N + 1], b[N * 3];
bool image[N + 1][N + 1];

inline int pos(int x, int y) {
    return (x % ROWS) * N + y;
}

inline bool valid(int x, int y) {
    return x >= 0 && x < N && y >= 0 && y < N;
}

void print() {
    for (int j = 0; j < N * 3 + 1; ++j)
        printf("__");
    printf("\n");
    for (int i = 0; i < N * 3; ++i) {
        for (int j = 0; j < N * 3 + 1; ++j) {
            if (a[i][j]) printf("1 ");
            else printf("  ");
        }
        printf("\n");
    }
    for (int j = 0; j < N * 3 + 1; ++j)
        printf("--");
    printf("\n");
    printf("\n");
}

char str[N*N + 10];

int main(int argc, char *argv[]) {

    FILE *f = fopen("bugpp.txt", "r");
    fscanf(f, "%s", str);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j)
            image[i][j] = str[i*N+j] == '1';
    }
    fclose(f);

    for (int x = 0; x < 3; ++x)
        for (int y = 0; y < N; ++y) {
            int p = pos(x, y);
            e[p][p] = true;
        }
    for (int x = 3; x < N; ++x) {
        for (int y = 0; y < N; ++y) {
            int p = pos(x, y);
            e[p].reset();
            e[p][N * 3] = image[x - 3][y];
            for (int i = -3; i < 3; ++i)
                if (valid(x - 3 + i, y)) {
                    int q = pos(x - 3 + i, y);
                    e[p] ^= e[q];
                }
            for (int j = -3; j <= 3; ++j)
                if (j != 0 && valid(x - 3, y + j)) {
                    int q = pos(x - 3, y + j);
                    e[p] ^= e[q];
                }
        }
    }
    for (int x = N - 3; x < N; ++x)
        for (int y = 0; y < N; ++y) {
            int p = pos(x - (N - 3), y);
            a[p][N * 3] = image[x][y];
            for (int i = -3; i <= 3; ++i)
                if (valid(x + i, y)) {
                    int q = pos(x + i, y);
                    a[p] ^= e[q];
                }
            for (int j = -3; j <= 3; ++j)
                if (j != 0 && valid(x, y + j)) {
                    int q = pos(x, y + j);
                    a[p] ^= e[q];
                }
        }

    cerr << "coef done" << endl;

    const int n = N * 3;
    for (int i = 0; i < n; ++i) {
        int pivot = -1;
        for (int j = i; j < n; ++j)
            if (a[j][i]) {
                pivot = j;
                break;
            }
        if (pivot == -1) continue;
        if (pivot != i) a[i] ^= a[pivot];
        for (int j = i + 1; j < n; ++j) {
            if (!a[j][i]) continue;
            a[j] ^= a[i];
        }
    }
    for (int i = n - 1; i >= 0; --i) {
        int pivot = -1;
        for (int j = i; j >= 0; --j)
            if (a[j][i]) {
                pivot = j;
                break;
            }
        if (pivot == -1) continue;
        for (int j = pivot - 1; j >= 0; --j) {
            if (!a[j][i]) continue;
            a[j] ^= a[pivot];
        }
    }
    cerr << "gaussian done" << endl;

    vector<int> free;
    for (int i = 0; i < n; ++i) {
        bool any = a[i].any();
        if (!any) free.push_back(i);
        if (!any) assert(!a[i][n]);
        else assert(a[i][i]);
    }
    cerr << free.size() << endl;

    int k = (int)free.size();
    int ans = INT_MAX;
    for (int state = 0; state < (1 << k); ++state) {
        for (int i = 0; i < k; ++i)
            b[free[i]] = (bool)(state >> i & 1);
        for (int i = n - 1; i >= 0; --i) {
            if (!a[i][i]) continue;
            bool val = a[i][n];
            for (int j = i + 1; j < n; ++j)
                if (a[i][j]) val ^= b[j];
            b[i] = val;
        }
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < N; ++j)
                sel[i][j] = b[pos(i, j)];
        for (int x = 3; x < N; ++x)
            for (int y = 0; y < N; ++y) {
                bool val = image[x - 3][y];
                for (int i = -3; i < 3; ++i)
                    if (valid(x - 3 + i, y)) val ^= sel[x - 3 + i][y];
                for (int j = -3; j <= 3; ++j)
                    if (j != 0 && valid(x - 3, y + j)) val ^= sel[x - 3][y + j];
                sel[x][y] = val;
            }
        // check validity
        for (int x = N - 3; x < N; ++x)
            for (int y = 0; y < N; ++y) {
                bool val = image[x][y];
                for (int i = -3; i <= 3; ++i)
                    if (valid(x + i, y)) val ^= sel[x + i][y];
                for (int j = -3; j <= 3; ++j)
                    if (j != 0 && valid(x, y + j)) val ^= sel[x][y + j];
                assert(!val);
            }

        int sum = 0;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                sum += sel[i][j];
        ans = min(ans, sum);
        cerr << state << " " << sum << endl;
    }

    cout << ans << endl;

	fclose(stdin);
	fclose(stdout);
	return 0;
}
