odoo.define('wk_library_management.odoo_script', function(require){
  "use strict";
    $(".select2").select2();

   
    

    $("#jsonForm").submit(function(event){
        event.preventDefault();
        var formData = $(this).serializeArray();
        var newData = {}
        formData.forEach(function(value,key){
            newData[value.name] = value.value
        });

    
    var ajax = require('web.ajax');
      return ajax.jsonRpc('/book/addBookJson', 'call',{
        'param':newData,
      }).then(function (result) {
        $('#addBook').append(result);
        $('#jsonForm').get(0).reset()
        $('#exampleModalJson').hide()

    
  });
});
});