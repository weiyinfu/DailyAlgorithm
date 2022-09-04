package horseracing.horse;

import java.util.List;

/**
 * 验证器，验证给定一组决策是否完备
 */
public class Validator {
int N, K;
Board board;
Pair[] tree;//决策树

Validator(int n, int k, Pair[] tree) {
    this.N = n;
    this.K = k;
    this.board = new Board(n, k);
    this.tree = tree;
}

void validateRecursive(Pair[] tree, int x) {
    if (board.isOver()) {
        //如果游戏已经结束了，决策树还没结束，那是不正常的
        if (x < tree.length && tree[x] != null) {
            throw new RuntimeException("validte fail! game over but not ended");
        }
        return;
    }
    //如果决策树结束了，游戏还没结束，那是不正常的
    if (x >= tree.length || tree[x] == null) {
        throw new RuntimeException("validate fail ! game not over but ended");
    }
    List<Pair> fix = board.updateByCompeteResult(tree[x].x, tree[x].y);
    validateRecursive(tree, x << 1);
    board.undo(fix);
    //如果两者等价，可以剪枝；否则需要继续验证
    if (!board.isSame(tree[x].x, tree[x].y)) {
        fix = board.updateByCompeteResult(tree[x].y, tree[x].x);
        validateRecursive(tree, x << 1 | 1);
        board.undo(fix);
    }
}

//验证结果的正确性
void validate() {
    validateRecursive(tree, 1);
}

}
