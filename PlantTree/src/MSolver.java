import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class MSolver {
int colorCount, treeCount, forestCount;
int[][] cost;
int big = (int) (1e9 + 7);

MSolver() throws FileNotFoundException {
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
        //f[i][j][k]表示种了i棵树最后一棵树是j森林树是k
        long[][][] f = new long[treeCount][colorCount][forestCount];
        for (int i = 0; i < f.length; i++)
            for (int j = 0; j < f[i].length; j++)
                for (int k = 0; k < f[i][j].length; k++) {
                    if (i == 0) {
                        if (k == 0) {
                            f[i][j][0] = cost[0][j];
                        } else {
                            f[i][j][k] = big;
                        }
                    } else {
                        long ans = big;
                        for (int p = 0; p < colorCount; p++) {
                            //上次种树的颜色
                            long now;
                            if (p == j) {
                                now = f[i - 1][p][k];
                            } else {
                                if (k == 0) {
                                    now = big;
                                } else {
                                    now = f[i - 1][p][k - 1];
                                }
                            }
                            ans = Math.min(ans, now + cost[i][j]);
                        }
                        f[i][j][k] = ans;
                    }
                }
        long ans = big;
        for (int lastColor = 0; lastColor < colorCount; lastColor++) {
            ans = Math.min(ans, f[treeCount - 1][lastColor][forestCount - 1]);
        }
        if (ans == big) {
            ans = -1;
        }
        System.out.println(ans);
    }
}

public static void main(String[] args) throws FileNotFoundException {
    new MSolver();
}
}
