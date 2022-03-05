$(document).ready(function () {

    $("[data-like-photo-id]").click(function (event) {
        event.preventDefault();
        const url = $(this).attr('url');
        const photo_id = $(this).attr('value');

        $.ajax({
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            url: url,
            data: JSON.stringify({
                'photo_id': photo_id
            }),
            success: function (response) {
                let like_counter_update = response + ' Liked'
                console.log('success', like_counter_update)
                $('[data-like-photo-id]').css('display', 'none')
                $('[data-unlike-photo-id]').css('display', 'block')
                $(`.like-counter${photo_id}`).text(like_counter_update)
            },
            error: function (response) {
                let error_obj = response.responseJSON['photo_id'][0]
                console.log(error_obj)
                $(`.like-counter${photo_id}`).text(error_obj)

            }
        })
    })


    $("[data-unlike-photo-id]").click(function (event) {
        event.preventDefault();
        const url = $(this).attr('url');
        let photo_id = $(this).attr('value');

        //The problem with setting type as DELETE by default is:
        //     'photo_id': request.DELETE['photo_id']
        // AttributeError: 'ASGIRequest' object has no attribute 'DELETE'

        $.ajax({
            type: 'DELETE',
            dataType: 'json',
            contentType: 'application/json',
            url: url,
            data: JSON.stringify({
                'photo_id': photo_id
            }),
            success: function (response) {
                let like_counter_update = response + " Liked"
                console.log('success', like_counter_update)
                $('[data-unlike-photo-id]').css('display', 'none')
                $('[data-like-photo-id]').css('display', 'block')
                $(`.like-counter${photo_id}`).text(like_counter_update)
            },
            error: function (response) {
                let error_obj = response.responseJSON['photo_id'][0]
                console.log('error', error_obj)
                $(`.like-counter${photo_id}`).text(error_obj)
            }
        })
    })
})
