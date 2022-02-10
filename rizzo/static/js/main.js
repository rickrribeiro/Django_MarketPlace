$(".search-bar-top").keyup(async () => {
    query = $(".search-bar-top").val()
    $.get('/filterFamous', { 'name': query }, async (data) => {
        text = ""
        data.forEach(element => {
            text += `<li>
            <a href="/idolo/${element.username}" class="flex items-center space-x-2 p-2 hover:bg-gray-100 rounded-md"> 
                <img src="${element.image}" alt="" class="border mr-3 rounded-full shadow-sm w-8">
            ${element.name + " " + element.last_name}
            </a>
        </li>`
        });
        $(".searchRecommendations").html(text)
    })

})


$(".product-btn").click((element) => {
    service_id = element.target.getAttribute("data-service-id");
    service_name = element.target.getAttribute("data-service-name");
    service_price = element.target.getAttribute("data-service-price");
    service_description = element.target.getAttribute("data-service-description");
    new Swal({
        title: service_name,
        text: service_description + " Por apenas R$" + service_price,
        showCancelButton: true,
        confirmButtonText: 'Comprar!',
        cancelButtonText: "Cancelar :(",

    }).then(
        function ({ isConfirmed }) {
            if (isConfirmed) {
                window.location.href = '/compra/' + service_id
            }
        })

})


$(document).ready(function () {
    //Menu Toggle Script
    $("#menu-toggle").click(function (e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    // For highlighting activated tabs
    $("#tab1").click(function () {
        console.log("clickkk")
        $(".tabs").removeClass("active1");
        $(".tabs").addClass("bg-light");
        $("#tab1").addClass("active1");
        $("#tab1").removeClass("bg-light");
    });
    $("#tab2").click(function () {
        $(".tabs").removeClass("active1");
        $(".tabs").addClass("bg-light");
        $("#tab2").addClass("active1");
        $("#tab2").removeClass("bg-light");
    });
    $("#tab3").click(function () {
        $(".tabs").removeClass("active1");
        $(".tabs").addClass("bg-light");
        $("#tab3").addClass("active1");
        $("#tab3").removeClass("bg-light");
    });
})