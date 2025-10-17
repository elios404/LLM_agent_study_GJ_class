console.log("hello")

// 변수
// var, const, let
var num = 10; //공용 변수, scope 가 전체, 되도록 사용하지 않도록
console.log(num)
console.log(typeof num)

num = "안녕";
console.log(num)
console.log(typeof num)

// var : 여러 큰 scope에서 공유하기 위한 최상위 변수 사용

// let : 작은 scope에서 사용, 로컬 변수

// const : 상수값으로 사용 값이 변할 수 없음.

// 정수, 실수 둘 다 number 형
let intNum = 10;
let floatNum = 3.14;

console.log(typeof intNum)
console.log(typeof floatNum)

let sinS = 'single';
let doubleS = "double";

const kosa = '홍길동\t박길동'
console.log(kosa)

// 여러 줄 원하는대로 표시 가능
const kosa2 = `안녕
반가워
잘가
ㅎㅎ
`;
console.log(kosa2);

// 변수 출력
const name = "광인사";
console.log(name + " 입니다.")
console.log(`${name} 입니다.`)

// 논리형(boolena) -> true/false 만 있는 것이 아니다.
/*
    다음은 모두 같은 false 이다.
    false
    string : '' -> 빈 문자열일 때
    null
    undefined
    0
*/

let boolVar = true;
console.log(typeof boolVar);
console.log(!!false);
console.log(!0); // 0이 false 이기에 !로 true 로 바뀜
console.log(!!undefined);
console.log(!!null);
console.log(!!'0'); //'0'은 true
console.log(!!{}); //true
console.log(!![]); //true

// 함수 -> 익명함수
let fun = function() {};
console.log(typeof fun); //데이터 타입 function

// js에서 {}는 객체, 리터럴 객체
let person = {
    name : '홍길동',
    age : 20
}

console.log(typeof person) //object 타입
// 클래스 안의 값을 키로 접근하는 법
console.log(person.name);
console.log(person['age']);

//배열
const kosaMember = ["홍길동", "박길동"," 김길동"];
console.log(kosaMember);