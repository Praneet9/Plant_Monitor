function previewImage(event){
    var reader = new FileReader();
    var imageField = document.getElementById('image-field')

    reader.onload = function(){
        if (reader.readyState == 2) {
            imageField.src = reader.result;
        }
    }
    reader.readAsDataURL(event.target.files[0]);
    event.preventDefault();
}

$("#image_upload").click(function(){
    
    var fd = new FormData();
    var files = $('#file-field')[0].files[0];
    fd.append('file',files);
    
    $('#disorder').css('display', 'none');
    $('#score').css('display', 'none');
    $('#predtext_image').css('display', 'none');
    $('#loader_image').css('display', 'inline');

    $.ajax({
        url: '/image',
        type: 'post',
        data: fd,
        mimeType:"multipart/form-data",
        contentType: false,
        timeout: 6000,
        processData: false,
        success: function(response){
            var result = JSON.parse(response);
            console.log(result);
            if(result.status){
                $('#loader_image').css('display', 'none');
                $('#disorder').text("Disorder: " + result.message);
                $('#disorder').css('display', 'inline');
                $('#score').text("Confidence Score: " + result.score);
                $('#score').css('display', 'inline');
            }else{
                $('#loader_image').css('display', 'none');
                $('#disorder').text(result.message);
                $('#disorder').css('color', 'red');
            }
        },
    });
});

$("#sensor_data").click(function(){
    
    $('#rfc').css('display', 'none');
    $('#kmeans').css('display', 'none');
    $('#svm').css('display', 'none');
    $('#predtext_sensor').css('display', 'none');
    $('#loader_sensor').css('display', 'inline');

    var temperature = $('#temperature').val();
    var humidity = $('#humidity').val();
    var soil_moisture = $('#soil_moisture').val();

    var sensors = {"temperature": temperature, "humidity": humidity, "soil_moisture": soil_moisture};

    $.ajax({
        url: '/sensor',
        type: 'post',
        data: sensors,
        timeout: 6000,
        success: function(response){
            // var result = JSON.parse(response);
            console.log(response);
            result = response
            if(result.status){
                $('#loader_sensor').css('display', 'none');

                $('#rfc').css('display', 'inline');
                $('#kmeans').css('display', 'inline');
                $('#svm').css('display', 'inline');

                $('#rfc').text("RFC: " + result.rfc);
                $('#kmeans').text("KMeans: " + result.kmeans);
                $('#svm').text("SVM: " + result.svm);
            }else{
                $('#loader_sensor').css('display', 'none');
                $('#kmeans').css('display', 'inline');
                $('#kmeans').text(result.message);
                $('#kmeans').css('color', 'red');
            }
        },
    });
});