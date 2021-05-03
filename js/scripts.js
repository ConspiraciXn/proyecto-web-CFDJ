/* Alertas de acciones ejecutadas correctamente. */
function iniciarSesion() {
    /* A futuro añadir método de inicio de sesión. */
    toastr.success('', '¡Has iniciado sesión correctamente!');
    toastr.options = {
        "closeButton": false,
        "debug": false,
        "newestOnTop": false,
        "progressBar": true,
        "positionClass": "toast-top-right",
        "preventDuplicates": false,
        "onclick": null,
        "showDuration": "300",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
}

function crearVentana(url, titulo){
    window.open(url, titulo, "width=700, height=800")
}

$(document).ready(function() {
    $.get("https://mindicador.cl/api/dolar",function(data){
    var dolar = data.serie[0].valor;
    $("#valor_dolar").html('$' + dolar);

    })
});

$(document).ready(function() {
    $.get("https://mindicador.cl/api/uf",function(data){
    var uf = data.serie[0].valor;
    $("#valor_uf").html('$' + uf);

    })
});

$(document).ready(function() {
    $.get("https://mindicador.cl/api/euro",function(data){
    var euro = data.serie[0].valor;
    $("#valor_euro").html('$' + euro);

    })
});

$(document).ready(function() {
    $.get("https://mindicador.cl/api/utm",function(data){
    var utm = data.serie[0].valor;
    $("#valor_utm").html('$' + utm);

    })
});