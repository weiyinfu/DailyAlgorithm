package horseracing.horse;

import java.util.List;

/**
 * 这个程序是Bruteforce的缩减版，这个程序的优点在于：
 * 肯定不会内存溢出，只要算力足够强大就能够计算到很多位
 */
public class BruteForceWithoutTraceback {
//N匹马取前K名
int N, K;
//使用字典记录已经解决过的局面，一方面用于加速；另一方面用于回溯寻找解法
Board board;
PairGenerator generator = new BasePairGenerator();


//求局面的最少步数
int minSteps(int maxStep) {
    if (board.isOver()) {
        return 0;
    }
    if (maxStep <= 0) return N * N;
    int nowMin = N * N;
    List<Pair> strategies = generator.getCompetePairs(board);
    for (Pair p : strategies) {
        List<Pair> fix = board.updateByCompeteResult(p.x, p.y);
        int xy = minSteps(nowMin);
        board.undo(fix);
        if (xy >= nowMin) continue;
        if (board.isSame(p.x, p.y)) {
            nowMin = Math.min(nowMin, xy);
        } else {
            fix = board.updateByCompeteResult(p.y, p.x);
            int yx = minSteps(nowMin);
            board.undo(fix);
            nowMin = Math.min(Math.max(xy, yx), nowMin);
        }
    }
    return 1 + nowMin;
}

//打表寻找规律
void findRule() {
    long begTime = System.currentTimeMillis();
    int n = 9;
    for (int i = 1; i < n; i++) {
        for (int j = 1; j <= i; j++) {
            int minStep = solveOne(i, j, 100);
            System.out.print(minStep + " ");
        }
        System.out.println();
    }
    long endTime = System.currentTimeMillis();
    System.out.println("总共用时" + (endTime - begTime));
}


int solveOne(int n, int k, int maxStep) {
    this.N = n;
    this.K = k;
    this.board = new Board(n, k);
    if (maxStep == 0) maxStep = n * n;
    int ans = minSteps(maxStep);
    return ans;
}


BruteForceWithoutTraceback() {
    findRule();
//    showStrategy(5, 3);
}

public static void main(String[] args) {
    new BruteForceWithoutTraceback();
}
}
