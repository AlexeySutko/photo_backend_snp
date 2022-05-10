$(document).ready(function () {
    notifications();
});


function notifications() {
    const notificationSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/notifications/'
    );

    notificationSocket.onopen = function (event) {
        console.log("connection is open")
        notificationSocket.send(JSON.stringify({
            "type": "ping",
        }));
    }

    notificationSocket.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log(data)
        $("<body>").append(`<div> ${data.message} </div>`)
    }
}