$(document).ready(function() {
    poll();
});

function poll() {
    refresh_fermenter(0);
    setTimeout(poll,5000);
}

function refresh_fermenter(id) {
    $.get('api/fermenter/refresh/' + id, function(data) {
        $("#fermenter" + id).find(".text-actual-temperature").text(data.temperature);
        $("#fermenter" + id).find(".text-actual-temperature-time").text(data.temperature_read_time);
    });
}
