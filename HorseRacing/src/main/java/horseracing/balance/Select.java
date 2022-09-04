package horseracing.balance;

import java.util.ArrayList;
import java.util.List;

//从一堆int中选择k个int，通过selectVisitor进行访问
public class Select {
List<Integer> f;
int cnt;
SelectVisitor v;

void go(int index, List<Integer> now) {
    if (now.size() == cnt) {
        v.handle(now);
        return;
    }
    if (index >= f.size()) return;
    now.add(f.get(index));
    go(index + 1, now);
    now.remove(now.size() - 1);
    go(index + 1, now);
}

Select(List<Integer> f, int cnt, SelectVisitor visitor) {
    this.f = f;
    this.cnt = cnt;
    this.v = visitor;
    go(0, new ArrayList<>());
}
}
