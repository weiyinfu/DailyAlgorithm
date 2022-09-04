package horsecontrol;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * 不考虑憋腿则不利于剪枝
 * 看似考虑憋腿,多了约束,实际上减少了问题的解空间
 * 世间万事也是如此:看似是一种麻烦,实际上更有利于解决问题,缩小可行解范围
 */
public class HorseControlBruteForce {
int row = 5, col = 5;
//用下面两个数组来表示整个局面
//a[i][j]表示i,j处被控制的次数
int[][] a = new int[row][col];
char[][] b = new char[row][col];//b[i][j]存储是否放了马
//可行解
List<char[][]> methods = new ArrayList<>();
//最优答案
int ans = 22;
//马腿
int leg[][] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

//保存当前解法
void saveMethod() {
    char[][] b = new char[a.length][];
    for (int i = 0; i < a.length; i++) {
        b[i] = new char[a[i].length];
        for (int j = 0; j < a[i].length; j++) {
            b[i][j] = this.b[i][j];
        }
    }
    methods.add(b);
}

//判断是否越界
boolean legal(int x, int y) {
    return x >= 0 && y >= 0 && x < row && y < col;
}

void addDelta(int x, int y, int delta) {
    if (legal(x, y)) a[x][y] += delta;
}

//更新局面
void update(int x, int y, int delta) {
    //更新x,y马的控制范围
    for (int i = 0; i < leg.length; i++) {//四个方向
        int legX = x + leg[i][0], legY = y + leg[i][1];
        if (legal(legX, legY) && b[legX][legY] != '*') {//不能绊马腿
            if (leg[i][0] == 0) {
                addDelta(x - 1, legY + leg[i][1], delta);
                addDelta(x + 1, legY + leg[i][1], delta);
            } else {//leg[i][1]==0
                addDelta(legX + leg[i][0], y - 1, delta);
                addDelta(legX + leg[i][0], y + 1, delta);
            }
        }
    }
    //更新我上方和我左方的马的控制范围,我会影响我的上方和我的左方的马
    if (legal(x - 1, y) && b[x - 1][y] == '*') {//如果上方有马
        addDelta(x + 1, y + 1, -delta);
        addDelta(x + 1, y - 1, -delta);
    }
    if (legal(x, y - 1) && b[x][y - 1] == '*') {
        addDelta(x - 1, y + 1, -delta);
        addDelta(x + 1, y + 1, -delta);
    }
}

//判断x,y处是否必须放马,需要考虑最左上那个位置是否有马,因为那个位置以后再也没人能访问到了
//如果不需要放,0;可以放马解决,1;放马也不管用2
int must(int x, int y) {
    if (legal(x - 2, y - 1) && a[x - 2][y - 1] == 0) {
        if (b[x - 1][y] == '*') return 2;
        else return 1;
    }
    //如果是最后一列,必须控制住右上角
    if (y == col - 2) {
        if (legal(x - 2, y + 1) && a[x - 2][y + 1] == 0) {
            if (b[x - 1][y] == '*') return 2;
            else return 1;
        }
    }
    return 0;
}

void pause() {
    try {
        System.in.read();
    } catch (IOException e) {
        e.printStackTrace();
    }
}

//最后两行局面是否满足全部被控条件
boolean ok() {
    for (int i = 0; i < col; i++) {
        for (int j = 0; j < 3; j++) {
            if (a[row - j - 1][i] == 0) return false;
        }
    }
    return true;
}

void go(int x, int y, int cnt) {
//    showBoard(b);
//    System.out.println("====");
//    showBoard(a);
//    pause();
    if (x == row) {
        if (ok()) {
            if (cnt < ans) {
                ans = cnt;
                methods.clear();
            }
            if (cnt == ans) {
                saveMethod();
//                showBoard(b);
//                System.out.println("====");
            }
        }
        return;
    }
    if (cnt > ans) return;
    int nextX = x, nextY = y + 1;
    if (nextY == col) {
        nextY = 0;
        nextX = x + 1;
    }
    int mustPut = must(x, y);
    if (mustPut == 2) return;//放也不管用
    if (mustPut == 0) {//不是必须放,可以不放
        b[x][y] = '.';
        go(nextX, nextY, cnt);
    }
    //放置
    update(x, y, 1);
    b[x][y] = '*';
    a[x][y]++;
    go(nextX, nextY, cnt + 1);
    //拿起来
    a[x][y]--;
    b[x][y] = '.';
    update(x, y, -1);
}

void showBoard(Integer[][] board) {
    for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[i].length; j++) {
            System.out.print(board[i][j]);
        }
        System.out.println();
    }
}

void showBoard(int[][] board) {
    for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[i].length; j++) {
            System.out.print(board[i][j]);
        }
        System.out.println();
    }
}

void showBoard(char[][] board) {
    for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[i].length; j++) {
            System.out.print(board[i][j]);
        }
        System.out.println();
    }
}

HorseControlBruteForce() {
    for (int i = 0; i < row; i++) for (int j = 0; j < col; j++) b[i][j] = '.';
    go(0, 0, 0);
    System.out.println(ans + " 解法种数" + methods.size());
    for (char[][] board : methods) {
        showBoard(board);
        System.out.println("==========");
    }
}

public static void main(String[] args) {
    new HorseControlBruteForce();
}
}