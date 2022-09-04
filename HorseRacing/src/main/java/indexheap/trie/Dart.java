package trie;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Dart<V> implements Trie<V> {
class Node {
    int id;
    int base;//每个结点的儿子们的起始位置base
    int father;//每个结点的father
    V value;//每个结点的value
    boolean used = false;//此Node是否已被利用
}


List<Node> a;
int freePos = 1;

Dart(Map<String, V> a) {
    int n = 100;
    this.a = new ArrayList<>(n);
    for (int i = 0; i < n; i++) this.a.add(new Node());
    init(this.a, 0, n);
    insert(0, 0, 0, new LinkedList<Map.Entry<String, V>>(a.entrySet()));
}

void init(List<Node> a, int beg, int end) {
    for (int i = beg; i < end; i++) {
        Node node = a.get(i);
        node.id = i;
        node.used = false;
    }
}

void insert(int father, int nodeId, int depth, List<Map.Entry<String, V>> a) {
    List<List<Map.Entry<String, V>>> next = new ArrayList<>(26);
    for (int i = 0; i < 26; i++) next.add(null);
    V v = null;
    for (Map.Entry<String, V> i : a) {
        if (i.getKey().length() == depth) {//没有更多了
            v = i.getValue();
            continue;
        }
        if (i.getKey().length() <= depth) throw new RuntimeException("key is too short here");
        int pos = i.getKey().charAt(depth) - 'a';
        if (next.get(pos) == null) next.set(pos, new LinkedList<>());
        next.get(pos).add(i);
    }
    Node node = this.a.get(nodeId);
    node.father = father;
    node.value = v;
    node.used=true;
    int maxValidIndex = 0, minValidIndex = 25;
    for (int i = 0; i < next.size(); i++) {
        if (next.get(i) != null && next.get(i).size() > 0) {
            maxValidIndex = Math.max(maxValidIndex, i);
            minValidIndex = Math.min(minValidIndex, i);
        }
    }
    int validSonRange = maxValidIndex - minValidIndex + 1;
    if (validSonRange < 0) return;//没有儿子
    boolean pattern[] = new boolean[validSonRange];
    for (int i = minValidIndex; i <= maxValidIndex; i++) {
        pattern[i - minValidIndex] = next.get(i) != null && next.get(i).size() > 0;
    }
    int pos = allocate(pattern);//当前结点的儿子们的位置
    node.base = pos - minValidIndex;
    for (int i = 0; i < next.size(); i++) {
        if (next.get(i) == null || next.get(i).size() == 0) continue;
        //此处应该改为非递归形式
        insert(node.id, node.base + i, depth + 1, next.get(i));
    }
}

int allocate(boolean[] pattern) {
    int range = pattern.length;
    if (this.freePos + range >= this.a.size()) {
        int bsize = this.a.size() * 2;
        List<Node> b = new ArrayList<>(bsize);
        b.addAll(a);
        for (int i = a.size(); i < bsize; i++) {
            b.add(new Node());
        }
        //初始化新加入的空间
        init(b, a.size(), b.size());
        this.a = b;
    }
    int goodPos = freePos;
    freePos += range;
    return goodPos;
}

public V query(String k) {
    Node now = a.get(0);
    for (int i = 0; i < k.length(); i++) {
        int pos = k.charAt(i) - 'a';
        if (now == null) return null;
        if (now.base + pos >= a.size() || now.base + pos < 0) return null;
        Node son = a.get(now.base + pos);
        if (son.father != now.id) return null;//不是我的儿子
        now = son;
    }
    return now.value;
}
}
