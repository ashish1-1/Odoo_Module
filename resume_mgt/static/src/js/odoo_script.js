odoo.define("wk_ashish_varshney_resume_mgt.odoo_script", function (require) {
  "use strict";
  $(".select2").select2();
  // $("#add_btn_div").hide();
  var education_list = [];

  // $("#validate_btn").click(function(event){
  //   event.preventDefault();
  //   var name = $("input[name='name']").val();
  //   if ( name.match('^[a-zA-Z]{3,16}$') ) {
  //     alert( "Give Valid Name" );
  // }
  // });
  // $('#validate_btn').click(function(e){
  //   e.preventDefault();
  //   var date = $("#DOB").val()

  //   if (underAgeValidate(date)){
  //     $("#dobDiv").append("<div class='invalid-feedback' id='addon'>Give Valid Date</div>")
  //     $("#addon").prop('style',"display:block");
  //   }
  //   else{
  //     $("#form_data").submit();
  //   }
  // })
  // function underAgeValidate(birthday){
  //   // it will accept two types of format yyyy-mm-dd and yyyy/mm/dd
  //   var optimizedBirthday = birthday.replace(/-/g, "/");

  //   //set date based on birthday at 01:00:00 hours GMT+0100 (CET)
  //   var myBirthday = new Date(optimizedBirthday);

  //   // set current day on 01:00:00 hours GMT+0100 (CET)
  //   var currentDate = new Date().toJSON().slice(0,10)+' 01:00:00';

  //   // calculate age comparing current date and borthday
  //   var myAge = ~~((Date.now(currentDate) - myBirthday) / (31557600000));
  //   // console.log(myAge)
  //   if(myAge < 18) {
  //            return true;
  //         }
  //   if(myAge>100){
  //     return true
  //   }

  //   return false;

  // }

  //==========================================EDUCATION FROM JASON IT CREATE RECORD THEN SUBMITTING FORM IT LINK IDS WITH RESUME:=========================
  //     var new_edu_html = $("#add_edu").html()
  //     $("#save_data_btn").click(function(event){

  //       var edu_data = {
  //         'board' : $("input[name='board']").last().val(),
  //         'school_college':$("input[name='school_college']").last().val(),
  //         'year':$("input[name='year']").last().val(),
  //         'max_marks':parseInt($("input[name='max_marks']").last().val()),
  //         'marks_obtained':parseInt($("input[name='marks_obtained']").last().val()),
  //         'degree':$("input[name='degree']").last().val()
  //       }
  //       let flag = 0
  //       if(edu_data.max_marks < edu_data.marks_obtained){
  //       $('#alertBox').prop('style','display:block')
  //       $('#alertBox').html('Marks Obtained should be less than Maximum Marks')
  //       flag = 1
  //       return false;
  //     }
  //     else{
  //       $('#alertBox').prop('style','display:none')
  //           flag=0;
  //     }
  //       $.each( edu_data, function( key, value ) {
  //         if (value == "" || value == NaN){
  //           $('#alertBox').prop('style','display:block')
  //           $('#alertBox').html('Please Fill complete Education')
  //           flag = 1
  //           return false;
  //         }
  //         else{
  //           $('#alertBox').prop('style','display:none')
  //           flag=0;
  //         }
  //       });

  //     if(flag == 1){
  //       return false;
  //     }
  //   var ajax = require('web.ajax');
  //     return ajax.jsonRpc('/add/education', 'call',{
  //       'param':edu_data,
  //     }).then(function (result) {
  //       result = JSON.parse(result)
  //       education_list.push(result.id)
  //       $("#education_background_id").val(education_list);
        // $("#add_edu").append(new_edu_html);
  // });
  // });

  //========================== SAVE EDUCATION DATA:============================================
  var edu_all_data = [];
  var add_flag = false;
  var new_edu_html = $("#add_edu").html();
  $("button[name='save']").last().click(function () {
    console.log(edu_all_data)
    var edu_data = {
      board: $("input[name='board']").last().val(),
      school_college: $("input[name='school_college']").last().val(),
      year: $("input[name='year']").last().val(),
      max_marks: $("input[name='max_marks']").last().val(),
      marks_obtained: $("input[name='marks_obtained']").last().val(),
      degree: $("input[name='degree']").last().val(),
    };
    let flag = 0;
    if (parseInt(edu_data.max_marks) < parseInt(edu_data.marks_obtained)) {
      $("#alertBox").prop("style", "display:block");
      $("#alertBox").html("Marks Obtained should be less than Maximum Marks");
      flag = 1;
      return false;
    } else {
      $("#alertBox").prop("style", "display:none");
      flag = 0;
    }

    $.each(edu_data, function (key, value) {
      if (value == "") {
        $("#alertBox").prop("style", "display:block");
        $("#alertBox").html("Please Fill complete Education");
        flag = 1;
        return false;
      }else {
        $("#alertBox").prop("style", "display:none");
        flag = 0;
      }
    });

    if(flag == 1){
      return false;
    }
    edu_all_data.push(edu_data)
    console.log(edu_all_data);
    add_flag = true;

    $("button[name='save']").prop("style", "display:none");
    $("button[name='add']").prop("style", "display:block");

  });

  $("button[name='add']").last().click(function(){
  
  $("#add_edu").append(new_edu_html);
  $("button[name='save']").prop("style", "display:block");

  $("button[name='add']").prop("style", "display:none");

  });



  $("select.countries").change(function () {
    var selectedCountry = $(".countries option:selected").val();

    var ajax = require("web.ajax");
    return ajax
      .jsonRpc("/countries", "call", {
        param: selectedCountry,
      })
      .then(function (result) {
        if (result != undefined) {
          result = JSON.parse(result);
          $("#state").empty();
          $("#state").append("<option>Select a state</option>");
          for (var val = 0; val < result.id.length; val++) {
            $("#state").append(
              '<option value="' +
                result.id[val] +
                '" class="">' +
                result.name[val] +
                "</option>"
            );
          }
        }
      });
  });

  var hobbies_ids = []
  $("#form_data").submit(function (event) {
    // if ($("#education_background_id").val() == "") {
    //   $("#alertBox").prop("style", "display:block");
    //   $("#alertBox").html("Fill Atleast one education And click to add button");
    //   return false;
    // }

    // return true;

    event.preventDefault();
    if (add_flag == false){
      $("#alertBox").html("Please Fill complete Education");
      return true;
    }
    var edu_data = {
      board: $("input[name='board']").last().val(),
      school_college: $("input[name='school_college']").last().val(),
      year: $("input[name='year']").last().val(),
      max_marks: $("input[name='max_marks']").last().val(),
      marks_obtained: $("input[name='marks_obtained']").last().val(),
      degree: $("input[name='degree']").last().val(),
    };
    let flag = 0;
    if (parseInt(edu_data.max_marks) < parseInt(edu_data.marks_obtained)) {
      $("#alertBox").prop("style", "display:block");
      $("#alertBox").html("Marks Obtained should be less than Maximum Marks");
      flag = 1;
      return false;
    } else {
      $("#alertBox").prop("style", "display:none");
      flag = 0;
    }
    $.each(edu_data, function (key, value) {
      if (value == "") {
        $("#alertBox").prop("style", "display:block");
        
        flag = 1;
        return false;
      }else {
        $("#alertBox").prop("style", "display:none");
        flag = 0;
      }
    });

    if(flag == 1){
      return false;
    }
    else{


    var new_record = {}
    var formData = $(this).serializeArray();
    console.log(formData);

    formData.forEach(function(value,key){
      if(value.name == 'hobbies_ids'){
        hobbies_ids.push(value.value)
      }
      new_record[value.name] = value.value
      
  });
  console.log(new_record)
  new_record['edcation_ids'] = edu_all_data
  new_record['hobbies_ids'] = hobbies_ids
  console.log(new_record)

    var ajax = require('web.ajax');
      return ajax.jsonRpc('/resume-form', 'call',{
        'param':new_record,
      }).then(function (result) {
        result = JSON.parse(result)
        if(result.id != undefined){

          window.location.href = "/resume/";
        }
  });
    }
  });
});
