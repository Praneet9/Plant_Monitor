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
    
            $.ajax({
                url: '/image',
                type: 'post',
                data: fd,
                mimeType:"multipart/form-data",
                contentType: false,
                timeout: 6000,
                processData: false,
                success: function(response){
                    console.log(response);
                    if(response != 0){
                        // $("#img").attr("src",response); 
                        // $(".preview img").show(); // Display image element
                        console.log("Done")
                        alert('Uploaded');
                    }else{
                        console.log("Failed");
                        alert('file not uploaded');
                    }
                },
            });
        });

}