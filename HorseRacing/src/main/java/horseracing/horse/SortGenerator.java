package horseracing.horse;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class SortGenerator extends BasePairGenerator {
    @Override
    public List<Pair> getCompetePairs(Board board) {
        //根据局面获取比赛对,优先让高手们决战,优先让优胜者胜
        List<Pair> pairs = new ArrayList<>();
        Set<String> added = new TreeSet<>();
        for (int i = 0; i < board.N; i++) {
            for (int j = 0; j < i; j++) {
                if (board.a[i][j] == 0) {
                    String pairCode = board.hashPerson(i) + board.hashPerson(j);
                    if (!added.contains(pairCode)) {
                        added.add(pairCode);
                        pairs.add(new Pair(i, j));
                    }
                }
            }
        }
        pairs.sort((o1, o2) -> {
            int one = board.win[o1.x] + board.win[o1.y];
            int two = board.win[o2.x] + board.win[o2.y];
            return two - one;
        });
        return pairs;
    }
}
