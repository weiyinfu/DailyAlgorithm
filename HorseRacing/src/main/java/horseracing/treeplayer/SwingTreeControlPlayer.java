package horseracing.treeplayer;

import java.awt.*;
import java.util.Enumeration;

import javax.swing.*;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.*;


public class SwingTreeControlPlayer<T> extends JFrame implements TreeSelectionListener {
    private DefaultTreeModel treeModel;
    NodeVisitor<T> visitor;

    DefaultMutableTreeNode buildNodes(T t) {
        DefaultMutableTreeNode node = new DefaultMutableTreeNode(visitor.tos(t));
        for (T son : visitor.getSons(t)) {
            node.add(buildNodes(son));
        }
        return node;
    }

    public SwingTreeControlPlayer(NodeVisitor<T> visitor) {
        this.visitor = visitor;
        this.setSize(200, 150);


        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int x = (screenSize.width - this.getSize().width) / 2;
        int y = (screenSize.height - this.getSize().height) / 2;
        this.setLocation(x, y);
        this.setExtendedState(MAXIMIZED_BOTH);

        treeModel = new DefaultTreeModel(buildNodes(visitor.root()));
        JTree tree = new JTree(treeModel);
        tree.setBackground(Color.BLACK);
        tree.getSelectionModel().setSelectionMode(TreeSelectionModel.SINGLE_TREE_SELECTION);
        tree.expandPath(new TreePath(treeModel.getRoot()));
        tree.setEditable(false);
        tree.setCellRenderer(new TreeCellRenderer() {
            @Override
            public Component getTreeCellRendererComponent(JTree tree, Object value, boolean selected, boolean expanded, boolean leaf, int row, boolean hasFocus) {
                JLabel label = new JLabel(value.toString());
                label.setBackground(Color.BLACK);
                label.setForeground(Color.WHITE);
                label.setFont(new Font("楷体", Font.BOLD, 20));
                return label;
            }
        });
        expandAll(tree, new TreePath(treeModel.getRoot()), true);
        this.add(new JScrollPane(tree));
        this.setVisible(true);
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }

    // 展开树的所有节点的方法
    private static void expandAll(JTree tree, TreePath parent, boolean expand) {
        TreeNode node = (TreeNode) parent.getLastPathComponent();
        if (node.getChildCount() >= 0) {
            for (Enumeration e = node.children(); e.hasMoreElements(); ) {
                TreeNode n = (TreeNode) e.nextElement();
                TreePath path = parent.pathByAddingChild(n);
                expandAll(tree, path, expand);
            }
        }
        if (expand) {
            tree.expandPath(parent);
        } else {
            tree.collapsePath(parent);
        }
    }

    public void valueChanged(TreeSelectionEvent e) {

    }
}