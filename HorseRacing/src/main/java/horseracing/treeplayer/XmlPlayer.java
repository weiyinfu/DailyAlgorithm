package horseracing.treeplayer;

import org.dom4j.Document;
import org.dom4j.DocumentHelper;
import org.dom4j.Element;

import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.util.List;

public class XmlPlayer<T> {
NodeVisitor<T> visitor;

Element createXML(T x) {
    Element e = visitor.toElement(x);
    List<T> sons = visitor.getSons(x);
    for (T son : sons) {
        e.add(createXML(son));
    }
    return e;
}

void exportXML(String filename) {
    try {
        Document doc = DocumentHelper.createDocument();
        doc.add(createXML(visitor.root()));
        Writer writer = new FileWriter(filename);
        doc.write(writer);
        writer.close();
    } catch (IOException e) {
        e.printStackTrace();
    }
}

XmlPlayer(NodeVisitor<T> visitor) {
    this.visitor = visitor;
}
}
