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
            {"data": "service.name"},
            {"data": "cod_open"},
            {"data": "sub_service.name"},
            {"data": "component.name"},
            {"data": "device"},
            {"data": "description"},
            {"data": "id"},
        ],
        columnDefs: [
            
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                     var buttons = '<a href="/warehouse/product/update/' + row.id + '" class="btn btn-info btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/warehouse/product/delete/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});