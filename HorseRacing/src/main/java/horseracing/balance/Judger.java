package horseracing.balance;

import java.util.ArrayList;
import java.util.List;

public class Judger {
    /**
     * 当备选答案遇见称量策略strategy之后的结果
     */
    boolean heavy = true;
    int n;

    Judger(int n, boolean heavy) {
        this.n = n;
        this.heavy = heavy;
    }

    int judge(int solution, Strategy strategy) {
        boolean heavier = true;
        if (!this.heavy) {
            if (solution > n) {
                solution -= n;
            } else {
                heavier = false;
            }
        }
        for (int i : strategy.left) if (i == solution) return heavier ? 1 : 2;
        for (int i : strategy.right) if (i == solution) return heavier ? 2 : 1;
        return 0;
    }

    List<Integer> getAllSolutions() {
        List<Integer> ans = new ArrayList<>(n << 1);
        for (int i = 0; i < n << (heavy ? 0 : 1); i++) {
            ans.add(i);
        }
        return ans;
    }
}
