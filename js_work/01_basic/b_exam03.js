// 형 변환

let age = 20;

// 명시적 형변환
let stringAge = age.toString();
console.log(typeof stringAge);

//암묵적 형변환
let test = age + "";
console.log(typeof test);

//문자열 -> 정수형 : eval(), Number(), parseInt()
let num = '100';
let result = num + 100;
console.log(result); // '100100'으로 나옴

let num2 = '100안녕' 
parnum = parseInt(num2); //문자열에서 숫자만 뽑아서 int로 바꿈.
let result2 = parnum + 100;
console.log(result2);

//호이스팅(Hoisting) : 모든 변수 선언문이 코드의 최상단으로 이동되는 것 처럼 느껴지는 것
console.log(Kim);

var Kim = '김씨';