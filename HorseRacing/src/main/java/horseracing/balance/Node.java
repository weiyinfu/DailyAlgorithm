package horseracing.balance;

import java.util.List;

public class Node {
    //三种结果对应三种决策
    Node[] sons = new Node[3];
    List<Integer> solutions;
    Strategy strategy;
    int order;//排行

    Node(List<Integer> solutions, int order) {
        this.solutions = solutions;
        this.order = order;
    }
}
