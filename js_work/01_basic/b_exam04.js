console.log(5 == 5);
console.log(5 == '5'); // 알아서 형 변환도 해줌.
console.log(5 == '6'); // false
console.log(5 === '5');

// for ~ in (key 사용), for ~ of(이터러블 일때)
const gilDong = {
    name : '홍길동',
    year : 2000,
    company : 'kosa'
}

// for ~ in 은 key 값을 가져온다.
for(let key in gilDong) {
    console.log(gilDong[key]);
}

console.log("----------------------")

// for ~ of : iterable 객체일때

const member = ["가", "나", "다"]
for(let value of member) {
    console.log(value);
}

// boolean을 활용한 출력 조건?
console.log('' || 'Dog');

let event2 = '';

if (event2) {
    console.log(event2)
} else {
    console.log("영화보기")
}
// 이것을

console.log(event2 || '영화보기')