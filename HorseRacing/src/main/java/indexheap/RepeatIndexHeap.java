import java.util.*;

/**
 * 使用最简单的方式实现索引堆
 * 堆中元素可重复，但是不是每个元素都有效
 * 这种方法的优点在于实现简单，缺点在于堆中存在重复元素
 * <p>
 * 为了辨别堆中元素是否为最新版本，使用version数组来记录变量，每次更新都会更新此变量
 */
public class RepeatIndexHeap<T> implements IndexHeap<T> {
class Node {
    int index;
    int version;
    T value;

    Node(int index, T value, int tag) {
        this.index = index;
        this.version = tag;
        this.value = value;
    }
}

PriorityQueue<Node> q;
List<T> a;
int[] tag;//存储每个结点的最新状态

RepeatIndexHeap(int capacity, Comparator<T> cmp) {
    this.q = new PriorityQueue<>(capacity, (Comparator<Node>) (o1, o2) -> {
        int res = cmp.compare(o1.value, o2.value);
        if (res == 0) return o1.index - o2.index;
        return res;
    });
    a = new ArrayList<>(capacity);
    for (int i = 0; i < capacity; i++) a.add(null);
    tag = new int[capacity];
}

public void add(int index, T value) {
    a.set(index, value);
    tag[index] += 1;
    q.add(new Node(index, value, tag[index]));
}

@Override
public void remove(int index) {
    tag[index] += 1;
}

public void update(int index, T value) {
    a.set(index, value);
    tag[index] += 1;
    q.add(new Node(index, value, tag[index]));
}

@Override
public boolean isEmpty() {
    return size() == 0;
}

@Override
public int size() {
    return q.size();
}


@Override
public T get(int index) {
    return a.get(index);
}

@Override
public T peek() {
    if (q.isEmpty()) return null;
    while (!q.isEmpty()) {
        Node i = q.peek();
        if (tag[i.index] != i.version) {
            q.poll();
            continue;
        }
        return a.get(i.index);
    }
    return null;
}

@Override
public T poll() {
    if (q.isEmpty()) return null;
    while (!q.isEmpty()) {
        Node i = q.poll();
        if (tag[i.index] != i.version) continue;
        return a.get(i.index);
    }
    return null;
}

public static void main(String[] args) {
    Scanner cin = new Scanner(System.in);
    int n = cin.nextInt(), m = cin.nextInt();
    RepeatIndexHeap<Integer> q = new RepeatIndexHeap<>(m, Comparator.comparing(x -> x));
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
