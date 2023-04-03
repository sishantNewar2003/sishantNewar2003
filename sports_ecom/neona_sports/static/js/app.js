const menu = document.getElementById('bar');
const nav = document.getElementById('navbar');
const close = document.getElementById('close');

menu.addEventListener('click', () => {
    nav.classList.toggle('active');
})

close.addEventListener('click', () => {
    nav.classList.toggle('active');
})

// window.onclick = function(e) {
//     nav.style.display = 'flex';
//     if (e.target !== nav && e.target !== menu && e.target !== close) {
//         nav.style.display = "hidden";
//     } else {
//         nav.style.display = "flex";
//     }
// }

const productContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})