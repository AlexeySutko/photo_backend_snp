$(document).ready(function () {
    // callCommentCollection
    console.log(window.location.href.concat("comments"))
    let paramStorage = localStorage;
    paramStorage.setItem('page', '1');
    $.ajax({
        type: "GET",
        url: window.location.href.concat("comments"),
        data: {
            'page': paramStorage.getItem('page'),
        },
        success: function (response) {
            $(".comments").append(response)
            infiniteScroll();
            addSubmitListenerToCommentForm();
            callChangeOrAnswerCommentForm();
            addClickListenerOnAnswersBtnAndDeleteBtn();

        }
    });
});

function infiniteScroll() {
    let lastComment = $(".comment").last();
    let paramStorage = localStorage;

    paramStorage.setItem('page', String(Number(paramStorage.getItem('page')) + 1))

    window.addEventListener("scroll", function Scrolling(event) {
        console.log(isScrolledIntoView(lastComment));
        if (isScrolledIntoView(lastComment)) {
            window.removeEventListener("scroll", Scrolling, false);

            $.ajax({
                type: 'GET',
                url: window.location.href.concat("comments"),
                data: {
                    "page": paramStorage.getItem('page')
                },

                success: function (response) {
                    $(".comments").append(response);
                    debugger;
                    infiniteScroll();
                    addSubmitListenerToCommentForm();
                    callChangeOrAnswerCommentForm();
                    addClickListenerOnAnswersBtnAndDeleteBtn();
                }
            });
        }
    });
}

function callChangeOrAnswerCommentForm() {
    const changeCommentBtn = $("[data-comment-id] .change-comment-btn")
    const createSubCommentBtn = $("[data-comment-id] .create-subcomment-btn")


    const callChangeForm = function (event) {
        event.preventDefault();
        let commentId = $(this).parent().parent().attr("data-comment-id"); // $(this).parents("[data-comment-id]").attr("data-comment-id");
        let comment = $(this).parent().parent();
        console.log(comment)
        $(".comment-multiform").remove();

        comment.children('.comment-control-buttons').append("<form class=\"comment-multiform\" data-form-comment-id=\"{{ comment.id }}\" name=\"comment\"><label for=\"comment-multiform-text-area\">Change your comment</label><textarea name=\"comment-text\" class=\"form-control\" id=\"comment-multiform-text-area\" type=\"comment\" rows=\"3\"></textarea><button type=\"submit\" class=\"btn btn-warning\">Submit</button></form>");
        debugger;
        let commentForm = $(".comment-multiform")
        commentForm.on("submit", function (event) {
            event.preventDefault()
            let commentText = commentForm.children("#comment-multiform-text-area").val()
            console.log(commentText)
            $.ajax({
                type: 'PUT',
                url: `/comments/${commentId}`,
                data: JSON.stringify({
                    'comment_text': commentText,
                }),
                success: function (response) {
                    $(".comment-multiform").remove();
                    comment.replaceWith(response)
                    addSubmitListenerToCommentForm();
                    callChangeOrAnswerCommentForm();
                    addClickListenerOnAnswersBtnAndDeleteBtn();
                },
            });
        });
    }

    changeCommentBtn.off('click');
    changeCommentBtn.on('click', callChangeForm);

    createSubCommentBtn.on('click', function (event) {
        event.preventDefault();
        let commentId = $(this).parent().parent().attr("data-comment-id"); // $(this).parents("[data-comment-id]").attr("data-comment-id");
        let comment = $(this).parent().parent();
        let urlParentId = comment.parents("#photo").attr("data-photo-id");
        $(".comment-multiform").remove();

        comment.children('.comment-control-buttons').append("<form class=\"comment-multiform\" name=\"comment\"><label for=\"comment-multiform-text-area\">Enter your answer</label><textarea name=\"comment-text\" class=\"form-control\" id=\"comment-multiform-text-area\" type=\"comment\" rows=\"3\"></textarea><button type=\"submit\" class=\"btn btn-warning\">Submit</button></form>");
        debugger;
        let commentForm = $(".comment-multiform")

        commentForm.on("submit", function (event) {
            event.preventDefault()
            let commentText = commentForm.children("#comment-multiform-text-area").val()
            console.log(commentText)

            $.ajax({
                type: 'POST',
                url: `/photo/${urlParentId}/comments/`,
                data: {
                    'parent': 'comment',
                    'parent_id': commentId,
                    'comment_text': commentText,
                },
                success: function (response) {
                    $(".comment-multiform").remove();
                    comment.append("<div class=\"sub-comments\" >" + response + "</div>")
                    comment.children(".answer-counter").text().replaceWith(comment.children(".answer-counter").val() + 1)
                    debugger;
                    addSubmitListenerToCommentForm();
                    callChangeOrAnswerCommentForm();
                    addClickListenerOnAnswersBtnAndDeleteBtn();
                },
            });
        })
    });
}

function addSubmitListenerToCommentForm() {
    let commentForm = $("#create-comment-form");
    let photoId = $("#photo").attr("data-photo-id");
    let parent = $("#photo").attr("id");
    commentForm.off('submit');
    commentForm.on('submit', function (event) {
        event.preventDefault().stopPropagation();
        let commentText = commentForm.children("#create-comment-text-area").val()
        console.log(commentText)
        console.log('button was pressed')

        $.ajax({
            type: 'POST',
            url: `/photo/${photoId}/comments/`,
            data: {
                'parent': parent,
                'parent_id': photoId,
                'comment_text': commentText
            },
            success: function (response) {
                commentForm.children("#create-comment-text-area").val().empty()
                $(".comments").append(response);
                addSubmitListenerToCommentForm();
                callChangeOrAnswerCommentForm();
                addClickListenerOnAnswersBtnAndDeleteBtn();
            },
        });
    });
}

function addClickListenerOnAnswersBtnAndDeleteBtn() {
    let getAnswersBtn = $("[data-comment-id]").children('.get-answers-btn');

    getAnswersBtn.off("click");
    getAnswersBtn.on("click", function (event) {
        event.preventDefault();
        let comment = $(this).parent();
        let parentId = $(this).parent().attr('data-comment-id');
        $(this).addClass("d-none")
        debugger;

        console.log(parentId)

        $.ajax({
            type: 'GET',
            url: `/comment/${parentId}/comments/`,

            success: function (response) {
                comment.find(".sub-comments").append(response);
                addSubmitListenerToCommentForm();
                callChangeOrAnswerCommentForm();
                addClickListenerOnAnswersBtnAndDeleteBtn();
            }
        })
    });

    $("[data-delete-btn-comment-id]").off('click')
    $("[data-delete-btn-comment-id]").on('click', function (event) {
        event.preventDefault();
        let comment = $(this).parent().parent();
        const commentId = $(this).attr("data-delete-btn-comment-id");

        $.ajax({
            type: 'DELETE',
            url: `/comments/${commentId}`,
            success: function (response) {
                console.log("Worked")
                comment.remove()
            },
            error: function (response) {
                console.log(response)
                let message = response.responseJSON['comment_id'][0]
                comment.append(message)
            }
        })
    });
}

function isScrolledIntoView(elem) {
    let docViewTop = $(window).scrollTop();
    let docViewBottom = docViewTop + $(window).height();

    let elemTop = $(elem).offset().top;
    let elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}