// 一.基础语法
// 1.注释：//
// 2:必须以分号结束；
// 3：变量声明：var 变量名 = 'string',3
// (与python一样是动态类型，可以更改变变量名的数据类型)
//var a='stringa';
// var num=18;
// print(a)
//
// console.log('a:',a);
// console.log('num:',num);

//
// 二.数据类型
// 1.布尔类型 :var flag=true/false;(注意是小写的)
// 2.数组：类似python中的数组 :var list=[123,'abc']
// 3.常用方法
//     .length :获取长度
//     .push() ：尾部追加
//     .pop()  :移除尾部元素
//     l.join('s') :将数组l通过's'拼接成新的字符串（与python相反）
//
// //.引入javascript:在html head里加上 <script src="js_basic.js"></script>
//
// 4.null和undefined
//  null:表示变量的值是空
// undefined ：表示只声明了变量，但还没有赋值
//
//
// 三.逻辑运算符
//  &&  ||  !
//
// 四.流程控制
// 1.if-else
//     var n=10;
//     if (n>13){
//         console.log('n>13');
//     }
//     else if (n<7){
//         console.log('n<7');
//     }
//     else{
//         console.log('7<n<13');
//     }
//
//
// 2.switch
// d=3
// switch(d){
//         case 1:console.log('d=1');
//         case 2:console.log('d=2');
//         case 3:console.log('d=3');
//
//
// }
//
//
// 3.for
// for(var i=0,sum=0;i<11;i++){
//     sum+=i;
//     console.log(sum);
// }
//
//
// 4.while
//
// var i=0;
// var sum=0;
//
// while(i<11){
//
//     sum+=i;
//     i++;
//     console.log(sum);
//
// }
//
//
// 五.函数
//
// 定义与调用
// function f1(a,b){
//     console.log(a);
//     console.log(b);
//     return a+b
// }
//
// var sum=f1(11,22);
// console.log(sum);
//
//
//
// 六：对象
//
// 1.自定义对象：
//     1:key不需要加引号
//     2：value如果是字符串类型，必须加双引号
// var person ={name:"suisui",age:7}
//
// 2.date对象
// var d1=new Date();  d1是object类型
// d1.toLocaleDateString(); d1为string类型
// d1.getDate();  获取那一天（多少号）
//
//
//
// 3.json对象
// -将json字符串转换成
// var s='{"name":"suisui","age":7}'; 字符串必须加双引号
// var ret=JSON.parse(s);
// -将js内部对象转换成json字符串
// var s={name:"suisui",age:7};
// var ret=JSON.stringify(s);
//
//
// 七.BOM:浏览器对象模型，是js有能力与浏览器进行对象
// 1.常用的window操作：
//     window.open()/close()
//     location.href ：获取当前的url
//     location.href="url" :前往url
//     location.reload()
//
// 2.警告框：
//     alert("这是一个alert");
// 3.确认框：
//     confirm("你确定吗")；
//     点击确认，返回值为true，点击取消，返回值为false
//
// 4.提示框
//     prompt("请输入你的邮箱","默认内容");
//     返回值为输入的信息
//
//
// 5。计时相关
//     var t = setTimeout("js语句"，毫秒);
//     clearTimeout(t);
//     var timer=setInterval("js语句",3000)
//     clearInterval(timer)
//
//
//
//
//
// 八.DOM：文档对象模型，访问html文档的所有属性
//  -js能够改变页面中所有html元素，属性，css样式，对页面中所有事件做出反应
//
// 1.查找标签
//
// -直接查找
//
//     document.getElementById("heading1");
//     document.getElementsByClassName("index-logo-srcnew");
//
// -间接查找
//  -通过子标签找父标签：sonele.parentElement
//  -通过父标签找所有子标签：faele.children
//
// 2.添加标签
// -创建标签 ：var aele = createElement("a");
// -在某个父标签下添加：
//     faele=document.getElementBy....;
//     faele.appendChild(aele);
//
// 3.更改、添加属性：
// 标签变量.属性名="xxx";
//
// 4.设置文本内容
// 标签变量.innerText="xxx";
// 标签变量.innerHTML="<p>dddd</p>";
//
//
// 5.事件：用户点击某个html元素时启动javascript


// 九.jquery

// (1)点击行为：隐藏，显示
$(document).ready(function(){
  $("#b1").click(function(){
    $("h1").hide();
  });
});

$(document).ready(function(){
  $("#b2").click(function(){
    $("h1").show();
  });
});
