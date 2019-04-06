function previewImage(event){
    var reader = new FileReader();
    var imageField = document.getElementById('image-field')

    reader.onload = function(){
        if (reader.readyState == 2) {
            imageField.src = reader.result;
        }
    }
    reader.readAsDataURL(event.target.files[0]);
    console.log("Starting");
        $("#submit").click(function(){
    
            var fd = new FormData();
            var files = $('#file-field')[0].files[0];
            fd.append('file',files);
            
            $('#disorder').css('display', 'none');
            $('#score').css('display', 'none');
            $('#predtext').css('display', 'none');
            $('#loader').css('display', 'inline');

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
                        $('#loader').css('display', 'none');
                        $('#disorder').text("Disorder: " + result.message);
                        $('#disorder').css('display', 'inline');
                        $('#score').text("Confidence Score: " + result.score);
                        $('#score').css('display', 'inline');
                    }else{
                        $('#disorder').text(result.message);
                        $('#disorder').css('color', 'red');
                    }
                },
            });
        });

}