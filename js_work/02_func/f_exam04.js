// 함수 클로저
// 함수 클로저의 이유 1 : 함수가 끝나도 그 안에 있는 변수 값을 유지하기 위해서

function outerFunc(){
    const x = 10;
    const innerFunc = function(){
        console.log(x);
    }

    return innerFunc; // 이 함수가 x를 사용하고 있기에 outerFunc이 끝나도 여전히 x가 살아있다.
}

const inner = outerFunc();
inner(); // 10이 출력됨.

// 데이터 캐싱에 사용된다.
// function cashFunction(newNum) {
//     // 아주 오래 소요되는 작업이 있을 때
//     // .....
//     const number = 10 * 10; // 만약 이게 엄청 오래걸리는 거라면? -> 데이터 캐싱 필요
//     console.log(number);
//     return newNum * newNum;
// }

// // 함수를 호출할 때 마다, 오래걸리는 작업이 반복됨.
// console.log(cashFunction(10)); 
// console.log(cashFunction(20));


// 캐싱 적용
function cashFunction() {
    // 아주 오래 소요되는 작업이 있을 때
    // .....
    const number = 5 * 5;

    function innerCashFunction(newNum){
        console.log(number); // 이 데이터를 캐싱하는 것처럼 사용.
        return newNum * newNum;
    }
    
    return innerCashFunction;
}

const runner = cashFunction()

console.log(runner(10));  //number를 매 번 구할 필요가 없음.
console.log(runner(20));