// 함수 실행 컨텍스트
// Lexical Scope : 함수가 선언된 위치가 상위 스코프를 결정한다. (JavaScript)
// Dynamic Scopoe : 함수가 실행한(호출) 위치가 상위 스코프를 결정한다.

// 예제 1번

// let var1 = 10;

// function func() {
//     let var2 = 20;
//     console.log(var1);
// }

// func(); // 상위 스코프인 var1의 10이 출력됨

// 예제 2번

// let value = "value1";

// function printFunction(){
//   let value = "value2";

//   function printValue(){
//     return value;
//   }

//   console.log(printValue());
// }

// printFunction(); // value2 출력

//예제 3번

// let value = "value1";

// // 함수가 선언된 위치가 중요함! 상위 스코프인 value1을 출력!
// function printValue(){
//   return value;
// }

// function printFunction(func){
//   let value = "value2";

//   console.log(func());
// }

// printFunction(printValue); // value1 출력



// var : 공용 함수 => 함수 레벨 스코프만 적용 -> 함수 안에서만 변수를 분리해서 해석한다.
// let, const : 함수레벨, 블록레벨 스코프 모두 적용 -> 블록 레벨에서도 변수를 분리해서 해석한다.

// var var3 = 100;

// function func3() {
//     var var3 = 200; // 함수 레벨에서는 var도 분리 된다.
//     console.log(var3);
// }

// func3(); // 200 출력
// console.log(var3); // 100 출력

let i = 999;

for (let i=0; i<10; i++) { // i는 블록 안에 있어도, 블록 밖에 있는 것도 바꾼다.
    console.log(i);
}

console.log(i);