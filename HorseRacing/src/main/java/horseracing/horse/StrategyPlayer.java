package horseracing.horse;

import org.dom4j.DocumentHelper;
import org.dom4j.Element;
import horseracing.treeplayer.NodeVisitor;
import horseracing.treeplayer.TreePlayer;

import java.util.ArrayList;
import java.util.List;

/**
 * 决策演示器，给定一个决策二叉树，形象的展示结果
 */
public class StrategyPlayer {
    Pair[] tree;

    NodeVisitor<Integer> visitor = new NodeVisitor<Integer>() {
        boolean valid(int x) {
            return x < tree.length && tree[x] != null;
        }

        @Override
        public List<Integer> getSons(Integer x) {
            List<Integer> sons = new ArrayList<>();
            if (valid(x << 1)) sons.add(x << 1);
            if (valid(x << 1 | 1)) sons.add(x << 1 | 1);
            return sons;
        }

        @Override
        public String tos(Integer integer) {
            return tree[integer].x + "," + tree[integer].y;
        }

        @Override
        public Element toElement(Integer x) {
            Element e = DocumentHelper.createElement((x & 1) == 0 ? "if" : "else");
            e.addAttribute("x", tree[x].x + "");
            e.addAttribute("y", tree[x].y + "");
            return e;
        }

        @Override
        public Integer root() {
            return 1;
        }
    };

    public String fileStyle() {
        return TreePlayer.filestyle(visitor);
    }

    public void xml() {
        TreePlayer.xml(visitor, "horse.xml");
    }

    public void swingControl() {
        TreePlayer.swingControl(visitor);
    }

    StrategyPlayer(Pair[] tree) {
        this.tree = tree;
    }
}
