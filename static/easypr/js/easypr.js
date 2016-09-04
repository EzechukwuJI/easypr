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
      } else {
        return true;
      }
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
    if ($('#check_bank_deposit').is(':checked') || $('#check_bank_transfer').is(':checked'))  {
      $('#pay-details').removeClass('hidden');
    } else {
      $('#pay-details').addClass('hidden');
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





















