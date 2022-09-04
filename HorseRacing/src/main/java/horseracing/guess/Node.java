package horseracing.guess;

import java.util.List;

public class Node {
public List<Integer> solutions;
public Node[] sons;
public int strategy;
public int order;//我的排名

public Node(List<Integer> solutions, int N, int order) {
    this.solutions = solutions;
    this.sons = new Node[N + 1];
    this.order = order;
}
}
