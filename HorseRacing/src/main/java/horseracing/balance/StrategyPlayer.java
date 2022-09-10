package horseracing.balance;

import org.dom4j.DocumentHelper;
import org.dom4j.Element;
import horseracing.treeplayer.NodeVisitor;
import horseracing.treeplayer.TreePlayer;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class StrategyPlayer {

    Node root;
    boolean heavy = false;
    int n;

    NodeVisitor<Node> visitor = new NodeVisitor<Node>() {
        @Override
        public List<Node> getSons(Node node) {
            return Arrays.stream(node.sons).filter(Objects::nonNull).collect(Collectors.toList());
        }

        @Override
        public String tos(Node node) {
            StringBuilder builder = new StringBuilder();
            builder.append("平左右".charAt(node.order)).append(' ');
            if (node.strategy == null) {
                if (node.solutions.size() == 0) builder.append("error");
                else {
                    builder.append(node.solutions.get(0) % n);
                    if (!heavy) {
                        builder.append(node.solutions.get(0) >= n ? "偏重" : "偏轻");
                    }
                }
            } else {
                builder.append(node.strategy).append(' ');
                builder.append("[").append(node.solutions.size()).append("]");
            }
            return builder.toString();
        }

        @Override
        public Element toElement(Node node) {
            Element e = DocumentHelper.createElement("if");
            e.addAttribute("result", "平左右".charAt(node.order) + "");
            if (node.strategy == null) {
                if (node.solutions.size() == 0) e.addAttribute("state", "error");
                else {
                    e.addAttribute("state", node.solutions.get(0) % n + "");
                    if (!heavy) {
                        e.addAttribute("type", node.solutions.get(0) >= n ? "heavy" : "light");
                    }
                }
            } else {
                e.addAttribute("strategy", node.strategy.toString());
            }
            return e;
        }

        @Override
        public Node root() {
            return root;
        }
    };

    StrategyPlayer(Node root, boolean heavy, int n) {
        this.root = root;
        this.heavy = heavy;
        this.n = n;
        String s = TreePlayer.filestyle(visitor);
        System.out.println(s);
        TreePlayer.xml(visitor, "balance.xml");
        TreePlayer.swingControl(visitor);
    }

}
