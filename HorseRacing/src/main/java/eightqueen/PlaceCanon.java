package eightqueen;

import java.util.Scanner;

/**
 * 在N*M的棋盘上放置若干个互不攻击的炮，有多少种放法？
 * 动态规划插头DP，逐行放置，考虑每列炮数为0，1的个数。
 * dp[i][j][k]表示第i行有j个0炮列、k个1炮列的情况下有多少种放法
 * <p>
 * 问题链接
 * https://www.luogu.org/problemnew/show/P2051
 */
public class PlaceCanon {
int MA = 9999973;

PlaceCanon() {
    Scanner cin = new Scanner(System.in);
    int N = cin.nextInt(), M = cin.nextInt();
    if (N < M) {
        int temp = M;
        M = N;
        N = temp;
    }
    if (M == 1) {
        long ans = 1 + N + N * (N - 1) / 2;
        ans %= MA;
        System.out.println(ans);
        return;
    }
    long dp[][][] = new long[N][M + 1][M + 1];
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            dp[0][i][j] = 0;
        }
    }
    if (M >= 2)
        dp[0][M - 2][2] = M * (M - 1) / 2;//put 2
    if (M >= 1)
        dp[0][M - 1][1] = M;//put 1
    dp[0][M][0] = 1;//put 0
    for (int i = 0; i < N - 1; i++) {//行
        for (int j = 0; j <= M; j++) {//包含0个炮的列
            for (int k = 0; k <= M; k++) {//包含1个炮的列
                if (dp[i][j][k] == 0) continue;
                //放置0个
                dp[i + 1][j][k] = (dp[i + 1][j][k] + dp[i][j][k]) % MA;

                //放置1个
                //放在0个炮的列上
                if (j >= 1)
                    dp[i + 1][j - 1][k + 1] = (dp[i + 1][j - 1][k + 1] + dp[i][j][k] * j) % MA;
                //放在1个炮的列上
                if (k >= 1)
                    dp[i + 1][j][k - 1] = (dp[i + 1][j][k - 1] + dp[i][j][k] * k) % MA;

                //放置2个
                //放在0个的列上
                if (j >= 2)
                    dp[i + 1][j - 2][k + 2] = (dp[i + 1][j - 2][k + 2] + dp[i][j][k] * j * (j - 1) / 2) % MA;
                //放在1个的列上
                if (k >= 2)
                    dp[i + 1][j][k - 2] = (dp[i + 1][j][k - 2] + dp[i][j][k] * k * (k - 1) / 2) % MA;
                //放在0个和1个的列上,0列减一，1列个数不变
                if (j >= 1 && k >= 1)
                    dp[i + 1][j - 1][k] = (dp[i + 1][j - 1][k] + dp[i][j][k] * j * k) % MA;
            }
        }
    }
    long s = 0;
    for (int i = 0; i <= M; i++) {
        for (int j = 0; j <= M; j++) {
            s += dp[N - 1][i][j];
            s %= MA;
        }
    }
    System.out.println(s);
}

public static void main(String[] args) {
    new PlaceCanon();
}
}