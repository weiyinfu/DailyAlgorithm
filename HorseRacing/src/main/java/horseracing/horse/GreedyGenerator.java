package horseracing.horse;

import java.util.Collections;
import java.util.List;
/**
 * 贪心法，每次选择能够画出最多对号的那些着法
 * */
public class GreedyGenerator extends BasePairGenerator {
@Override
public List<Pair> getCompetePairs(Board board) {
    List<Pair> pairs = super.getCompetePairs(board);
    Pair bestPair = null;
    int bestProfit = Integer.MIN_VALUE;
    for (Pair i : pairs) {
        List<Pair> operations = board.updateByCompeteResult(i.x, i.y);
        int one = operations.size();
        board.undo(operations);
        operations = board.updateByCompeteResult(i.y, i.x);
        int two = operations.size();
        board.undo(operations);
        int profit = Math.min(one, two);//利润就是可以填充的符号越多越好
        if (profit > bestProfit) {
            bestProfit = profit;
            bestPair = i;
        }
    }
    return Collections.singletonList(bestPair);
}
}
