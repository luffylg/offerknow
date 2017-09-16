$('#delete-btn').click(function () {
    return confirm('确认删除？');
});

$('select.dropdown').dropdown();

$('.calendar-div').calendar({
    type: 'date',
    today: true,
    formatter: {
        date: function (date, settings) {
            if (!date) return '';
            var day = date.getDate();
            var month = date.getMonth() + 1;
            var year = date.getFullYear();
            return year + '-' + month + '-' + day;
        }
    },
    popupOptions: {
        position: 'bottom left'
    }
});