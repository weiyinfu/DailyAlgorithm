package horseracing.balance;

import java.util.List;

public interface SelectVisitor {
    void handle(List<Integer> chosen);
}
