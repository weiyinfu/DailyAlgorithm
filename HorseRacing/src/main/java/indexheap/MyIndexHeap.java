package indexheap;

import java.util.*;

public class MyIndexHeap<T> implements IndexHeap<T> {
int[] q;//堆
List<T> a;//存放元素值
int[] ind;//存放元素在堆中的下标
Comparator<T> cmp;//元素比较函数
int qsize;//堆的当前大小

/**
 * index的取值范围必须在[1,q.length)之间
 */
MyIndexHeap(int capacity, Comparator<T> cmp) {
    q = new int[capacity];
    qsize = 1;//下标从1开始
    this.cmp = cmp;
    a = new ArrayList<>(capacity);
    for (int i = 0; i < capacity; i++) a.add(null);
    ind = new int[capacity];
    Arrays.fill(ind, -1);//-1表示不包含此元素
}

//下标检查，堆的下标从1开始
void checkIndex(int index) {
    if (index <= 0 || index > ind.length) throw new RuntimeException("invalid index " + index);
}

//比较函数，如果相等则比较index，这样可以确保输出值是确定的，不会出现乱序
int compare(int indexA, int indexB) {
    int res = cmp.compare(a.get(indexA), a.get(indexB));
    if (res == 0) return indexA - indexB;
    return res;
}

//交换堆中的两个元素
void swap(int x, int y) {
    if (x == y) return;
    int temp = q[x];
    q[x] = q[y];
    q[y] = temp;
    ind[q[x]] = x;
    ind[q[y]] = y;
}

void shiftDown(int index) {
    int pos = ind[index];
    while (pos < qsize) {
        int left = pos << 1, right = pos << 1 | 1;
        if (left >= qsize && right >= qsize) break;//已经旋转到底了
        int swapping = left;
        if (right < qsize && compare(q[right], q[left]) < 0) swapping = right;
        //无需再往下了
        if (compare(q[swapping], q[pos]) > 0) break;
        swap(swapping, pos);
        pos = swapping;
    }
}

//元素上移只需要跟自己的父节点比较即可
void shiftUp(int index) {
    int pos = ind[index];
    while (true) {
        int parent = pos >> 1;
        if (parent == 0) break;
        if (compare(q[parent], q[pos]) < 0) break;
        swap(pos, parent);
        pos = parent;
    }
}

@Override
public T peek() {
    if (qsize == 1) return null;
    int index = q[1];
    return a.get(index);
}

/**
 * 弹出堆顶元素
 */
@Override
public T poll() {
    if (qsize == 1) return null;
    int index = q[1];
    T value = a.get(index);
    remove(index);//移除在q[1]处的元素
    return value;
}

@Override
public T get(int index) {
    checkIndex(index);
    return a.get(index);
}

/**
 * 添加元素，统一收敛到update
 */
@Override
public void add(int index, T value) {
    update(index, value);
}

/**
 * 删除index元素
 */
@Override
public void remove(int index) {
    checkIndex(index);
    int pos = ind[index];
    if (pos == -1) return;
    int compareRes = compare(index, q[qsize - 1]);
    swap(qsize - 1, pos);//把要移除的元素跟最后一个元素交换位置
    ind[index] = -1;
    a.set(index, null);
    qsize--;
    if (pos < qsize) {//如果删除的元素是最后一个元素，那么不需要往下走了
        //如果最后一个元素比删除的元素大，则下移之，否则上移之，相等则不移动
        if (compareRes < 0) {
            shiftDown(q[pos]);
        } else {
            shiftUp(q[pos]);
        }
    }
}

@Override
public void update(int index, T value) {
    checkIndex(index);
    if (ind[index] == -1) {//如果元素不存在，则创建之
        a.set(index, value);
        if (qsize >= q.length) {
            throw new RuntimeException("heap capacity overflow");
        }
        int pos = qsize++;
        ind[index] = pos;
        q[pos] = index;
        shiftUp(index);
    } else {
        int res = cmp.compare(a.get(index), value);
        a.set(index, value);
        if (res > 0) {
            shiftUp(index);
        } else if (res < 0) {
            shiftDown(index);
        }
    }
}

@Override
public boolean isEmpty() {
    return size() == 1;
}

@Override
public int size() {
    return qsize;
}


public static void main(String[] args) {
    Scanner cin = new Scanner(System.in);
    int opCount = cin.nextInt(), capacity = cin.nextInt();
    MyIndexHeap<Integer> q = new MyIndexHeap<>(capacity, Comparator.comparing(x -> x));
    for (int i = 0; i < opCount; i++) {
        String op = cin.next();
//        q.show();
        if (op.equals("add")) {
            int index = cin.nextInt(), value = cin.nextInt();
            q.add(index, value);
        } else if (op.equals("update")) {
            int index = cin.nextInt(), value = cin.nextInt();
            q.update(index, value);
        } else if (op.equals("remove")) {
            int index = cin.nextInt();
            q.remove(index);
        } else if (op.equals("peek")) {
            Integer x = q.peek();
            System.out.println(x == null ? -1 : x);
        } else if (op.equals("poll")) {
            Integer x = q.poll();
            System.out.println(x == null ? -1 : x);
        } else {
            throw new RuntimeException("unkonwn op " + op);
        }
    }
}
}
