$('#delete-btn').click(function () {
    return confirm('确认删除？');
});

$(".form_datetime").datepicker({
    format: 'yyyy-mm-dd',
    language: 'zh-CN',
    todayBtn: 'linked',
    clearBtn: true,
    todayHighlight: true,
    autoclose: true,
    orientation: "bottom auto"
});