package horseracing.auc;

import org.dom4j.Element;
import horseracing.treeplayer.NodeVisitor;
import horseracing.treeplayer.TreePlayer;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * 攻破AUC
 * 对于二分类问题，N个样本一共有2**N种答案
 * 每次我的提交有N！种，怎样提交才能最快找到正确答案
 */
public class Main {
int N = 7;
Node root;
//全局变量记录结果
int bestScore;
int maxTry;

void swap(int[] a, int x, int y) {
    int temp = a[x];
    a[x] = a[y];
    a[y] = temp;
}

int auc(int[] a, int solution) {
    int s = 0;
    for (int i = a.length - 1; i >= 0; i--) {
        if ((solution & (1 << i)) != 0) {
            s += a.length - a[i];
        }
    }
    return s;
}

void update(int[] a, Node node) {
    Map<Integer, List<Integer>> cnt = new TreeMap<>();
    for (int solution : node.solutions) {
        int score = auc(a, solution);
//        System.out.println("strategy");
//        debug(a);
//        System.out.println("solution " + solution + " " + score);
//        System.out.println("============");
        List<Integer> son = cnt.getOrDefault(score, new ArrayList<>());
        son.add(solution);
        cnt.put(score, son);
    }
    int s = 0;
    for (List<Integer> i : cnt.values()) {
        s += i.size() * i.size();
    }
    if (s < bestScore) {
        bestScore = s;
        node.strategy = toInt(a);
        node.sons.clear();
        for (int i : cnt.keySet()) {
            node.sons.put(i, new Node(cnt.get(i), i));
        }
    }
}

int toInt(int[] a) {
    int s = 0;
    for (int i = 0; i < a.length; i++) s += a[i] * Math.pow(10, i);
    return s;
}

void debug(int[] a) {
    for (int i = 0; i < a.length; i++) {
        System.out.print(a[i] + " ");
    }
    System.out.println();
}

void permutation(int[] a, int ind, Node node) {
    if (ind == a.length - 1) {
        update(a, node);
        return;
    }
    for (int i = ind; i < a.length; i++) {
        swap(a, ind, i);
        permutation(a, ind + 1, node);
        swap(a, ind, i);
    }
}

void go(Node node, int maxTry) {
    if (node.solutions.size() <= 1) return;
    this.maxTry = Math.max(maxTry, this.maxTry);
    int[] p = new int[N];
    for (int i = 0; i < p.length; i++) p[i] = i;
    bestScore = Integer.MAX_VALUE;
    permutation(p, 0, node);
//    System.out.println(node.strategy + " ================strategy");
//    for (Node i : node.sons.values()) {
//        for (int j : i.solutions) {
//            System.out.print(j + " ");
//        }
//        System.out.println();
//    }
//    try {
//        System.in.read();
//    } catch (IOException e) {
//        e.printStackTrace();
//    }
    for (Node i : node.sons.values()) {
        go(i, maxTry + 1);
    }
}

Main() {
    List<Integer> solutions = new ArrayList<>();
    for (int i = 0; i < (1 << N); i++) {
        solutions.add(i);
    }
    root = new Node(solutions, 0);
    go(root, 1);
    System.out.println("最多尝试" + maxTry);
    TreePlayer.swingControl(new NodeVisitor<Node>() {
        @Override
        public List<Node> getSons(Node node) {
            return new ArrayList<>(node.sons.values());
        }

        String toBinary(int x) {
            StringBuilder s = new StringBuilder();
            for (int i = N - 1; i >= 0; i--) {
                if ((x & (1 << i)) == 0) {
                    s.append('0');
                } else {
                    s.append('1');
                }
            }
            return s.toString();
        }

        @Override
        public String tos(Node node) {
            if (node.solutions.size() == 0) {
                return "若 " + node.order + "则 无解";
            }
            if (node.solutions.size() == 1) {
                return "若 " + node.order + "则 " + toBinary(node.solutions.get(0));
            }
            return "若 " + node.order + "则 剩余解法" + node.solutions.size() + "，采取策略 " + node.strategy;
        }

        @Override
        public Element toElement(Node node) {
            return null;
        }

        @Override
        public Node root() {
            return Main.this.root;
        }
    });
}

public static void main(String[] args) {
    new Main();
}
}
