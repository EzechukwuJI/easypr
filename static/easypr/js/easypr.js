function show_hidden_form(form_id,social_btn){
  $sc   =   $('#' + social_btn);
  $this = $('#' + form_id );
  $sc.addClass('hidden');
  $this.removeClass('hidden');
}


function hide_form(form_id,social_btn){
  $sc   =   $('#' + social_btn);
  $this = $('#' + form_id );
  $sc.removeClass('hidden');
  $this.addClass('hidden');
}

function compare_passwords(field_name, confirm_field){
      // evt.preventDefault();
      var confirm_field   =   $('#' + confirm_field);
      var password        =   $('#' + field_name);
      if (confirm_field.val() != password.val()){
          alert('The password you entered did not match.');
        return false;
      } 
      // else {
  return true;
      // }
}


function swap_reg_form(user_form, details_form){
  $user_form   =   $('#' + user_form);
  $details     =   $('#' + details_form );
  $user_form.addClass('hidden');
  $details.removeClass('hidden');
}



function load_image(pic_id, img_placeholder_id,cap_id){
    var url = document.getElementById(pic_id).value;
    var input = document.getElementById(pic_id);
    var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
    var image_placeholder = document.getElementById(img_placeholder_id);
    if (input.files && input.files[0] && (ext == "png" || ext == "jpeg" || ext == "jpg")){
      var reader = new FileReader();
      reader.onload = function (e){
        image_placeholder.src = e.target.result;
      }
      reader.readAsDataURL(input.files[0]);
      document.getElementById(cap_id).focus();
    }
    else {
      image_placeholder.src = "";
      image_placeholder.alt = "Unsupported file type"
      input.value=""
    }
  }



var div_ids = ['bank_deposit','debit_card','bank_transfer','ewallet'];
  function select_payment(div_id){
    $('#id_proceed').attr('disabled', true);
    var chosen_box  =   $('#' + div_id);
    var option   =   $('#check_' + div_id);
    if (option.is(':checked')){
      option.prop('checked', false);
      chosen_box.removeClass('selected');
    } else {
      option.prop('checked', true);
      chosen_box.addClass('selected');
    }
    var selected_div = div_ids.indexOf(div_id);
    for (id = 0; id < div_ids.length; id++){
        if (id !== selected_div ){
        $('#check_' + div_ids[id]).prop('checked',false);
        $('#' + div_ids[id]).removeClass('selected');
      }
    }
    if ($('#check_bank_deposit').is(':checked') || $('#check_bank_transfer').is(':checked')){
      $('#pay-details').removeClass('hidden');
      $("#id_payment_method").val(div_id); 
    } else {
      $('#pay-details').addClass('hidden');
    }
  }


function hide_div(div){
  var div_to_hide = $("#" + div);
  div_to_hide.addClass('hidden');
}




function show_search_div(){
      $("#id_search").html("<i class='fa fa-times search text-center'></i>"); 
      var search_box = $("#search-box");
      if (search_box.hasClass('hidden')){
        $("#search-box").addClass('animate-div');
        $("#search-box").removeClass('hidden');
      } else {
        $("#search-box").addClass('hidden');
        $("#id_search").html("<i class='fa fa-search search text-center'></i>"); 
      }
    }






// var div_ids = ['bank_deposit','debit_card','bank_transfer','ewallet'];
  function select_payment(div_id){
    $('#id_proceed').attr('disabled', true);
    var chosen_box  =   $('#' + div_id);
    var option   =   $('#check_' + div_id);
    if (option.is(':checked')){
      option.prop('checked', false);
      chosen_box.removeClass('selected');
    } else {
      option.prop('checked', true);
      chosen_box.addClass('selected');
    }
    var selected_div = div_ids.indexOf(div_id);
    for (id = 0; id < div_ids.length; id++){
        if (id !== selected_div ){
        $('#check_' + div_ids[id]).prop('checked',false);
        $('#' + div_ids[id]).removeClass('selected');
      }
    }
    if ($('#check_bank_deposit').is(':checked') || $('#check_bank_transfer').is(':checked')){
      $('#pay-details').removeClass('hidden');
      $("#id_payment_method").val(div_id); 
    } else {
      $('#pay-details').addClass('hidden');
    }
  }





