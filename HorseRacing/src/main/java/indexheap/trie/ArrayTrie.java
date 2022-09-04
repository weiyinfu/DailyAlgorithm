package trie;

import java.util.*;

public class ArrayTrie<V> implements Trie<V> {

class Node {
    List<Node> sons;
    V v;
}

Node root;

ArrayTrie(Map<String, V> a) {
    root = new Node();
    for (Map.Entry<String, V> i : a.entrySet()) {
        insert(i.getKey(), i.getValue());
    }
}

void insert(String k, V v) {
    Node now = root;
    for (int i = 0; i < k.length(); i++) {
        int pos = k.charAt(i) - 'a';
        if (now.sons == null) {
            now.sons = new ArrayList<>(26);
            for (int sonIndex = 0; sonIndex < 26; sonIndex++) {
                now.sons.add(null);
            }
        }
        if (now.sons.get(pos) == null) {
            now.sons.set(pos, new Node());
        }
        now = now.sons.get(pos);
    }
    now.v = v;
}

public V query(String s) {
    Node now = root;
    for (int i = 0; i < s.length(); i++) {
        int pos = s.charAt(i) - 'a';
        if (now.sons == null) return null;
        if (now.sons.get(pos) == null) return null;
        now = now.sons.get(pos);
    }
    return now.v;
}

}
