import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Collectors;

//评判器
public class Judger {
final static InputStream stdin = System.in;
final static PrintStream stdout = System.out;

public static void judge(Class<?> bruteforce, Class<?> mine, Generator generator) {
    try {
        while (true) {
            if (!generator.generateProblem()) break;
            System.setIn(new FileInputStream("in.txt"));
            System.setOut(new PrintStream(new FileOutputStream("out1.txt")));
            bruteforce.getMethod("main", String[].class).invoke(bruteforce, (Object) new String[]{});
            System.setIn(new FileInputStream("in.txt"));
            System.setOut(new PrintStream(new FileOutputStream("out2.txt")));
            mine.getMethod("main", String[].class).invoke(mine, (Object) new String[]{});
            System.setIn(stdin);
            System.setOut(stdout);
            String rightAns = Files.readAllLines(Paths.get("out1.txt")).stream().collect(Collectors.joining("\n"));
            String myAns = Files.readAllLines(Paths.get("out2.txt")).stream().collect(Collectors.joining("\n"));
            if (!rightAns.equals(myAns)) {
                System.err.println("error");
                System.exit(-1);
            }
        }
        System.out.println("accepted");
    } catch (Exception e) {
        e.printStackTrace();
    }
}

public static void main(String[] args) {
    judge(TreeIndexHeap.class, RemoveIndexHeap.class, new Generator());
}
}
