package horseracing.treeplayer;

import org.dom4j.Element;

import java.util.List;

public interface NodeVisitor<T> {
    List<T> getSons(T t);

    String tos(T t);

    Element toElement(T t);

    T root();
}
