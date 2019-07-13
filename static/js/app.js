$(document).ready(function() {
    poll();
});

function poll() {
    device_refresh(0);
    setTimeout(poll,5000);
}

function device_refresh(id) {
    $.get('api/device/refresh/' + id, function(data) {
        $("#device" + id).find(".text-actual-temperature").text(data.temperature);
        $("#device" + id).find(".text-actual-temperature-time").text(data.temperature_read_time);
    });
}

function device_update(id, data) {
    $.ajax({
        url: "api/device/update/" + id,
        data: data
    })
}
