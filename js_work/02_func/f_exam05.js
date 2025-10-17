// 함수가 많아서 관리가 힘들 땐? -> 함수를 묶어줌. replyService.create 와 같이 쓰기 위해서

// 즉시 실행 함수
const replyService = (function(){
    function create() {
        console.log("create");
    }

    function update() {
        console.log("update");
    }

    function getList(param, callback) { // callback 함수에 데이터를 넣어서 돌려줌. -> 근데 그냥 함수를 넣어서 안에서 실행시키는 것과 같은 것 아님?
        // console.log("getList");
        const data = '결과값: ' + param; // 데이터를 만들어서
        callback(data); // 돌려주기만 함.
    }

    function deleteList() {
        console.log("deleteList");
    }

    // 함수를 properties로 담고있는 객체
    return {
        create: create,
        update: update,
        getList: getList,
        deleteList: deleteList
    }
})();

// replyService.create();

function show() {
    replyService.getList('sejun', function(result){
        console.log('내가 원하는 형태의 출력 : ' + result);
    })
}

show();
