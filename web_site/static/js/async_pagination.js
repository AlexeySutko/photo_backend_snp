function asignControls() {
    ajaxPagination();
    ajaxSearch();
    ajaxSort();
}

$(document).ready(function () {
    ajaxPagination()
});


function ajaxPagination() {
    let paramStorage = localStorage;
    let firstPageBtn = $('#pagination .first-page-btn');
    let prevPageBtn = $('#pagination .previous-page-btn');
    let nextPageBtn = $('#pagination .next-page-btn');
    let lastPageBtn = $('#pagination .last-page-btn');
    let currentPage = paramStorage.getItem('page');

    firstPageBtn.on('click', (event) => {
        event.preventDefault();
        let newPage = firstPageBtn.attr('value');
        paramStorage.setItem('page', newPage);
        console.log(paramStorage.getItem('page'));

        $.ajax({
            type: 'GET',
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string'),
            }, success: (response) => {
                $('#photos .photos-collection').empty();
                $('#photos .photos-collection').append($(response).html());
                asignControls();

                $('.current .current-page').empty().text(newPage)

                prevPageBtn.attr('value', null)
                nextPageBtn.attr('value', String(Number(newPage) + 1))

                lastPageBtn.removeClass("d-none")
                nextPageBtn.removeClass("d-none")
                firstPageBtn.addClass("d-none")
                prevPageBtn.addClass("d-none")

            },
        })
    })
    prevPageBtn.on('click', (event) => {
        event.preventDefault();
        let newPage = prevPageBtn.attr('value');
        paramStorage.setItem('page', newPage);
        console.log(paramStorage.getItem('page'));

        $.ajax({
            type: 'GET',
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string'),
            }, success: (response) => {
                $('#photos .photos-collection').empty();
                $('#photos .photos-collection').append($(response).html());
                asignControls();

                $('.current .current-page').text(newPage)

                prevPageBtn.attr('value', String(Number(newPage) - 1))
                nextPageBtn.attr('value', String(Number(newPage) + 1))

                lastPageBtn.removeClass("d-none")
                nextPageBtn.removeClass("d-none")

                if (Number(paramStorage.getItem('page')) === Number(firstPageBtn.attr('value'))) {
                    prevPageBtn.attr('value', null)
                    nextPageBtn.attr('value', String(Number(newPage) + 1))
                    firstPageBtn.addClass("d-none")
                    prevPageBtn.addClass("d-none")
                }
            },
        })
    })
    nextPageBtn.on('click', (event) => {
        event.preventDefault();
        let newPage = nextPageBtn.attr('value');
        paramStorage.setItem('page', newPage);
        console.log(paramStorage.getItem('page'));

        $.ajax({
            type: 'GET',
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string'),
            }, success: (response) => {
                $('#photos .photos-collection').empty();
                $('#photos .photos-collection').append($(response).html());
                asignControls();

                $('.current .current-page').text(newPage)

                prevPageBtn.attr('value', String(Number(newPage) - 1))
                nextPageBtn.attr('value', String(Number(newPage) + 1))

                firstPageBtn.removeClass("d-none")
                prevPageBtn.removeClass("d-none")

                if (Number(paramStorage.getItem('page')) === Number(lastPageBtn.attr('value'))) {
                    lastPageBtn.attr('value', null)
                    prevPageBtn.attr('value', String(Number(newPage) - 1))
                    lastPageBtn.addClass("d-none")
                    nextPageBtn.addClass("d-none")
                }
            },
        })
    })
    lastPageBtn.on('click', (event) => {
        event.preventDefault();
        let newPage = lastPageBtn.attr('value');
        paramStorage.setItem('page', newPage);
        console.log(paramStorage.getItem('page'));

        $.ajax({
            type: 'GET',
            data: {
                'page': paramStorage.getItem('page'),
                'sorted_by': paramStorage.getItem('sorted_by'),
                'search_string': paramStorage.getItem('search_string'),
            }, success: (response) => {
                $('#photos .photos-collection').empty();
                $('#photos .photos-collection').append($(response).html());
                asignControls();

                $('.current .current-page').text(newPage)

                nextPageBtn.attr('value', null)
                prevPageBtn.attr('value', String(Number(newPage) - 1))

                firstPageBtn.removeClass("d-none")
                prevPageBtn.removeClass("d-none")
                nextPageBtn.addClass("d-none")
                lastPageBtn.addClass("d-none")

                firstPageBtn.removeClass("d-none")
                prevPageBtn.removeClass("d-none")
            },
        })
    })
}

// $(document).ajaxStop(function () {
//     ajaxPagination()
// });