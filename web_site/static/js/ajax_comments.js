$(document).ready(function () {
    ajaxComments();
    callCommentForm();
});


function callCommentForm() {
    const changeCommentBtn = $("[data-comment-id] #change-comment-btn")
    const createSubCommentBtn = $("[data-comment-id] #create-subcomment-btn")

    changeCommentBtn.on('click', function (event) {
        event.preventDefault();
        let commentId = $(this).parent().parent().attr("data-comment-id"); // $(this).parents("[data-comment-id]").attr("data-comment-id");
        let comment = $(this).parent().parent();
        console.log(comment)
        $("#comment").children("#form-container").empty();

        comment.children("#form-container").append("<form id=\"comment-multiform\" data-form-comment-id=\"{{ comment.id }}\" data-http-method=\"\" name=\"comment\"><label for=\"comment-multiform-text-area\">Change your comment</label><textarea name=\"comment-text\" class=\"form-control\" id=\"comment-multiform-text-area\" type=\"comment\" rows=\"3\"></textarea><button type=\"submit\" class=\"btn btn-warning\">Submit</button></form>");
        debugger;
        let commentForm = $("#comment-multiform")
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
                    console.log("WE DID IT!");
                },
            });
        })
    });

    createSubCommentBtn.on('click', function (event) {
        event.preventDefault();
        let commentId = $(this).parent().parent().attr("data-comment-id"); // $(this).parents("[data-comment-id]").attr("data-comment-id");
        let comment = $(this).parent().parent();
        console.log(comment)
        let parent = comment.attr("id");
        let urlParent = comment.parents("#photo").attr("id");
        let urlParentId = comment.parents("#photo").attr("data-photo-id");
        $("#comment").find("#form-container").empty();

        comment.find("#form-container").append("<form id=\"comment-multiform\" data-form-comment-id=\"{{ comment.id }}\" data-http-method=\"\" name=\"comment\"><label for=\"comment-multiform-text-area\">Enter your answer</label><textarea name=\"comment-text\" class=\"form-control\" id=\"comment-multiform-text-area\" type=\"comment\" rows=\"3\"></textarea><button type=\"submit\" class=\"btn btn-warning\">Submit</button></form>");
        debugger;
        let commentForm = $("#comment-multiform")

        commentForm.on("submit", function (event) {
            event.preventDefault()
            let commentText = commentForm.children("#comment-multiform-text-area").val()
            console.log(commentText)

            $.ajax({
                type: 'POST',
                url: `http://127.0.0.1:8000/${urlParent}/${urlParentId}/comments/`,
                data: {
                    'parent': parent,
                    'parent_id': commentId,
                    'comment_text': commentText,
                },
                success: function (response) {
                    console.log("WE DID IT!");
                },
            });
        })
    });
}

function ajaxComments() {
    let commentForm = $("#create-comment-form");
    let photoId = $("#photo").attr("data-photo-id");
    let parent = $("#photo").attr("id");
    let getAnswersBtn = $("[data-comment-id]").children('#get-answers-btn');

    getAnswersBtn.click(function (event) {
        event.preventDefault();
        let comment = $(this).parent().parent();
        let answerParent = $(this).parent().attr('id');
        let parentId = $(this).parent().attr('data-comment-id');

        console.log(answerParent)
        console.log(parentId)

        $.ajax({
            type: 'GET',
            url: `http://127.0.0.1:8000/${answerParent}/${parentId}/comments/`,

            success: function (response) {
                comment.find("#sub-comments").append(response)
            }
        })
    });

    commentForm.submit(function (event) {
        event.preventDefault();
        let commentText = commentForm.children("#create-comment-text-area").val()
        console.log(commentText)
        console.log('button was pressed')

        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:8000/${parent}/${photoId}/comments/`,
            data: {
                'parent': parent,
                'parent_id': photoId,
                'comment_text': commentText
            },
            success: function (response) {
                $('#comments').append($(response).html());
            },
        });
    });

    $("[data-delete-btn-comment-id]").click(function (event) {
        event.preventDefault();
        const commentId = $(this).attr("data-delete-btn-comment-id");
        console.log("delete button clicked");

        $.ajax({
            type: 'DELETE',
            url: `/comments/${commentId}`,
            success: function (response) {
                console.log("Worked")
                console.log(commentId)
            }
        })
    });
}