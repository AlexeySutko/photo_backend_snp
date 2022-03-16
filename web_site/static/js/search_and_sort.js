$(document).ready(function () {
    localStorage.clear();
    ajaxSort();
    ajaxSearch();
})

function ajaxSort() {
    $("[data-sort-by]").click(function (event) {
        let paramStorage = localStorage;
        event.preventDefault();
        const param = $(this).attr('data-sort-by');
        paramStorage.setItem('sorted_by', param);

        console.log($(this), param);
        console.log(paramStorage);

        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/test',
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string')
            },
            success: function (response) {
                $('#photos').empty();
                $('#photos').append($(response).filter('#photos').html());

                $('#pagination').empty();
                $('#pagination').append($(response).find('#pagination').html());
                asignControls();
            },
            error: function (response) {
                console.log('failed')
            },
        });
    });
}

function ajaxSearch() {
    $("#search-bar").submit(function (event) {
        let paramStorage = localStorage;
        event.preventDefault();
        let
            form = document.forms.search
        formData = new FormData(form)
        ;
        const param = formData.get("search_string");
        paramStorage.setItem('search_string', param);

        console.log($(this), param);
        console.log(paramStorage);

        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:8000/test',
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string')
            },
            success: function (response) {
                $('#photos').empty();
                $('#photos').append($(response).filter('#photos').html());

                $('#pagination').empty();
                $('#pagination').append($(response).find('#pagination').html());
                asignControls();
            },
            error: function (response) {
                console.log('failed', response)
            },
        });
    });
}