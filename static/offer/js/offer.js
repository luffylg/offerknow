function main() {
    $('#delete-btn').click(function () {
        return confirm('确认删除？');
    });

    $('select.dropdown').dropdown();

    $('#rangestart').calendar({
        type: 'date',
        today: true,
        endCalendar: $('#rangeend'),
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

    $('#rangeend').calendar({
        type: 'date',
        today: true,
        startCalendar: $('#rangestart'),
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
}

$(document).ready(function () {
    main();
});