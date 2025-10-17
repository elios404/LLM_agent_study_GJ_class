function showPic(obj){
    const source = obj.getAttribute('href');
    const placeholder = document.getElementById('placeholder');

    const title = obj.getAttribute('title');
    const description = document.getElementById('description');

    placeholder.setAttribute('src',source);
    description.innerHTML = title;
}

function prepareGallery() {
    const imagegallery = document.getElementById('imagegallery') // ul을 가져옴
    const links = imagegallery.getElementsByTagName('a') // ul안의 a태그들의 배열을 리턴한다.

    for (let i=0; i<links.length; i++) {
        links[i].addEventListener('click', function(e){
            e.preventDefault();
            showPic(this); // 이벤트 핸들러안의 this는 이벤트를 부른 객체이다. 즉 links[i]
        }, false);
    }
}

window.onload = prepareGallery;