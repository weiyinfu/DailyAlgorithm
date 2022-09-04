package eightqueen;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.concurrent.*;

/**
 * 此程序来自网络
 * 此程序对八皇后的优化主要集中在两个地方
 * 1:考虑对称性,第一行的对称性可以使时间减少一半
 * 2:多线程,第一行可以开辟N/2的线程整,是时间变为原来的2/N
 * 经过以上两个优化,整个程序时间变为原来的1/N
 */
//https://www.hexcode.cn/article/show/eight-queen?utm_source=wechat_session&utm_medium=social
public class Queen {
static short N = 0;

static void main(String[] args) throws Exception {
    new Queen();
}

Queen() throws ExecutionException, InterruptedException {
    for (N = 1; N <= 17; N++) {
        long count = 0;
        Date begin = new Date();
        /**
         * 初始化棋盘，使用一维数组存放棋盘信息
         * chess[n]=X:表示第n行X列有一个皇后
         */

        List<short[]> chessList = new ArrayList<>(N);
        for (short i = 0; i < N; i++) {
            short chess[] = new short[N];
            chess[0] = i;
            chessList.add(chess);
        }

        short taskSize = (short) Math.ceil(N / 2.0);
        // 创建一个线程池
        ExecutorService pool = Executors.newFixedThreadPool(taskSize);
        // 创建多个有返回值的任务
        List<Future<Long>> futureList = new ArrayList<>(taskSize);
        for (int i = 0; i < taskSize; i++) {
            Callable<Long> c = new EightQueenThread(chessList.get(i));
            // 执行任务并获取Future对象
            Future<Long> f = pool.submit(c);
            futureList.add(f);
        }
        // 关闭线程池
        pool.shutdown();

        for (short i = 0; i < (short) (taskSize - (N % 2 == 1 ? 1 : 0)); i++) {
            count += futureList.get(i).get();
        }
        count = count * 2;
        if (N % 2 == 1) {
            count += futureList.get(N / 2).get();
        }
        Date end = new Date();
        System.out.println("解决 " + N + "皇后问题，用时：" + String.valueOf(end.getTime() - begin.getTime()) + "毫秒，计算结果：" + count);
    }
}

class EightQueenThread implements Callable<Long> {
    short[] chess;

    EightQueenThread(short[] chess) {
        this.chess = chess;
    }

    @Override
    public Long call() {
        return putQueenAtRow(chess, (short) 1);
    }
}

Long putQueenAtRow(short[] chess, short row) {
    if (row == N) {
        return (long) 1;
    }
    short[] chessTemp = chess.clone();
    long sum = 0;
    /**
     * 向这一行的每一个位置尝试排放皇后
     * 然后检测状态，如果安全则继续执行递归函数摆放下一行皇后
     */
    for (short i = 0; i < N; i++) {
        //摆放这一行的皇后
        chessTemp[row] = i;

        if (isSafe(chessTemp, row, i)) {
            sum += putQueenAtRow(chessTemp, (short) (row + 1));
        }
    }
    return sum;
}

boolean isSafe(short[] chess, short row, short col) {
    //判断中上、左上、右上是否安全
    short step = 1;
    for (short i = (short) (row - 1); i >= 0; i--) {
        if (chess[i] == col)   //中上
            return false;
        if (chess[i] == col - step)  //左上
            return false;
        if (chess[i] == col + step)  //右上
            return false;
        step++;
    }
    return true;
}
}
/**
 * 解决 1皇后问题，用时：6毫秒，计算结果：1
 * 解决 2皇后问题，用时：0毫秒，计算结果：0
 * 解决 3皇后问题，用时：0毫秒，计算结果：0
 * 解决 4皇后问题，用时：0毫秒，计算结果：2
 * 解决 5皇后问题，用时：1毫秒，计算结果：10
 * 解决 6皇后问题，用时：1毫秒，计算结果：4
 * 解决 7皇后问题，用时：1毫秒，计算结果：40
 * 解决 8皇后问题，用时：1毫秒，计算结果：92
 * 解决 9皇后问题，用时：3毫秒，计算结果：352
 * 解决 10皇后问题，用时：8毫秒，计算结果：724
 * 解决 11皇后问题，用时：20毫秒，计算结果：2680
 * 解决 12皇后问题，用时：43毫秒，计算结果：14200
 * 解决 13皇后问题，用时：269毫秒，计算结果：73712
 * 解决 14皇后问题，用时：1929毫秒，计算结果：365596
 * 解决 15皇后问题，用时：10902毫秒，计算结果：2279184
 * 解决 16皇后问题，用时：66646毫秒，计算结果：14772512
 * 解决 17皇后问题，用时：550193毫秒，计算结果：95815104
 */