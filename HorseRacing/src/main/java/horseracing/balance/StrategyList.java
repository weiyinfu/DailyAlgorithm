package horseracing.balance;

import java.util.ArrayList;
import java.util.List;

/**
 * 遍历全部决策，通过StrategyVisitor进行访问每个决策
 */
public class StrategyList {
int n;
StrategyVisitor v;

StrategyList(int n, StrategyVisitor v) {
    this.n = n;
    this.v = v;
    go();
}

void go() {
    List<Integer> a = new ArrayList<>();
    for (int i = 0; i < n; i++) a.add(i);
    //天平两端小球个数必然相同，否则必然是无意义的称量
    for (int i = 1; i <= n / 2; i++) {
        final int cnt = i;
        //先从全部球中选择cnt个，再从cnt个球中选择cnt/2个
        new Select(a, i * 2, chosen -> new Select(chosen, cnt, right -> {
            List<Integer> left = new ArrayList<>(cnt);
            int j = 0;
            for (int k = 0; k < chosen.size(); k++) {
                if (j < right.size() && chosen.get(k).equals(right.get(j))) {
                    j++;
                } else {
                    left.add(chosen.get(k));
                }
            }
            v.handle(new Strategy(left, right));
        }));
    }
}


}
