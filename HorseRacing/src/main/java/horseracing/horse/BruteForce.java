package horseracing.horse;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 程序入口类
 * 核心类，相当于评判器
 * 给定一个决策生成器，此评判器可以为决策生成器进行打分
 */
public class BruteForce {
    //N匹马取前K名
    int N, K;
    //使用字典记录已经解决过的局面，一方面用于加速；另一方面用于回溯寻找解法
    Map<String, Integer> solved = new HashMap<>();//已经解决过得局面
    Board board;
    PairGenerator generator = new GreedyGenerator();
    //基本生成器，用于回溯
    BasePairGenerator simple = new BasePairGenerator();

    /**
     * 回溯找到策略
     */
    void traceStrategyRecursive(int x, Pair[] tree, int maxStep) {
        if (board.isOver()) return;
        //寻找当前局面最优策略
        List<Pair> pairs = simple.getCompetePairs(board);
        for (Pair p : pairs) {
            int xy = N * N, yx = N * N;
            List<Pair> fix = board.updateByCompeteResult(p.x, p.y);
            String now = board.hash();
            if (solved.containsKey(now)) {
                xy = solved.get(now);
            }
            if (board.isOver()) {
                xy = 0;
            }
            board.undo(fix);
            if (xy > maxStep - 1) continue;
            if (!board.isSame(p.x, p.y)) {
                fix = board.updateByCompeteResult(p.y, p.x);
                now = board.hash();
                if (solved.containsKey(now)) {
                    yx = solved.get(now);
                }
                if (board.isOver()) {
                    yx = 0;
                }
                board.undo(fix);
            } else {
                yx = xy;
            }
            if (Math.max(xy, yx) < maxStep) {
                tree[x] = p;
                break;
            }
        }
        if (tree[x] == null) return;
        //访问左子树
        List<Pair> fix = board.updateByCompeteResult(tree[x].x, tree[x].y);
        traceStrategyRecursive(x << 1, tree, maxStep - 1);
        board.undo(fix);
        //访问右子树
        fix = board.updateByCompeteResult(tree[x].y, tree[x].x);
        traceStrategyRecursive(x << 1 | 1, tree, maxStep - 1);
        board.undo(fix);
    }

    //回溯找到最优策略
    Pair[] traceStrategy(int minStep) {
        Pair[] tree = new Pair[1 << minStep];
        traceStrategyRecursive(1, tree, minStep);
        return tree;
    }


    //求局面的最少步数
    int minSteps(int maxStep) {
        if (board.isOver()) {
            return 0;
        }
        if (maxStep <= 0) return N * N;
        String code = board.hash();
        if (solved.containsKey(code)) return solved.get(code);
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
        if (nowMin < N * N) {
            solved.put(code, 1 + nowMin);
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
                Pair[] stra = traceStrategy(minStep);
                new Validator(i, j, stra).validate();
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
        solved.clear();
        if (maxStep == 0) maxStep = n * n;
        int ans = minSteps(maxStep);
        return ans;
    }

    //展示Strategy
    void showStrategy(int n, int k) {
        int ans = solveOne(n, k, 0);
        System.out.println("最少步数\n" + board.screenCut() + "\n" + ans);
        Pair[] tree = traceStrategy(ans);
        StrategyPlayer p = new StrategyPlayer(tree);
        System.out.println(p.fileStyle());
        p.xml();
        p.swingControl();
        new Validator(n, k, tree).validate();
    }

    BruteForce() {
        findRule();
//    showStrategy(5, 3);
    }

    public static void main(String[] args) {
        new BruteForce();
    }
}
