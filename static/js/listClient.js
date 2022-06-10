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
            {"data": "id"},
            {
                class: 'text-bold',
                "data": "id"
            },
            {"data": "state"},
            {"data": "client_type"},
            {"data": "nit_client"},
            {"data": "names"},
            {"data": "phone"},
            {"data": "email"},
            {"data": "city"},
            {"data": "legal_representative"},
            {"data": "niche.segment.name"},
            {"data": "niche.name"},
            {"data": "address"},
            {"data": "observations"},
            
        ],
        columnDefs: [
            {
                targets: [0],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {

                    var buttons = '<a title="Actualizar cliente" href="/erp/customer/update/' + row.id + '" class="btn btn-success btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a title="Eliminar cliente" href="/erp/customer/delete/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    //buttons += '<a rel="details" class="btn btn-info btn-xs btn-flat"><i class="fas fa-eye"></i></a> ';
                    //buttons += '<a href="" target="_blank" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-history"></i></a> ';
                    return buttons;
                }
            },
            {
                targets: [3],
                class: 'text-bold',
                orderable: false,
                render: function (data, type, row) {
                    if (row.client_type === 'True') {
                        return 'Juridico'
                    } else {
                        return 'Natural'
                    }
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });

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
                'action': 'search_details_client',
                'id': data.id,
            },
            dataSrc: ""
        },
        columns: [
            {"data": "nit_client"},
            {"data": "names"},
            {"data": "address"},
            {"data": "city"},
            {"data": "legal_representative"},
            {"data": "phone"},
            {"data": "segment"},
            {"data": "niche"},
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