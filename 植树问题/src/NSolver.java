import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class NSolver {
int colorCount, treeCount, forestCount;
int[][] cost;
int big = (int) (1e9 + 7);

NSolver() throws FileNotFoundException {
    Scanner cin = new Scanner(System.in);
    cin = new Scanner(new FileInputStream("in.txt"));
    int cas = cin.nextInt();
    while (cas-- > 0) {
        treeCount = cin.nextInt();
        colorCount = cin.nextInt();
        forestCount = cin.nextInt();
        cost = new int[treeCount][colorCount];
        for (int i = 0; i < treeCount; i++) {
            for (int j = 0; j < colorCount; j++) {
                cost[i][j] = cin.nextInt();
            }
        }
        if (treeCount == 0) {
            System.out.println(0);
            continue;
        }
        if (colorCount == 0 && treeCount > 0
                || treeCount > 0 && forestCount == 0
                || colorCount <= 1 && forestCount > 1
                || forestCount > treeCount
        ) {
            System.out.println(-1);
            continue;
        }
        int ma = (int) (treeCount - (forestCount - 1.0) / 2.0);
        if (ma < 0) {
            System.out.println(-1);
            continue;
        }
        //求前缀和,co[i][j]表示i种树种j棵的花费
        long[][] co = new long[colorCount][ma + 1];
        for (int i = 0; i < colorCount; i++) {
            for (int j = 1; j <= ma; j++) {
                co[i][j] += co[i][j - 1] + cost[j - 1][i];
            }
        }
        int maxUsed = Math.min(forestCount, colorCount) + 1;
        //f[i][j][k]表示使用前i种颜色种了j棵树，真正用到的树的个数为k
        long[][][] f = new long[colorCount][treeCount + 1][maxUsed];
        for (int i = 0; i < colorCount; i++) {
            for (int j = 0; j <= treeCount; j++) {
                for (int l = 0; l < maxUsed; l++) {
                    if (i == 0) {
                        if (j > 0) {
                            //如果种
                            if (l == 1) {
                                f[0][j][1] = j <= ma ? co[i][j] : big;
                            } else {
                                f[0][j][l] = big;
                            }
                        } else {
                            if (l > 0)
                                f[0][0][l] = big;
                            else
                                f[0][0][l] = 0;
                        }
                    } else {
                        f[i][j][l] = big;
                        for (int p = 0; p <= ma; p++) {
                            //此次准备种树的个数
                            long now;
                            if (p > 0) {
                                //如果此次种树
                                if (l == 0) {
                                    now = big;
                                } else {
                                    if (j >= p) {
                                        now = f[i - 1][j - p][l - 1] + co[i][p];
                                    } else {
                                        now = big;
                                    }
                                }
                            } else {
                                //如果此次不种树
                                now = f[i - 1][j][l];
                            }
                            f[i][j][l] = Math.min(f[i][j][l], now);
                        }
                    }
                }
            }
        }
        long ans = big;
        for (int usedCount = 0; usedCount < maxUsed; usedCount++) {
            long now = f[colorCount - 1][treeCount][usedCount];
            ans = Math.min(ans, now);
        }
        if (ans == big) {
            ans = -1;
        }
        System.out.println(ans);
    }
}

public static void main(String[] args) throws FileNotFoundException {
    new NSolver();
}
}
