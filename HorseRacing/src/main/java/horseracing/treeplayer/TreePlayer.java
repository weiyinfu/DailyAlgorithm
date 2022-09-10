package horseracing.treeplayer;


public class TreePlayer {
    public static <T> void xml(NodeVisitor<T> visitor, String filename) {
        new XmlPlayer<>(visitor).exportXML(filename);
    }

    public static <T> String filestyle(NodeVisitor<T> visitor) {
        return new StringPlayer<>(visitor).fileStyle();
    }

    public static <T> void swingControl(NodeVisitor<T> visitor) {
        new SwingTreeControlPlayer<>(visitor);
    }
}