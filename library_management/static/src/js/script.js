$(document).ready(function(){
    $(".select2").select2();
    $("#jsonForm").submit(function(event){

        event.preventDefault();
        var formData = $(this).serializeArray();
        var newData = {}
        formData.forEach(function(value,key){
            newData[value.name] = value.value
        });
        

        var jsonData = JSON.stringify({
            jsonrpc:"2.0",
            method:"call",
            params:{
                model:"book.books",
                method:"create",
                args:[newData]
            }
        });

        $.ajax({
            type:"POST",
            url:"/book/addBookJson",
            data:jsonData,
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            success:function(response){
                
                if(response.result){
                    $('#addBook').append(response.result);
                    $('#jsonForm').get(0).reset()
                    $('#exampleModalJson').hide()

                }
                else{
                    
                }
            },
            error:function(){
                
            }
        })
    })
});




