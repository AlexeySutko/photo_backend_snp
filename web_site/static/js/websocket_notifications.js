
function notifications() {
    const notificationSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/notifications/'
        + "userId" //Will be a variable
        + '/'
    );

    notificationSocket.onmessage = function (event) {
        const data = JSON.parse(event.data);
    }
}