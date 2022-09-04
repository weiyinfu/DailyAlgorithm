package horseracing.horse;

import java.util.List;
/**
 * 只返回第一对pair
 * */
public class FirstPairGenerator extends BasePairGenerator {
@Override
public List<Pair> getCompetePairs(Board board) {
    return super.getCompetePairs(board).subList(0, 1);
}
}
