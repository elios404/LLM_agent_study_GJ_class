// 3. class 기반 객체지향 프로그래밍

class IdolModel {
    // 변수 앞에 #을 붙이면 private 로 적용된다.
    #name;
    #year;

    constructor(name, year) {
        this.#name = name;
        this.#year = year;
    }

    // 근데 여기서 set, get은 따로 정의되어 있는건가?
    set name(name){
        this.#name = name;
    }

    get name(){
        return this.#name;
    }

    get toString(){
        return this;
    }

    static returnGroupName(){
        return "아이브";
    }
}

// class 상속
class FemaleIdolModel extends IdolModel {
    part;

    constructor(name, year, part){
        super(name, year);
        this.part = part;
    }
}

const yuJin = new IdolModel("안유진", 2003);
console.log(yuJin.name)
console.log(IdolModel.returnGroupName());