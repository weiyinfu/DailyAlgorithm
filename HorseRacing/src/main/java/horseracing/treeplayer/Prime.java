package horseracing.treeplayer;

import org.dom4j.Element;

import java.util.ArrayList;
import java.util.List;

public class Prime {
int n = 100;
List<List<Integer>> a = new ArrayList<>();

Prime() {
    for (int i = 0; i < n; i++) a.add(new ArrayList<>());
    List<Integer> primes = new ArrayList<>();
    boolean is[] = new boolean[n];
    for (int i = 0; i < n; i++) is[i] = true;
    for (int i = 2; i < n; i++) {
        if (is[i]) {
            primes.add(i);
        }
        for (int j = 0; j < primes.size() && i * primes.get(j) < n; j++) {
            is[i * primes.get(j)] = false;
            a.get(i).add(i * primes.get(j));
            if (i % primes.get(j) == 0) break;
        }
    }
    TreePlayer.swingControl(new NodeVisitor<Integer>() {
        @Override
        public List<Integer> getSons(Integer integer) {
            if (integer == 1) {
                return primes;
            }
            return a.get(integer);
        }

        @Override
        public String tos(Integer integer) {
            return integer + "";
        }

        @Override
        public Element toElement(Integer integer) {
            return null;
        }

        @Override
        public Integer root() {
            return 1;
        }
    });
}

public static void main(String[] args) {
    new Prime();
}
}
