const greeting = function(name) {
    return "hello " + name;
}

console.log(greeting("홍길동"));

// 화살표 함수 => , 표기법만 다름

const greeting2 = name => {
    return `hi ${name}`;
}

console.log(greeting2("천세준"));

// 함수가 한 줄 일 때
const greeting3 = name => `hi ${name}`;

console.log(greeting3("천세준"));

// 연습문제1
const add = (a,b) => a + b;

console.log(add(1,2))

// 연습문제 2
const numbers = [1,2,3,4,5];

// map을 통해서 배열의 각 요소에 함수를 적용
const result = numbers.map(a => a*a)
console.log(result)