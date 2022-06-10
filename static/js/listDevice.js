$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {
                class: 'text-center',   
                "data": "state"
            },
            
            {"data": "name"},
            {"data": "brand"},
            {"data": "mac"},

            {"data": "model"},
            {"data": "serial"},
            {"data": "value"},
            {"data": "description"},
            {"data": "image"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="'+data+'" class="img-fluid d-block mx-auto" style="width: 70px; height: 70px;">';
                }
            },

            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/warehouse/device/update/' + row.id + '" class="btn btn-info btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/warehouse/device/delete/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});