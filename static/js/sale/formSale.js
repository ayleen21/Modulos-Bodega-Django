/* 
$('input[name="search"]').autocomplete({
    source: function (request, response) {
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_client',
                'term': request.term
            },
            dataType: 'json',
        }).done(function (data) {
            response(data);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            //alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {

        });
    },
    delay: 500,
    minLength: 1,
    select: function (event, ui) {
        event.preventDefault();
        console.clear() //Limpiar el  elemento seleccionado desde la consola
        console.log(ui.item);
        $(this).val('');
    }
}); */
//search

var vents = {
    items: {
        /*  date_joined: '',
         service:'',
         subservice:'',
         component:'', */
        client: '',
        headquarters: ''
    }
};
//Select2

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es',
        placeholder: '',

    });

 

    $('.plan').select2({
        minimumResultsForSearch: -1,
        theme: "bootstrap4",
        language: 'es',
        placeholder: '',

    });

   
    $('.speed').select2({
        minimumResultsForSearch: -1,
        theme: "bootstrap4",
        language: 'es',
    
    });

     $('.service2').select2(
            {
                theme: "classic",
                language: 'es',
                placeholder: '',
            });

    

    //Selector para busqueda de clientes

    $('select[name="client"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_clients'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el Nit o el nombre del cliente',
        minimumInputLength: 1,

    });
    //Modal para crear el cliente
    $('.btnClient').on('click', function () {
        $('#myModalCreateClient').modal('show'); //Mostrar el modal para registrar clientes
    });

    $('#myModalCreateClient').on('hidden.bs.modal', function (e) {
        $('#frmClient').trigger('reset'); //sirve para que cuando el formulario se cierre borre la informacion
    })

    //Funcion al intentar guardar informacion del cliente

    $('#frmClient').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_client');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear al siguiente cliente?', parameters,
            function (response) {
                //console.log(response);
                //Al crear el usuario se seleccionara automaticamente
                var newOption = new Option(response.full_name, response.id, false, true);
                $('select[name="client"]').append(newOption).trigger('change');
                $('#myModalCreateClient').modal('hide'); //Ocultar modal al registrar usuario

            });

    });

    //Modal listado de clientes
    $('.btnListClient').on('click', function () { //Se le pone un nombre css al boton o se puede poner un id, se le asigna la funcion de al darle click nos muestre el modal
       tblHeadquarters =  $('#tblClients').DataTable({
                    responsive: true,
                    autoWidth: false,
                    destroy: true,
                    deferRender: true,
                    ajax: {
                        url: window.location.pathname,
                        type: 'POST',
                        data: {
                            'action': 'search_clients',
                            'term': $('select[name="client"]').val()
                        },
                        dataSrc: ""
                    },
                    columns: [
                        {"data": "client_type"},
                        {"data": "nit_client"},
                        {"data": "names"},
                        {"data": "city"},
                        {"data": "legal_representative"},
                        {"data": "phone"},

                    ],
                    columnDefs: [
                        {
                            targets: [0],
                            orderable: false,
                            render: function (data, type, row) {
                                if (row.client_type === 'True') {
                                    return 'Juridico'
                                } else {
                                    return 'Natural'
                                }
                            }
                    
                }
        ],
                    initComplete: function (settings, json) {

                    }
                }); 
                $('#tblClients tbody')
                .on('click', 'a[rel="details"]', function () {
                    var tr = tblHeadquarters.cell($(this).closest('td, li')).index();
                    var data = tblHeadquarters.row(tr.row)
                    console.log(data);
        
                   
         })

                $('#myModalListClient').modal('show');

                $('.btnClearSearch').on('click', function () {
                    $('select[name="search"]').val('').focus();
            
                })

    
        
            });


//Modal para crear una sede desde la venta

$('select[name="headquarters"]').select2({
    theme: "bootstrap4",
    language: 'es',
    allowClear: true,
    ajax: {
        delay: 250,
        type: 'POST',
        url: window.location.pathname,
        data: function (params) {
            var queryParameters = {
                term: params.term,
                action: 'search_headquarters'
            }
            return queryParameters;
        },
        processResults: function (data) {
            return {
                results: data
            };
        },
    },
    placeholder: 'Ingrese el nombre de la sede',
    minimumInputLength: 1,

});



//Modal de listar sede
 /*            $('.btnListH').on('click', function () { 
       
                $('#tblH').DataTable({
                           responsive: true,
                           autoWidth: false,
                           destroy: true,
                           deferRender: true,
                           ajax: {
                               url: window.location.pathname,
                               type: 'POST',
                               data: {
                                   'action': 'search_headquarters',
                                   'term': $('select[name="headquarters"]').val()
                               },
                               dataSrc: ""
                           },
                           columns: [
                               {"data": "grouped"},
                               {"data": "state"},
                               {"data": "client.nit_client"},
                               {"data": "client.names"},
                               {"data": "name"},
                               {"data": "addres"},
                               {"data": "city"},
            
                           ],
                           columnDefs: [
                            {
                                targets: [0],
                                orderable: false,
                                render: function (data, type, row) {
                
                                    buttons = '<a title="Añadir sede" rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                                    
                                    return buttons;
                                }
                            },
                            
                               {
                                   targets: [1],
                                   orderable: false,
                                   render: function (data, type, row) {
                                       if (row.state === 'True') {
                                           return '🟢'
                                       } else {
                                           return '🔴'
                                       }
                                   }
                           
                       }
               ],
                           initComplete: function (settings, json) {
            
                           }
            
                       })
            
                       $('#myModalListH').modal('show');
            
            });
 */
}).on('select2:select', function (e) {
    var data = e.params.data;
    console.log(data);

});

$(document).ready( function () {
    $('#TableH').DataTable( {
        responsive: true

     })

        });




    
//-------WIZARD-------------------------------

$(document).ready(function () {

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;

    setProgressBar(current);

    $(".next").click(function () {

        current_fs = $(this).parent();
        next_fs = $(this).parent().next();

        //Add Class Active
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

        //show the next fieldset
        next_fs.show();
        //hide the current fieldset with style
        current_fs.animate({
            opacity: 0
        }, {
            step: function (now) {
                // for making fielset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({
                    'opacity': opacity
                });
            },
            duration: 500
        });
        setProgressBar(++current);
    });

    $(".previous").click(function () {

        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();

        //Remove class active
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

        //show the previous fieldset
        previous_fs.show();

        //hide the current fieldset with style
        current_fs.animate({
            opacity: 0
        }, {
            step: function (now) {
                // for making fielset appear animation
                opacity = 1 - now;

                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previous_fs.css({
                    'opacity': opacity
                });
            },
            duration: 500
        });
        setProgressBar(--current);
    });

    function setProgressBar(curStep) {
        var percent = parseFloat(100 / steps) * curStep;
        percent = percent.toFixed();
        $(".progress-bar")
            .css("width", percent + "%")
    }

    /* $(".submit").click(function () {
        return false;
    }) */

});