function select_option(option_classname, selected_id, select_multiple){
  var selected_option_div      = $("#" + selected_id);
  var selected_option_checkbox = $("#select_" + selected_id).attr('id');
  var option_id_list  = []; // dynamic option list
  var option_selector = $("." + option_classname);
  // build dynamic option list
  for (var opt = 0; opt < option_selector.length; opt ++){
    option_id_list.push((option_selector[opt]).id);
  }
  if ($("#select_" + selected_id).is(':checked')){
    $("#select_" + selected_id).prop('checked',false);
    $("#" + selected_id).removeClass('selected');
  }
  else {
    $("#select_" + selected_id).prop('checked',true); 
    $("#" + selected_id).addClass('selected');
  }
  if (select_multiple === "No") {
    for (var item = 0; item < option_id_list.length; item++){
      if (option_id_list[item] !== selected_option_div.attr('id')){
          $("#select_" + option_id_list[item]).prop('checked', false);
          $("#" + option_id_list[item]).removeClass('selected');
        }
      }
    } 
  }





 $(".select_business_type").click(function(){
  if ((this.id === "company") && ($("#company").hasClass('selected'))){
      $("#company_type").removeClass('hidden');
   } else {
      $("#company_type").addClass('hidden'); 
   }
 })


$(".use-external-db").click(function(){
  if (this.id === "yes"){
      $("#external_db").removeClass('hidden');
   } else {
      $("#external_db").addClass('hidden'); 
   }
 })



function counter(action, display_id){
  var display  = $("#" + display_id);
  var current_count = display.val();
  if (action === "add"){
    current_count++;
    display.val(current_count);
  } else if ((action === "subtract") && (current_count >= 1)){
      current_count --;
      display.val(current_count);
  }
}



















// var isAdvancedUpload = function(){
// 	var div = document.createElement('div');
// 	return (('draggable' in div)||('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window;
// }();


// var $form  = $('.box');

// if (isAdvancedUpload){
// 	$form.addClass('has-advanced-upload');
// }


// if (isAdvancedUpload) {
//   var droppedFiles = false;
//   $form.on('drag dragstart dragend dragover dragenter dragleave drop', function(e) {
//     e.preventDefault();
//     e.stopPropagation();
//   })
//   .on('dragover dragenter', function() {
//     $form.addClass('is-dragover');
//   })
//   .on('dragleave dragend drop', function() {
//     $form.removeClass('is-dragover');
//   })
//   .on('drop', function(e) {
//     droppedFiles = e.originalEvent.dataTransfer.files;
//   });
// }


// $form.on('submit', function(e) {
//   if ($form.hasClass('is-uploading')) return false;

//   $form.addClass('is-uploading').removeClass('is-error');

//   if (isAdvancedUpload) {
//     // ajax for modern browsers
//   } else {
//   	var iframeName  = 'uploadiframe' + new Date().getTime();
//     $iframe   = $('<iframe name="' + iframeName + '" style="display: none;"></iframe>');
// 	  $('body').append($iframe);
// 	  $form.attr('target', iframeName);

// 	  $iframe.one('load', function() {
// 	    var data = JSON.parse($iframe.contents().find('body' ).text());
// 	    $form
// 	      .removeClass('is-uploading')
// 	      .addClass(data.success == true ? 'is-success' : 'is-error')
// 	      .removeAttr('target');
// 	    if (!data.success) $errorMsg.text(data.error);
// 	    $form.removeAttr('target');
// 	    $iframe.remove();
//   });
//   }
//   // alert('submitted');
// })
// .on('drop', function(e) { // when drag & drop is supported
//   droppedFiles = e.originalEvent.dataTransfer.files;
//   $form.trigger('submit');
//   // alert('submitted');
// });

// // ...

// $input.on('change', function(e) { // when drag & drop is NOT supported
//   $form.trigger('submit');
// });


// var $input    = $form.find('input[type="file"]'),
//     $label    = $form.find('label'),
//     showFiles = function(files) {
//       $label.text(files.length > 1 ? ($input.attr('data-multiple-caption') || '').replace( '{count}', files.length ) : files[ 0 ].name);
//     };

// // ...

// .on('drop', function(e) {
//   droppedFiles = e.originalEvent.dataTransfer.files; // the files that were dropped
//   showFiles( droppedFiles );
// });

// //...

// $input.on('change', function(e) {
//   showFiles(e.target.files);
// });





















