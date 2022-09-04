package horseracing.horse;

import java.util.List;
import java.util.Random;

/**
 * 随机决策产生器
 */
public class RandomPairGenerator extends BasePairGenerator {
Random random = new Random();

@Override
public List<Pair> getCompetePairs(Board board) {
    List<Pair> a = super.getCompetePairs(board);
    int x = random.nextInt(a.size());
    return a.subList(x, x + 1);
}
}
