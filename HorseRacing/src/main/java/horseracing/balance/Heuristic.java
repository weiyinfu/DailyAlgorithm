package horseracing.balance;

import java.util.List;

public class Heuristic {
    Strategy bestStrategy = null;
    int bestProfit = 0;
    Judger judger;

    /**
     * 计算决策的收益
     * 天平有三种结果：0，1，2
     * 假设这三种结果对应的答案个数分别为c1，c2，c3
     * 那么经过此次决策之后的期望剩余答案个数为
     * c1/N*c1+c2/N*c2+c3/N*c3
     * N可以省略掉
     */
    int profit(int[] cnt) {
        int s = 0;
        for (int i : cnt) {
            s += i * i;
        }
        return -s;
    }

    Heuristic(int n, List<Integer> solutions, Judger judger) {
        this.judger = judger;
        //遍历决策列表
        new StrategyList(n, strategy -> {
            int res[] = new int[3];//天平有三种状态
            for (int solution : solutions) {
                res[judger.judge(solution, strategy)]++;
            }
            int p = profit(res);
            if (bestStrategy == null || p > bestProfit) {
                bestProfit = p;
                bestStrategy = strategy.copy();
            }
        });
    }
}
