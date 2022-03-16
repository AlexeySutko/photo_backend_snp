function asignControls(){
    ajaxPagination();
}

function ajaxPagination() {
    $('#pagination button.page-link').each((index, elem) => {
        $(elem).on('click', (event) => {
            debugger;
            let paramStorage = localStorage;
            let page_url = $(elem).attr('url');
            paramStorage.setItem('page', page_url);
            event.preventDefault();
            console.log(paramStorage.getItem('page'));

            $.ajax({
                type: 'GET',
                data: {
                    'page' : paramStorage.getItem('page'),
                    'sorted_by': paramStorage.getItem('sorted_by'),
                    'search_string': paramStorage.getItem('search_string'),
                },
                success: (response) => {
                    $('#photos').empty();
                    $('#photos').append($(response).filter('#photos').html());

                    $('#pagination').empty();
                    $('#pagination').append($(response).find('#pagination').html());
                    asignControls()
                },
            })
        })
    })
}

$(document).ready(function () {
    ajaxPagination()
})

$(document).ajaxStop(function () {
    ajaxPagination()
})