// * navbar hambuger menu event

const burger_menu_btn = document.querySelector("#burger_menu_btn");
burger_menu_btn.addEventListener("click", function (event) {
    event.preventDefault();
    const burger_container = document.querySelector("#burger_container");
    burger_container.classList.toggle("dsp-block");
});


//  !genel navigation scrool bitti
