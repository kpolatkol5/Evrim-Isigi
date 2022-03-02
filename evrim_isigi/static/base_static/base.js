// * navbar hambuger menu event

const burger_menu_btn = document.querySelector("#burger_menu_btn");
burger_menu_btn.addEventListener("click", function (event) {
    event.preventDefault();
    const burger_container = document.querySelector("#burger_container");
    burger_container.classList.toggle("dsp-block");
});

// ! navbar hambuger menu event *end*
//  *genel navigation scrool başladı

// window.addEventListener("scroll", function () {

//     // 1800 px

//     const scrol_heigth = window.scrollY;
//     const navbar_select = this.document.querySelector("#navbar_select")

//     if (scrol_heigth > 800) {

//         navbar_select.classList.add("navigation_sticky");
//         console.log("başarılı");
//         console.log(scrol_heigth)


//     }
//     if (scrol_heigth == 1600) {

//         navbar_select.classList.remove("navigation_sticky");
//         navbar_select.classList.add("navigation_sticky_none");
//         console.log("başarılı 22");

//     }

// })

//  !genel navigation scrool bitti
// *youtube script başladı*




$('.youtube_container').owlCarousel({
    loop: true,
    margin: 10,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        },
        1500: {
            items: 4
        }
    }
})
// !youtube script bitti!