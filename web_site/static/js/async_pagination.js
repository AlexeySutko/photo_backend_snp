
function ajaxPagination(){
    $('#pagination a.page-link').each((index, el) =>{
        $(el).click((e) => {
            e.preventDefault()
            let page_url = $(el).attr('href')
            console.log(page_url)

            $.ajax({
                url: page_url,
                type: 'GET',
                success: (response) => {
                    $('#photos').empty()
                    $('#photos').append($(response).filter('#photos').html())

                    $('#pagination').empty()
                    $('#pagination').append($(response).find('#pagination').html())
                }
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