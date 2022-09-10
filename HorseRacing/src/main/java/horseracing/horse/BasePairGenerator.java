package horseracing.horse;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

/**
 * 最基本的决策产生器
 */
public class BasePairGenerator implements PairGenerator {
    List<Pair> hashInt(Board board) {
        List<Pair> pairs = new ArrayList<>();
        Set<Long> added = new TreeSet<>();
        for (int i = 0; i < board.N; i++) {
            for (int j = 0; j < i; j++) {
                if (board.a[i][j] == 0) {
                    int one = board.hashPersonInt(i);
                    int two = board.hashPersonInt(j);
                    long pairCode;
                    if (one < two) {
                        pairCode = (one << 16) | two;
                    } else {
                        pairCode = (two << 16) | one;
                    }
                    if (!added.contains(pairCode)) {
                        added.add(pairCode);
                        pairs.add(new Pair(i, j));
                    }
                }
            }
        }
        return pairs;
    }

    List<Pair> hashString(Board board) {
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
        return pairs;
    }

    @Override
    public List<Pair> getCompetePairs(Board board) {
        //根据局面获取比赛对,优先让高手们决战,优先让优胜者胜
        if (board.N < 16) {
            return hashInt(board);
        } else {
            return hashString(board);
        }
    }
}
