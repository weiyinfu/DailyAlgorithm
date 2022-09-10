package horseracing.balance;

import java.util.ArrayList;
import java.util.List;

/**
 * 启发式方法寻找病球，答案不一定是最少步数
 */
public class Main {
    int n = 12;
    boolean heavy = false;
    Judger judger = new Judger(n, heavy);

    //根据当前可行解决定下一步的称量计划
    Node build(List<Integer> solutions, int order) {
        Node node = new Node(solutions, order);
        if (solutions.size() <= 1) return node;
        node.strategy = new Heuristic(n, node.solutions, judger).bestStrategy;
        List<List<Integer>> sonsSolutions = new ArrayList<>(3);
        for (int i = 0; i < 3; i++) sonsSolutions.add(new ArrayList<>());
        for (int solution : node.solutions) {
            int res = judger.judge(solution, node.strategy);
            sonsSolutions.get(res).add(solution);
        }
        for (int i = 0; i < 3; i++) node.sons[i] = build(sonsSolutions.get(i), i);
        return node;
    }

    Main() {
        Node root = build(judger.getAllSolutions(), 0);
        new StrategyPlayer(root, heavy, n);
    }

    public static void main(String[] args) {
        new Main();
    }
}
