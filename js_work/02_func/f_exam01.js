// console.log(add(10,20)); // 선언적 함수는 먼저 사용하고 아래에서 정의 가능
// console.log(add2(10, 20)); // 익명함수는 호이스팅이 안됨.

//선언적 함수 -> 먼저 메모리에 올라가 선언보다 위에서도 사용 가능
function add(a,b) {
    let sum = a+b;
    return sum;
}

console.log(add(10,20));

// 익명 함수 : 변수에 함수를 할당할 수 있다.
let add2 = function(a, b) {
    let sum = a+b;
    return sum;
}

console.log(add2(10, 20));


// add2 VS add2()
let plus = add2; // 함수 자체를 대입받음
let plus2 = add2(); // 함수의 return 값을 대입받음.

//함수의 파라미터에 함수를 전달할 수 있다.

let foo = function(func){
    if(typeof func === 'function'){ //파라미터가 함수로 전달될 때만
        func();
    }

}

foo(function(){
    console.log("파라미터에 함수를 전달하는 예제")
})

//함수가 함수를 리턴할 수 있다.

let foo2 = function(){
    return function(){
        console.log("함수를 리턴하는 예제");
    }
}

let box = foo2();
box();


// 콜백함수(함수의 파라미터에 전달되는 함수)

function sortDesending(a,b) { // 내림차순으로 할 때
    if(a > b){ //앞이 크면
        return -1; // 자리 바꾸지 않기
    } else if (a < b) { //뒤가 크면
        return 1; // 자리 바꾸기
    } else {
        return 0;
    }
}

function sortDesending2(a,b) { // 내림차순으로 할 때
    return b - a;
}

let arr = [32,33,34,42,51,21,13];
console.log(arr.sort(sortDesending));

// 즉시 실행 함수 : 함수를 정의하고, 그 동시에 호출까지 진행하기 -> ()안에 함수를 정의
(function(a,b) {
    console.log(a+b);
})(10,9)