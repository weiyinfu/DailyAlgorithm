function add(one, two) {
  return one + two + (this.addition || 0);
}

const obj = {addition: 3};
console.log(add.call(obj, 1, 2))
console.log(add.apply(obj, [1, 2]))//apply与call完全相同，只是它接受数组参数
const ad = add.bind(obj)//bind可以延迟执行，相当于函数装饰器。
console.log(ad(1, 2));

function f() {

}

f.addition = 3;
f.add = function () {
  console.log(this.addition);
}
console.log(add.call(f, 1, 2))
console.log(add.apply(f, [1, 2]))
