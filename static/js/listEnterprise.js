

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
                "data": "state",
            },
            {"data": "legal_representive.full_name_and_nit"},
            {"data": "nit_enterprise"},
            {"data": "name"},
            {"data": "phone"},
            {"data": "segment.name"},
            {"data": "niche.name"},
        ],
        columnDefs: [
            {
                targets: [8],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/enterprise/update/' + row.id + '" class="btn btn-info btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/enterprise/delete/' + row.id + '" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});