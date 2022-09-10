package horseracing.treeplayer;

import java.util.List;

public class StringPlayer<T> {
    NodeVisitor<T> visitor;

    String fileStyle() {
        return fileStyle("", visitor.root());
    }

    public String fileStyle(String prefix, T x) {
        StringBuilder builder = new StringBuilder();
        builder.append(prefix).append(visitor.tos(x)).append("\n");
        List<T> sons = visitor.getSons(x);
        if (sons.size() == 0) return builder.toString();
        String temp = prefix.replace('┣', '┃');
        temp = temp.replace("━", "  ");
        temp = temp.replace("┗", "  "); //一定要注意，一个这个符号是两个空格
        for (int i = 0; i < sons.size() - 1; i++) {
            builder.append(fileStyle(temp + "┣━", sons.get(i)));
        }
        builder.append(fileStyle(temp + "┗━", sons.get(sons.size() - 1)));
        return builder.toString();
    }

    StringPlayer(NodeVisitor<T> visitor) {
        this.visitor = visitor;
    }
}
