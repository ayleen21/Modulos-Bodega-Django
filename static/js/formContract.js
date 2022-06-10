var tblProducts;
var vents = {
    items: {
        contract_cli: '',
        // contract_enterprise: '',
        date_joined: '',
        subtotal: 0.00,
        total: 0.00,
        products: []
    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        $.each(this.items.products, function (pos, dict) {
            dict.pos = pos;
            dict.subtotal = dict.cant * parseFloat(dict.pvp);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.total = this.items.subtotal;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function(item){
        this.items.products.push(item);
        this.list();
    },
    list: function(){
            this.calculate_invoice();

           tblProducts = $('#tblProducts').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                data: this.items.products,
                columns: [
                    {"data": "id"},
                    {"data": "pvp"},
                    {"data": "cant"},
                    {"data": "subtotal"},
                ],
                columnDefs: [
                    {
                        targets: [0],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) { 
                            return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';    
                        }
                    },
                    {
                        targets: [-3],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) { 
                            return '$'+parseFloat(data).toFixed(2);    
                        }
                    },
                    {
                        targets: [-2],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) { 
                            return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="'+ row.cant +'"></input>';    
                        }
                    },
                    {
                        targets: [-1],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) { 
                            return '$'+parseFloat(data).toFixed(2);    
                        }
                    },
                ],
                rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                    $(row).find('input[name="cant"]').TouchSpin({
                        min: 1,
                        max: data.stock,
                        step: 1
                    });
    
                },
                initComplete: function (settings, json) {
                }
            });
    }
};

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
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
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            console.log(vents.items)
            vents.add(ui.item);

            $(this).val('');
        }
    });

   // search clients

//    $('select[name="cli"]').select2({
//     theme: "bootstrap4",
//     language: 'es',
//     allowClear: true,
//     ajax: {
//         delay: 250,
//         type: 'POST',
//         url: window.location.pathname,
//         data: function (params) {
//             var queryParameters = {
//                 term: params.term,
//                 action: 'search_clients'
//             }
//             return queryParameters;
//         },
//         processResults: function (data) {
//             return {
//                 results: data
//             };
//         },
//     },
//     placeholder: 'Ingrese una descripción',
//     minimumInputLength: 1,
// });

// $('.btnAddClient').on('click', function () {
//     $('#myModalClient').modal('show');
// });

// $('#myModalClient').on('hidden.bs.modal', function (e) {
//     $('#frmClient').trigger('reset');
// })

// $('#frmClient').on('submit', function (e) {
//     e.preventDefault();
//     var parameters = new FormData(this);
//     parameters.append('action', 'create_client');
//     submit_with_ajax(window.location.pathname, 'Notificación',
//         '¿Estas seguro de crear al siguiente cliente?', parameters, function (response) {
//             //console.log(response);
//             var newOption = new Option(response.full_name, response.id, false, true);
//             $('select[name="cli"]').append(newOption).trigger('change');
//             $('#myModalClient').modal('hide');
//         });
// });

    

    $('.btnRemoveAll').on('click', function () {
        if (vents.items.products.length === 0) return false;
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function () {
            vents.items.products = [];
            vents.list();
        }, function () {

        });
    });

    //event cant
    $('#tblProducts tbody')
    .on('click', 'a[rel="remove"]', function () {
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?',
            function () {
                vents.items.products.splice(tr.row, 1);
                vents.list();
            }, function () {

            });
    })
    
    .on('change', 'input[name="cant"]', function(){
        console.clear()
        var cant = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        console.log(tr)
        var data = tblProducts.row(tr.row).data()
        vents.items.products[tr.row].cant = cant;
        vents.calculate_invoice()
        $('td:eq(5)', tblProducts.row(tr.row).node()).html('$' + vents.items.products[tr.row].subtotal.toFixed(2));
        // console.log(vents.items.products);
    })

    $('.btnClearSearch').on('click', function () {
        $('input[name="search"]').val('').focus();
    });

    //event submit
    $('#frmSale').on('submit', function (e) {
        e.preventDefault();

        if (vents.items.products.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.date_joined = $('input[name="date_joined"]').val();
        vents.items.contract_cli = $('select[name="contract_cli"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {
                alert_action('Notificación', '¿Desea imprimir la boleta de venta?', function () {
                    window.open('/erp/sale/invoice/pdf/' + response.id + '/', '_blank');
                    location.href = '/erp/sale/list/';
                }, function () {
                    location.href = '/erp/sale/list/';
                });
            });
    });
})