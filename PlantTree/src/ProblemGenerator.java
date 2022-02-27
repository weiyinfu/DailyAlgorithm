import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Random;

public class ProblemGenerator {
static class Desc {
    int MAX_TREE;
    int MAX_COLOR;
    int MAX_COST;
    int CASE_COUNT;

    Desc(int maxTree, int maxColor, int maxCost, int caseCount) {
        this.MAX_COLOR = maxColor;
        this.MAX_COST = maxCost;
        this.CASE_COUNT = caseCount;
        this.MAX_TREE = maxTree;
    }
}

final static Desc production = new Desc(100, 10, 50, 100);
final static Desc development = new Desc(5, 5, 10, 15);
Random r = new Random();

int rand(int beg, int end) {
    return r.nextInt(end - beg) + beg;
}

ProblemGenerator(Desc desc) throws FileNotFoundException {
    int casCount = desc.CASE_COUNT;
    PrintWriter cout = new PrintWriter("in.txt");
    cout.println(casCount);
    while (casCount-- > 0) {
        cout.println();
        int treeCount = rand(1, desc.MAX_TREE);
        int colorCount = rand(1, desc.MAX_COLOR);
        int forestCount = rand(1, treeCount + 1);
        cout.printf("%d %d %d\n", treeCount, colorCount, forestCount);
        for (int i = 0; i < treeCount; i++) {
            for (int j = 0; j < colorCount; j++) {
                cout.printf("%d ", rand(0, desc.MAX_COST));
            }
            cout.println();
        }
    }
    cout.close();
}

public static void main(String[] args) throws FileNotFoundException {
    new ProblemGenerator(ProblemGenerator.production);
//    new ProblemGenerator(ProblemGenerator.development);
}
}
