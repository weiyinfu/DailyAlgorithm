package horseracing.guess;

import org.dom4j.Element;
import horseracing.treeplayer.NodeVisitor;
import horseracing.treeplayer.TreePlayer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 贪心法估计最少需要尝试多少次才能找到答案
 * <p>
 * 给N道单选题，每道单选题有四个答案，每次可以提交N个0~3之间的数字，提交之后会反馈得了多少分，请设计最优的“瞎蒙机”，使得尝试次数的期望尽量少！
 * <p>
 * 如果可以不做选择:
 * 最多需要尝试4N次就可以找到答案。
 * <p>
 * 这个问题略微有点复杂,可以简化之.
 * 给定N道判断题,你的决策期望尝试多少次才能得到答案.
 * <p>
 * 2道题尝试2次
 * 3道题尝试3次
 * 4道题尝试4次
 * 5道题尝试4次
 * 6道题尝试5次
 * 7道题尝试6次
 * 8道题尝试6次
 * 9道题尝试6次
 * 10道题尝试7次
 * 11道题尝试7次
 *
 * N道题,每道题都是包含M个选项的单选题,求f(N,M)表示最多需要尝试多少次才能解决问题.
 */
public class Main {
int N = 11;//问题的个数
Node root;
int maxTry = 0;

int getScore(int stra, int solution) {
    int s = 0;
    for (int i = 0; i < N; i++) {
        if ((stra & (1 << i)) == (solution & (1 << i))) s++;
    }
    return s;
}

void go(Node node, int level) {
    if (node.solutions.size() <= 1) {
        return;
    }
    maxTry = Math.max(level, maxTry);
    int best = 0;
    int bestScore = Integer.MAX_VALUE;
    List<List<Integer>> bestSons = new ArrayList<>();
    for (int stra = 0; stra < (1 << N); stra++) {
        List<List<Integer>> sons = new ArrayList<>(N + 1);
        for (int i = 0; i < N + 1; i++) sons.add(new ArrayList<>());
        for (int solution : node.solutions) {
            int score = getScore(stra, solution);
            sons.get(score).add(solution);
        }
        int good = 0;
        for (int i = 0; i <= N; i++) {
            good += sons.get(i).size() * sons.get(i).size();
        }
        if (good < bestScore) {
            bestScore = good;
            bestSons = sons;
            best = stra;
        }
    }
    node.strategy = best;
    for (int i = 0; i <= N; i++) {
        node.sons[i] = new Node(bestSons.get(i), N, i);
        go(node.sons[i], level + 1);
    }
}

Main() {
    List<Integer> solutions = new ArrayList<>();
    for (int i = 0; i < Math.pow(2, N); i++) {
        solutions.add(i);
    }
    root = new Node(solutions, N, 0);
    go(root, 1);
    System.out.println(maxTry);
    TreePlayer.swingControl(new NodeVisitor<Node>() {
        @Override
        public List<Node> getSons(Node node) {
            return Arrays.stream(node.sons).filter(x -> x != null && x.solutions.size() >= 1).collect(Collectors.toList());
        }

        String tos(int x) {
            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < N; i++) {
                if ((x & (1 << i)) == 0) {
                    builder.append('0');
                } else {
                    builder.append('1');
                }
            }
            return builder.toString();
        }

        @Override
        public String tos(Node node) {
            String prefix = "如果" + node.order + "分,";
            if (node.solutions.size() == 0) return prefix + "无解";
            if (node.solutions.size() == 1) return prefix + "答案是" + tos(node.solutions.get(0));
            return prefix + tos(node.strategy);
        }

        @Override
        public Element toElement(Node node) {
            return null;
        }

        @Override
        public Node root() {
            return root;
        }
    });
}

public static void main(String[] args) {
    new Main();
}
}
