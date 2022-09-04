package horsecontrol;

/**
 * 马控棋盘问题：中国象棋棋盘10*9，需要多少匹马才能控制棋盘每一个点（需要考虑蹩马腿）
 * 每行有两种表示方式：2**col种放法（0表示空着，1表示放马）；3**col种状态，0表示空着，1表示有马，2表示被控
 * 插头DP，滚动数组
 **/
class HorseControl {

final int SPACE = 0;
final int HORSE = 1;
final int CONTROL = 2;

int row = 5, col = 5;
int ROWSTATE = (int) Math.pow(3, col);//一行的状态数：从0000到2222


//滚动数组动态规划
int[][] a = new int[ROWSTATE][ROWSTATE];//最近两行的局面
int[][] b = new int[ROWSTATE][ROWSTATE];//最近两行的局面
int leg[][] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int[] pow = new int[col];//预先存下3的幂次
int[] horseToState = new int[1 << col];//把马的2**col种放法转换成一行的状态
int[][] chessAt = new int[ROWSTATE][col];//根据ROWSTATE求col处的棋子
int[] horseCount = new int[1 << col];//把马2**col种放法转换成马的个数
boolean[] ok = new boolean[ROWSTATE];//状态i是否全部非0
int[] threeLine = new int[3];//三行

//预置表法加速，以空间换时间
void init() {
    //预先算出3的幂次
    pow[0] = 1;
    for (int i = 1; i < pow.length; i++) {
        pow[i] = pow[i - 1] * 3;
    }
    //预先算出马到状态的转换
    for (int i = 0; i < (1 << col); i++) {
        int k = 0;
        for (int t = 0; t < col; t++) {
            if ((i & (1 << t)) > 0) {
                k = put(k, t, HORSE);
            }
        }
        horseToState[i] = k;
    }
    //初始化chessAt数组，获取状态i在j处的棋子
    for (int i = 0; i < ROWSTATE; i++) {
        for (int j = 0; j < col; j++) {
            chessAt[i][j] = i / pow[j] % 3;
        }
    }
    //初始化horseCount
    for (int i = 0; i < (1 << col); i++) {
        int s = 0;
        for (int j = 0; j < col; j++) if ((i & (1 << j)) > 0) s++;
        horseCount[i] = s;
    }
    //初始化ok数组，判断是否全1
    for (int i = 0; i < ROWSTATE; i++) {
        int x = i;
        boolean o = true;
        for (int j = 0; j < col; j++) {
            if (x % 3 == SPACE) {
                o = false;
                break;
            }
            x /= 3;
        }
        ok[i] = o;
    }
}

//只考虑3行的情况
boolean legal(int x, int y) {
    return x >= 0 && y >= 0 && x < 3 && y < col;
}


int put(int rowState, int x, int value) {
    if (value == 0) return rowState;
    else if (value == 1) return rowState + pow[x];
    else return rowState + (pow[x] << 1);
}

void control(int x, int y) {
    if (legal(x, y) && chessAt[threeLine[x]][y] == 0) {
        threeLine[x] = put(threeLine[x], y, CONTROL);
    }
}

void calculateState(int i, int j, int k) {
    threeLine[0] = i;
    threeLine[1] = j;
    threeLine[2] = k;
    for (int p = 0; p < 3; p++) {//三行
        for (int q = 0; q < col; q++) {//q列
            if (chessAt[threeLine[p]][q] == HORSE) {//如果p,q处是马
                for (int t = 0; t < leg.length; t++) {//四个方向
                    int legX = p + leg[t][0], legY = q + leg[t][1];
                    if (legal(legX, legY) && chessAt[threeLine[legX]][legY] != 1) {//不能绊马腿
                        if (leg[t][0] == 0) {
                            control(p - 1, legY + leg[t][1]);
                            control(p + 1, legY + leg[t][1]);
                        } else {//leg[i][1]==0
                            control(legX + leg[t][0], q - 1);
                            control(legX + leg[t][0], q + 1);
                        }
                    }
                }
            }
        }
    }
}

void setMax(int[][] a) {
    for (int i = 0; i < a.length; i++) {
        for (int j = 0; j < a[i].length; j++) {
            a[i][j] = Integer.MAX_VALUE;
        }
    }
}

int getCount() {
    setMax(a);
    for (int i = 0; i < (1 << col); i++) {
        for (int j = 0; j < (1 << col); j++) {
            calculateState(horseToState[i], horseToState[j], 0);
            a[threeLine[0]][threeLine[1]] = horseCount[i] + horseCount[j];
        }
    }
    int ans = Integer.MAX_VALUE;
    /***如果能够开辟下ROWSTATE*ROWSTATE*2**COL大小的空间就可以把下面过程用数据存储下来
     * 程序跟数据是可以互相转化的，以空间换时间
     * 状态ROWSTATE*ROWSTATE，算子2**COL，算子作用于状态从而改变状态
     */
    for (int r = 2; r < row; r++) {
        System.out.println("row " + r);
        setMax(b);
        for (int i = 0; i < ROWSTATE; i++) {
            for (int j = 0; j < ROWSTATE; j++) {
                //如果已经无解，继续
                if (a[i][j] == Integer.MAX_VALUE) continue;
                for (int op = 0; op < (1 << col); op++) {//当前行操作
                    calculateState(i, j, horseToState[op]);
                    if (r == row - 1) {//如果是最后一行，三行必须全部控住
                        if (ok[threeLine[0]] && ok[threeLine[1]] && ok[threeLine[2]]) {
                            int cnt = a[i][j] + horseCount[op];
                            if (cnt < ans) {
                                ans = cnt;
                            }
                        }
                    } else {
                        if (ok[threeLine[0]]) {//第一行必须控住，后两行还有希望
                            int cnt = a[i][j] + horseCount[op];
                            if (cnt < b[threeLine[1]][threeLine[2]]) {
                                b[threeLine[1]][threeLine[2]] = cnt;
                            }
                        }
                    }
                }
            }
        }
        int[][] c = a;
        a = b;
        b = c;
    }
    return ans;
}

HorseControl() {
    if (row < col || col <= 2) throw new RuntimeException("row > col >2 is needed");
    init();
    int ans = getCount();
    System.out.println(ans);
}

public static void main(String[] args) {
    new HorseControl();
}
}