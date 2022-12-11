#include<stdio.h>
#include<math.h>
int main(){
	double r = 1;//操场半径
	double ax = 0, ay = 0, bx = r, by = 0;//a为小明初始位置，b为小红初始位置
	double v1 = 0.1;//小明的速度
	double v2 = 0.08;//小红的速度
	double dt = 0.0001;//时间间隔
	double t = 0;//当前时间
	double eps = 1e-3;//0阈值
	double w = v2 / r;//小红的角速度
	while (1){
		bx = r, by = v2*t;//小红的位置
		double vx = bx - ax, vy = by - ay+v2*dt;//小明的方向
		double len = hypot(vx, vy);
		vx = vx / len, vy = vy / len;
		ax += v1*dt*vx, ay += v1*dt*vy;//更新小明的位置
		if (hypot(ax - bx, ay - by) < eps)break;
		t += dt;
	}
	printf("%lf\n", t);
	printf("%lf\n", r / sqrt(v1*v1 - v2*v2));
	printf("%lf\n", r / v2*asin(v2 / v1));
	return 0;
}