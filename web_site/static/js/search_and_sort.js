$(document).ready(function () {
    localStorage.clear();
    ajaxSort();
    ajaxSearch();
});

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
            url: window.location.href,
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string')
            },
            success: function (response) {
                $('#photos .photos-collection').empty();
                $('#photos .photos-collection').append($(response).html());
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
            url: '/',
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string')
            },
            success: function (response) {
                $('#photos .photos-collection').empty();
                $('#photos .photos-collection').append($(response).html());
            },
            error: function (response) {
                const error_obj = response?.responseJSON['search_string'][0]
                console.log(response)
                window.alert(error_obj)
            },
        });
    });
}