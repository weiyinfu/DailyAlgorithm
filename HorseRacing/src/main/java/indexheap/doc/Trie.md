
日本鬼子的C++ Darts：
https://github.com/s-yata/darts-clone  
有人将之翻译成Java：https://github.com/hiroshi-manabe/darts-clone-java

cedar：
官方介绍：http://www.tkl.iis.u-tokyo.ac.jp/~ynaga/cedar/  
中文翻译：https://segmentfault.com/a/1190000004374433

DoubleArray入门资料：
https://segmentfault.com/a/1190000008877595


darts-clone-java: A Java port of darts-clone.
=========================================================

SYNOPSIS
--------

A Java port of [darts-clone](https://code.google.com/p/darts-clone/) by Susumu Yata.

USAGE
-----
Pass an array of keys and int values to build a double array.
There are some points you should be aware of:

1. Keys should be given in byte[], not String.
1. Keys must not contain zeros.
1. Keys must be sorted lexically based on their unsigned values. For example, the key 0x80 should be sorted after the key 0x7f. See jp.dartsclone.DoubleArrayTest.java.
1. If you don't need to associate values to keys, pass an array of 0 with the same length as that of keys. This way, you can save some memory. If you pass NULL, consecutive integers starting from 0 will be associated to the keys.
1. Values should not contain negative numbers.

Caveats:

1. "Keys must not contain zeros" means you cannot put UTF-16 string (Java String) represented in byte array.
1. Maybe you want to use UTF-8 string represented in byte arrays. That is basically a good idea. But if you do so, be sure to sort the keys AFTER converting to UTF-8, not before. The sort order may change before converting from String and after converting to UTF-8 byte arrays.

# TODO:
更多优化技巧：
* 路径压缩，把多个字母压缩成一个
* 内存碎片管理，比如一个结点只有a和z两个儿子，那么b~y之间的空间可以被视为自由空间，这个问题描述如下：每个物体都是由若干个01组成的，这些物体的最密堆积方式下，物体的长度是多少？
