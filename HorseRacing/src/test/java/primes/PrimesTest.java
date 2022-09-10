package primes;

import cn.weiyinfu.tqdm.Tqdm;
import indexheap.details.Pair;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/*
 * int范围内需要记录多少个质数？
 * int范围内有多少个质数？
 * int范围内因子最多的数字是哪些？它的因子个数是多少？
 * */
public class PrimesTest {
    boolean[] isPrime;
    List<Integer> primes = new ArrayList<>();
    int N;
    int[] maxPrimeFactor;

    @Before
    public void Setup() {
        this.N = (int) Math.ceil(Math.sqrt(Integer.MAX_VALUE));
        this.isPrime = new boolean[N];
        maxPrimeFactor = new int[N];
        Arrays.fill(isPrime, true);
        var primes = new ArrayList<Integer>();
        for (int i = 2; i < N; i++) {
            if (isPrime[i]) {
                primes.add(i);
                maxPrimeFactor[i] = i;
            }
            for (int j = 0; j < primes.size(); j++) {
                if (primes.get(j) * i >= N) {
                    break;
                }
                isPrime[primes.get(j) * i] = false;
                maxPrimeFactor[primes.get(j) * i] = primes.get(j);
                if (i % primes.get(j) == 0) {
                    break;
                }
            }
        }
        this.primes = primes;
        System.out.printf("N=%d,质数个数%d\n", N, this.primes.size());
    }

    //去重的质因子列表
    List<Integer> getUniquePrimeFactors(int v) {
        List<Integer> factors = new ArrayList<>();
        if (v >= N) {
            for (var i : primes) {
                boolean first = true;
                if (v < N) break;
                while (v % i == 0) {
                    if (first) {
                        factors.add(i);
                        first = false;
                    }
                    v /= i;
                }
            }
            if (v != 1) {
                factors.add(v);
                v = 1;
            }
        }

        while (v != 1) {
            var p = maxPrimeFactor[v];
            if (factors.size() <= 0 || factors.get(factors.size() - 1) != p) {
                factors.add(p);
            }
            v /= p;
        }
        return factors;
    }

    int getFactorCount(int v) {
        var a = getPrimeFactors(v);
        int s = 1;
        for (var i : a) {
            s *= i.second + 1;
        }
        return s;
    }

    List<Integer> getAllFactors(int v) {
        var a = getPrimeFactors(v);
        List<Integer> b = new ArrayList<>();
        handleFactors(a, 0, 1, b);
        return b;
    }

    private void handleFactors(List<Pair<Integer, Integer>> a, int index, int nowValue, List<Integer> factors) {
        if (index == a.size()) {
            factors.add(nowValue);
            return;
        }
        for (int i = 0; i <= a.get(index).second; i++) {
            handleFactors(a, index + 1, nowValue * (int) Math.pow(a.get(index).first, i), factors);
        }
    }

    //去重的质因子列表
    List<Pair<Integer, Integer>> getPrimeFactors(int v) {
        List<Pair<Integer, Integer>> factors = new ArrayList<>();
        Pair<Integer, Integer> pair = null;
        if (v >= N) {
            for (var i : primes) {
                boolean first = true;
                if (v < N) break;
                while (v % i == 0) {
                    if (first) {
                        pair = new Pair<>(i, 1);
                        first = false;
                    } else {
                        pair.second++;
                    }
                    v /= i;
                }
            }
            if (v != 1) {
                factors.add(new Pair<>(v, 1));
                v = 1;
            }
        }
        if (v < N) {
            while (v != 1) {
                var p = maxPrimeFactor[v];
                if (factors.size() <= 0 || factors.get(factors.size() - 1).first != p) {
                    factors.add(new Pair<>(p, 1));
                } else {
                    factors.get(factors.size() - 1).second++;
                }
                v /= p;
            }
        }
        return factors;
    }


    boolean isPrimeNumber(int v) {
        //首先判断v是否在primes列表中
        if (v < N) {
            return isPrime[v];
        }
        //如果不在，则for循环
        for (var i : primes) {
            if (v % i == 0) {
                return false;
            }
        }
        return true;
    }

    @Test
    public void testGetUniquePrimeFactors() {
        var ans = getUniquePrimeFactors(100);
        System.out.println(ans);
    }

    @Test
    public void testGetAllFactors() {
        var v = 1000;
        var a = getAllFactors(v);
        System.out.println(a);
        System.out.println(a.size());
        System.out.println(getFactorCount(v));
    }

    @Test
    public void testIntMaxFactorsCount() {
        var progress = Tqdm.tqdm(Integer.MAX_VALUE, "质数", true);
        List<Integer> candidates = new ArrayList<>();
        int maxFactorCount = 0;
        int batchSize = 10000;
        for (int i = 2; i < Integer.MAX_VALUE; i++) {
            if (i % batchSize == 0) {
                progress.update(batchSize);
            }
            var factors = getFactorCount(i);
            if (factors > maxFactorCount) {
                maxFactorCount = factors;
                candidates.clear();
                candidates.add(i);
            } else if (factors == maxFactorCount) {
                candidates.add(i);
            }
        }
        System.out.println("maxFactorCount:" + maxFactorCount);
        System.out.println(candidates);
    }

    @Test
    public void testFactor() {
        var a = getPrimeFactors(1000);
        for (var i : a) {
            System.out.println(i.first + "=>" + i.second);
        }
    }

    @Test
    public void testIntMaxUniquePrimesCount() {
        long s = 1;
        int i = 0;
        while (s * (long) (primes.get(i)) < Integer.MAX_VALUE) {
            s *= (long) primes.get(i);
            i++;
        }
        System.out.printf("质数个数：%d,%s\n", i, primes.subList(0, i));
    }

    @Test
    public void testPrimesCountOfInt() {
        int primesCount = 0;
        var progress = Tqdm.tqdm(Integer.MAX_VALUE, "质数", true);
        for (int i = 0; i < Integer.MAX_VALUE; i++) {
            if (i % 10000 == 0) {
                progress.update(10000);
            }
            if (isPrimeNumber(i)) {
                primesCount++;
            }
        }
        System.out.printf("质数个数：%d\n", primesCount);
    }
}
