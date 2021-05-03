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
