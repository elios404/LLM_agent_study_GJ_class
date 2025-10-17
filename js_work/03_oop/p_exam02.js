// 객체를 만드는 방식 2 : 생성자 함수 기반

// 작성하는 형식은 함수와 거의 다를 바 없음
// 용도의 차이
// 여러개의 객체를 생성하는 목적으로 매우 좋음!
function Student(name, kor, eng, mat){
  this.name = name;
  this.kor = kor;
  this.eng = eng;
  this.mat = mat;

//   this.getSum = function(){
//     return this.kor + this.eng + this.mat;
//   }
//   this.getAverage = function(){
//     return this.getSum()/3;
//   }
//   this.toString = function(){
//     return this.name + "\t" + this.getSum() + "\t" + this.getAverage();
//   }
}

// 프로토 타입 : 각 객체에 공통/반복되는 함수를 따로 하나의 prototype 으로 분리해서 1개만 메모리에 올릴 수 있도록
// 각 객체에 공통된 함수가 반복되지 않기에, 메모리에 prototype으로 함수 하나만 저장하면 되기에 메모리 절약 가능
Student.prototype = {
    getSum : function() {
        return this.kor + this.eng + this.mat;
    },
    getAverage : function() {
        return this.getSum()/3;
    },
    toString : function() {
        return this.name + "\t" + this.getSum() + "\t" + this.getAverage();
    }
}

const students = [];
students.push(new Student('sejun',80, 90, 100));
students.push(new Student('gejun',70, 80, 90));
students.push(new Student('kojun',60, 70, 80));

// for - in 은 키 값을 인덱스?로
for (let i in students) { 
    console.log(students[i].toString());
}

for (let student of students){
    console.log(student.toString());
}

