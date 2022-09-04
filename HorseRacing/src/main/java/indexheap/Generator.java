import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.Random;
import java.util.stream.Collectors;

/**
 * 数据生成器
 */
public class Generator {
protected PrintStream cout;
public Random random = new Random(0);

public int randInt(int from, int toExcluded) {
    return random.nextInt(toExcluded - from) + from;
}

public void print(Object... args) {
    cout.println(Arrays.stream(args).map(Object::toString).collect(Collectors.joining(" ")));
}

int cnt = 0;

public boolean generate() {
    if (cnt == 1000) {
        return false;
    }
    cnt++;
    int n = randInt(3, 500);//操作个数
    int m = randInt(3, 100);//数组大小
    print(n, m);
    boolean added[] = new boolean[m];
    int valueRange = 100;
    for (int i = 0; i < n; i++) {
        int op = randInt(0, 5);
        if (op == 0 || op == 3) {
            int index = randInt(1, m);
            if (added[index]) {
                print("update", index, randInt(0, valueRange));
            } else {
                added[index] = true;
                print("add", index, randInt(0, valueRange));
            }
        } else if (op == 1) {
            print("peek");
        } else if (op == 2) {
            int index = randInt(1, m);
            if (added[index]) added[index] = false;
            print("remove", index);
        } else {
            print("poll");
        }
    }
    return true;
}

public boolean generateProblem() {
    try {
        cout = new PrintStream(new FileOutputStream("in.txt"));
        boolean over = generate();
        cout.close();
        return over;
    } catch (FileNotFoundException e) {
        e.printStackTrace();
    }
    return true;
}
}
