// 자바스크립트 객체

// 1. 리터럴 형식 객체 기반 -> 하지만 리터럴 객체는 여러 개 객체를 만들 때는 매우 비효율적
const obj = {
    name : '홍길동',
    age : 30,
    display: function() {
        console.log(this.name); // 자기 자신에 접근할 때 this.
    }
};

obj.display();
console.log(`나이 : ${obj.age}`);
console.log(`나이 : ${obj['age']}`);

// 2. 자바 객체는 없는 속성도 추가할 수 있음
// 즉 객체가 만들어 질 때 없었던 속성도 추가할 수 있음.
obj.address = '광주시 서석동';
console.log(obj.address);