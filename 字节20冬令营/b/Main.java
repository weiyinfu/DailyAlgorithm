import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.TreeSet;

class Main {
    List<TreeSet<Integer>> edges;
    int[] a;
    int[] target;

    void add(int f, int t) {
        //添加一条边
        if (edges.get(f).contains(t)) {
            return;
        }
        edges.get(f).add(t);
        a[f]++;
        a[t]++;
    }

    Main() throws IOException {
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        int nodeCount = 0;
        for (int i = 1; i <= n; i++) {
            nodeCount += i;
        }
        edges = new ArrayList<>(nodeCount);
        for (int i = 0; i < nodeCount; i++)
            edges.add(new TreeSet<>());
        a = new int[nodeCount];
        target = new int[nodeCount];
        int k = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < n + 1 - i; j++) {
                target[k++] = n + 1 - i;
            }
        }
        //开干
        k = 0;
        for (int i = 0; i < nodeCount; i++) {
            if (k <= i) k = i + 1;
            while (k < nodeCount && a[i] < target[i]) {
                if (a[k] < target[k]) {
                    add(i, k);
                }
                k++;
            }
        }
//        show();
        //第一轮结束，已经变成了连通图
        for (int i = 0; i < nodeCount; i++) {
            for (int j = i + 1; j < nodeCount && a[i] < target[i]; j++) {
                if (a[j] < target[j]) {
                    add(i, j);
                }
            }
        }
        output();
    }

    boolean same() {
        for (int i = 0; i < a.length; i++) {
            if (a[i] != target[i]) {
                return false;
            }
        }
        return true;
    }

    void show() {
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + ",");
        }
        System.out.println();
        for (int i = 0; i < a.length; i++) {
            System.out.print(target[i] + ",");
        }
        System.out.println();
    }

    void output() throws IOException {
        BufferedWriter cout = new BufferedWriter(new OutputStreamWriter(System.out));
        if (same()) {
            for (int i = 0; i < edges.size(); i++) {
                for (int j : edges.get(i)) {
                    cout.write((i + 1) + " " + (j + 1) + "\n");
                }
            }
        } else {
            cout.write(-1 + "\n");
        }
        cout.close();
    }

    public static void main(String[] args) throws IOException {
        new Main();
    }
}