package indexheap.trie;

import java.util.Map;
import java.util.Random;
import java.util.TreeMap;

public class Test {
static final Random r = new Random(0);
static final int n = 100, strLength = 5;

static String randomString(int length) {
    StringBuilder builder = new StringBuilder(length);
    for (int i = 0; i < length; i++) {
        builder.append((char) ('a' + r.nextInt(26)));
    }
    return builder.toString();
}

static void go(Trie<Integer> tr, Map<String, Integer> a) {
    for (Map.Entry<String, Integer> i : a.entrySet()) {
        Integer v = tr.query(i.getKey());
        if (v == null || !v.equals(i.getValue())) {
            throw new RuntimeException(String.format("该来的没来 %s", i.getKey()));
        }
    }
    for (int i = 0; i < n; i++) {
        String s = randomString(r.nextInt(strLength) + 1);
        if (a.containsKey(s)) continue;
        if (tr.query(s) != null) {
            throw new RuntimeException("不该来的来了");
        }
    }
}

public static void main(String[] args) {
    Map<String, Integer> a = new TreeMap<>();
    for (int i = 0; i < n; i++) a.put(randomString(r.nextInt(strLength) + 1), i);
    for (String i : a.keySet()) {
        System.out.println(i);
    }
    Trie<Integer> tr = new Dart<>(a);
//    Trie<Integer> tr = new ArrayTrie<>(a);
    go(tr, a);
}
}
