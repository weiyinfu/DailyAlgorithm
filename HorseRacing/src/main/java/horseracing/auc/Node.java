package horseracing.auc;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Node {
public List<Integer> solutions;
public Map<Integer, Node> sons;
public int strategy;
public int order;//我的排名

public Node(List<Integer> solutions, int order) {
    this.solutions = solutions;
    this.sons = new HashMap<>();
    this.order = order;
}
}
