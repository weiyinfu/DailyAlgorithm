package indexheap;

import java.util.*;

/**
 * 使用平衡树也可以logN实现最小堆
 * <p>
 * 实际上平衡树是更好的堆，平衡树是堆的一种
 * 堆比平衡树高效
 */
public class TreeIndexHeap<T> implements IndexHeap<T> {
TreeSet<Integer> tree;
List<T> a;

TreeIndexHeap(int capacity, Comparator<T> cmp) {
    a = new ArrayList<>(capacity);

    for (int i = 0; i < capacity; i++) a.add(null);
    tree = new TreeSet<>((o1, o2) -> {
//        System.out.println(o1 + " " + o2 + " " + tree.size());
        int res = cmp.compare(a.get(o1), a.get(o2));
        if (res == 0) return o1 - o2;
        return res;
    });
}

@Override
public T peek() {
    if (tree.size() == 0) return null;
    return a.get(tree.first());
}

@Override
public T poll() {
    if (tree.size() == 0) return null;
    Integer index = tree.pollFirst();
    if (index == null) return null;
    return a.get(index);
}

@Override
public T get(int index) {
    return a.get(index);
}

@Override
public void add(int index, T value) {
    a.set(index, value);
    tree.add(index);
}

@Override
public void remove(int index) {
    if (a.get(index) != null) {
        if (tree.contains(index))
            tree.remove(index);
        a.set(index, null);
    }
}

@Override
public void update(int index, T value) {
    tree.remove(index);
    a.set(index, value);
    tree.add(index);
}

@Override
public boolean isEmpty() {
    return tree.size() == 0;
}

@Override
public int size() {
    return tree.size();
}

public static void main(String[] args) {
    Scanner cin = new Scanner(System.in);
    int n = cin.nextInt(), m = cin.nextInt();
    TreeIndexHeap<Integer> q = new TreeIndexHeap<>(m, Comparator.comparing(x -> x));
    while (n-- > 0) {
        String op = cin.next();
        if (op.equals("add")) {
            int index = cin.nextInt(), value = cin.nextInt();
            q.add(index, value);
        } else if (op.equals("update")) {
            int index = cin.nextInt(), value = cin.nextInt();
            q.update(index, value);
        } else if (op.equals("peek")) {
            Integer v = q.peek();
            if (v == null) {
                System.out.println(-1);
                continue;
            }
            System.out.println(v);
        } else if (op.equals("poll")) {
            Integer v = q.poll();
            if (v == null) {
                System.out.println(-1);
                continue;
            }
            System.out.println(v);
        } else if (op.equals("remove")) {
            q.remove(cin.nextInt());
        } else {
            throw new RuntimeException("unkown op " + op);
        }
    }
}
}
