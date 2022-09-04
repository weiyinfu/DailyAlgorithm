package eightqueen;

public class SingleThreadQueen {
//单线程8皇后
class Node {
    int vertical, leftFail, rightFail;

    Node(int vertical, int leftFail, int rightFail) {
        this.vertical = vertical;
        this.leftFail = leftFail;
        this.rightFail = rightFail;
    }
}

int go(int N) {
    //描述竖直/撇/捺三种情况的占用情况
    long vertical = 0, leftFail = 0, rightFail = 0;

    //求每个结点的竖直/撇/捺对应的值
    Node[][] a = new Node[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            a[i][j] = new Node(j, i + j, i + N - j);
        }
    }
    int cnt = 0;
    int q[] = new int[N+1];//q[i]表示第i行放在哪里
    int qi = 0;
    q[qi++] = 0;
    while (qi > 0) {
        int col = q[--qi];
        int row = qi;
        if (col == N || qi == N) {
            if (qi == N) cnt++;
            if (qi == 0) break;
            //undo operation
            col = q[--qi];
            row = qi;
            if (row >= 0) {
                vertical &= ~(1 << a[row][col].vertical);
                leftFail &= ~(1 << a[row][col].leftFail);
                rightFail &= ~(1 << a[row][col].rightFail);
            }
            q[qi++] = col + 1;
            continue;
        }
        if ((vertical & (1 << a[row][col].vertical)
                | leftFail & (1 << a[row][col].leftFail)
                | rightFail & (1 << a[row][col].rightFail)) == 0) {
            //if can put , then put it
            vertical |= 1 << a[row][col].vertical;
            leftFail |= 1 << a[row][col].leftFail;
            rightFail |= 1 << a[row][col].rightFail;
            q[qi++] = col;//reput current queen
            q[qi++] = 0;//put next line
        } else {
            q[qi++] = col + 1;
        }
    }
    return cnt;
}

SingleThreadQueen() {
    for (int i = 1; i < 17; i++) {
        long beg = System.currentTimeMillis();
        System.out.println(i + "=" + go(i) + ",time=" + (System.currentTimeMillis() - beg) + "ms");
    }
}

public static void main(String[] args) {
    new SingleThreadQueen();
}
}
