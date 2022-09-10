package horseracing.horse;

import java.util.Arrays;
import java.util.List;

/**
 * 启发式着法生成器
 * 首先对list&lt;pairs&gt;进行排序
 * 然后对pair内的马进行排序，希望让能胜算大的马赢（这样能够是游戏进行足够多步，从而尽早剪枝）
 */
public class HeuristicGenerator extends BasePairGenerator {
    @Override
    public List<Pair> getCompetePairs(Board board) {
        List<Pair> pairs = super.getCompetePairs(board);
        pairs.sort((m, n) -> {
            int loseM = board.lose[m.x] + board.lose[m.y];
            int winM = board.win[m.x] + board.win[m.y];
            int loseN = board.lose[n.x] + board.lose[n.y];
            int winN = board.win[n.x] + board.win[n.y];
            if (loseM == loseN) {
                return winN - winM;
            } else {
                return loseM - loseN;
            }
        });
        pairs.forEach(p -> {
            int dif;
            if (board.lose[p.x] == board.lose[p.y]) {
                dif = board.win[p.x] - board.win[p.y];
            } else {
                dif = board.lose[p.y] - board.lose[p.x];
            }
            if (dif < 0) {
                int temp = p.x;
                p.x = p.y;
                p.y = temp;
            }
        });
        return pairs;
    }

    public static void main(String[] args) {
        int a[] = new int[]{1, 3, 2};
        Arrays.sort(a);
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}
