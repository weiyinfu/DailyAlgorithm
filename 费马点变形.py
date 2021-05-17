import numpy as np

"""
一维空间中有若干个苹果，每个苹果的位置为a[i]，每个位置至多有一个苹果。
把每个苹果移动一格花费力气为1，现在有n个力气用于移动苹果，
移动苹果之后，最长的连续苹果就归你所有了，你想得到尽量多的苹果，
请问n个力气可以让你得到多少个苹果？

费马点是把所有点移动到同一个点，此题是把若干个点移动到某个点。
"""
def generate(n):
    a = np.random.randint(1, 100, n)
    a = np.cumsum(a)
    return a, np.random.randint(0, a[-1])


def op(a, n):
    # 对数组a操作n次使得相邻元素尽量长
    ans = 0
    ma = 2 ** 30
    for i in range(len(a)):
        ll = i - 1
        rr = i + 1
        l = a[i] - 1
        r = a[i] + 1
        x = n
        while 1:
            left_cost = l - a[ll] if ll >= 0 else ma
            right_cost = a[rr] - r if rr < len(a) else ma
            if x < min(left_cost, right_cost):
                # 预算不足
                break
            if left_cost < right_cost:
                x -= left_cost
                l -= 1
                ll -= 1
            else:
                x -= right_cost
                r += 1
                rr += 1
        now = r - l - 1
        # print('if center ',a[i],'left,right=',(l,r),'cost=',x)
        ans = max(ans, now)
    # print(a,ans)
    return ans


def fast(a, n):
    """
    O(n)复杂度求解此问题
    从左到右扫描数组，窗口大小单调递增
    一旦确定了区间的左端点beg=i，区间右端点就是end=i+window，这是一个闭区间
    这个区间中的最优解必定是把全部元素都移动到mid=(beg+end)//2处，mid为不动点
    求出mid前面的元素的位置之和，也就是[i,mid)的和，记为pre_sum，则pre_count*mid-pre_sum就是把全部点移动到mid处，实际上无需把点移动到mid处就可以暂停，所以再加上pre_count*(pre_count+1)/2
    对于mid后面的元素做同样的处理
    如果此时得到的花费小于等于n，则放大窗口
    :param a:
    :param n:
    :return:
    """
    window = 0
    prefix = np.cumsum(a)

    def sum_of(beg, end):
        if beg > end:
            return 0
        return prefix[end] - (prefix[beg - 1] if beg > 0 else 0)

    ans = 0
    for i in range(len(a)):
        if i + window >= len(a):
            break
        while i + window < len(a):
            j = (i + window + i) // 2
            pre_sum = sum_of(i, j - 1)
            back_sum = sum_of(j + 1, i + window)
            pre_count = j - i
            back_count = i + window - j
            pre_cost = a[j] * pre_count - pre_sum - (pre_count + 1) * pre_count / 2
            back_cost = back_sum - a[j] * back_count - (back_count + 1) * back_count / 2
            cost = pre_cost + back_cost
            # print(f"i={i},j={j},window={window},presum={pre_sum},backsum={back_sum} pre_count={pre_count} back_count={back_count} pre_cost={pre_cost},back_cost={back_cost}")
            if cost <= n:
                ans = max(1 + window, ans)
                window += 1
            else:
                break
    return ans


np.random.seed(0)
a, n = generate(103)
# print(a, n)
real = op(a, n)
mine = fast(a, n)
print(real)
print(mine)
