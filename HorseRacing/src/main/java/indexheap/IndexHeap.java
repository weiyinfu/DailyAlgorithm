package indexheap;

public interface IndexHeap<T> {
T peek();

T poll();

T get(int index);

void add(int index, T value);

void remove(int index);

void update(int index, T value);

boolean isEmpty();

int size();
}

