要想随意判断一个int数字是不是质数，就需要打印`sqrt(Int.MAX_VALUE)`范围内的所有质数。  
0到46341范围内的质数个数是4792。  

int范围内质数的个数是：105097565

int范围内因子最多的数字是：
它们的因子个数是：



# 一道题
一个1e5的数组，数的大小的范围是int，要你找出一个三元组（x,y,z），满足x是y的因数，y是z的因数，然后这三个数在数组里的位置是递增的，求满足这样条件的三元组的最大的y是多少？

对数组逐个扫描，对于每个数字，找出它的全部因子。这基于一个常识：一个int数字，它的因子个数最多不超过1536个。  
对于每个因子，判断它是否在这个数组里面；如果在数组里面，这个因子的位置是否在当前数字的前面，如果在，则说明找到一对数字。  

关键在于找y，y就是前面有因子，并且是后面数字的因子。  

