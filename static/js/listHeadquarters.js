var tblClient;

$(function () {
    tblClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        dom: "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>B" +
        "<'row'<'col-sm-12'tr>>" +
        "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },   
            dataSrc: ""
        },
        buttons: [
            {
                extend: 'excelHtml5',
                text: '<i class="fas fa-file-excel"></i>&nbsp; Exportar a excel',
                titleAttr: 'Exportar a Excel',
                className: 'btn btn-success'
            },
        ],
        columns: [
            {"data": "grouped"},
            {   
                class: 'text-bold',
                "data": "id"
            },
            {"data": "state"},
            {"data": "client.nit_client"},
            {"data": "client.names"},
            {"data": "name"},
            {"data": "address"},
            {"data": "city"},
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a title="Actualizar sede" href="/erp/headquarters/update/' + row.id + '" class="btn btn-info btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a title="Ver contacto" rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                    buttons += '<a title="Eliminar sede" href="/erp/headquarters/delete/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });

    
    // MODAL_CONTACTO

    $('#data tbody')
    .on('click', 'a[rel="details"]', function () {
        var tr = tblClient.cell($(this).closest('td, li')).index();
        var data = tblClient.row(tr.row).data();
        console.log(data);

    $('#tblDetalle').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'search_details_headquarters',
                'id': data.id,
            },
            dataSrc: ""
        },
        columns: [
            {"data": "contact_name"},
            {"data": "contact_phone"},
            {"data": "contact_email"},
            {"data": "observations"},
        ],
        columnDefs: [
            {
                // targets: [-1],
                // class: 'text-center',
                // orderable: false,
                // render: function (data, type, row) {
                //     var buttons = '<a href="/erp/customer/update/' + row.id + '" class="btn btn-success btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                //     // buttons += '<a href="/erp/customer/delete/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                //     buttons += '<a rel="details" class="btn btn-info btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                //     buttons += '<a href="" target="_blank" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-history"></i></a> ';
                //     return buttons;
                // }
            },
        ],
        initComplete: function (settings, json) {
        }
        });
        $('#myModal').modal('show');
    })

});