# 三角形内心公式
首先证明这个结论：O是ABC内心的充要条件是：aOA+bOB+cOC=0 （均表示向量）
证明:OB=OA+AB,OC=OA+AC,代入aOA+bOB+cOC=0中得到：
AO=(bAB+cAC)/(a+b+c)
而|AC|=b,|AB|=c
所以AO=bc/(a+b+c) * (AB/|AB|+AC/|AC|)
而由平行四边形法则值(AB/|AB|+AC/|AC|)与BAC交角平分线共线
所以AO经过内心
同理BO,CO也经过内心,所以O为内心
反之亦然,就不证了
知道这个结论后
设ABC的坐标为：A(x1,y1),B(x2,y2),C(x3,y3) BC=a,CA=b,AB=c
内心为O(x,y)则有aOA+bOB+cOC=0（三个向量）
MA=(x1-x,y1-y)
MB=(x2-x,y2-y)
MC=(x3-x,y3-y)
则：a(x1-x)+b(x2-x)+c(x3-x)=0,a(y1-y)+b(y2-y)+c(y3-y)=0
∴x=(ax1+bx2+cx3)/(a+b+c),Y=(ay1+by2+cy3)/(a+b+c)
∴O((ax1+bx2+cx3)/(a+b+c),(ay1+by2+cy3)/(a+b+c))

# 三角形的4个心
内心是角平分线的交点，外心是垂直平分线交点，重心是中线交点，垂心是高的交点。
口诀：内角分，外中垂，重中线，垂直高。