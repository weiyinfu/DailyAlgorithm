package indexheap;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * priorityQueue有remove函数
 * 每次更新的时候，只需要把旧的值移除，把新值插入
 */
public class RemoveIndexHeap<T> implements IndexHeap<T> {
PriorityQueue<Integer> q;
ArrayList<T> a;

RemoveIndexHeap(int capacity, Comparator<T> cmp) {
    q = new PriorityQueue<>(capacity, (o1, o2) -> {
        int res = cmp.compare(a.get(o1), a.get(o2));
        if (res == 0) return o1 - o2;
        return res;
    });
    a = new ArrayList<>(capacity);
    for (int i = 0; i < capacity; i++) a.add(null);
}

public T poll() {
    if (q.isEmpty()) return null;
    int index = q.poll();
    return a.get(index);
}

public T peek() {
    if (q.isEmpty()) return null;
    return a.get(q.peek());
}

public T get(int index) {
    return a.get(index);
}

public void add(int index, T value) {
    a.set(index, value);
    q.add(index);
}

public void update(int index, T value) {
    //这个remove操作极为费时，复杂度为O(N),N表示队列中元素个数
    q.remove(index);
    a.set(index, value);
    q.add(index);
}

@Override
public boolean isEmpty() {
    return size() == 0;
}

@Override
public int size() {
    return q.size();
}

public void remove(int index) {
    a.set(index, null);
    q.remove(index);
}

public static void main(String[] args) {
    Scanner cin = new Scanner(System.in);
    int n = cin.nextInt(), m = cin.nextInt();
    RemoveIndexHeap<Integer> q = new RemoveIndexHeap<Integer>(m, Comparator.comparing(x -> x));
    while (n-- > 0) {
        String op = cin.next();
        if (op.equals("add")) {
            int index = cin.nextInt(), value = cin.nextInt();
            q.add(index, value);
        } else if (op.equals("update")) {
            int index = cin.nextInt(), value = cin.nextInt();
            q.update(index, value);
        } else if (op.equals("peek")) {
            Object v = q.peek();
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
            throw new RuntimeException("unkown op");
        }
    }
}
}
