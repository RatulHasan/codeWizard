$(document).ready(function() {
    console.log("Loaded!");
    $('body').bootstrapMaterialDesign();
});

$(document).ready(function() {
    $("#registration-form").on('submit',function (e) {
        e.preventDefault();

        var form_data = $("#registration-form").serialize();

        $.ajax({
          type: "POST",
          url: '/save-user-registration',
          data: form_data,
          success: function (responce) {
              console.log(responce);
          }
        });
    });

    $("#login-form").on('submit',function (e) {
        e.preventDefault();

        var form_data = $("#login-form").serialize();

        $.ajax({
          type: "POST",
          url: '/login-check',
          data: form_data,
          success: function (responce) {
              if (responce === 'error') {
                  $("#error").removeAttr("hidden")
              }else {
                  $("#success").removeAttr("hidden");
                  window.location.href = '/'
              }
          }
        });
    });

    $("#logout-btn").on('click',function (e) {
        e.preventDefault();

        $.ajax({
          type: "GET",
          url: '/logout',
          success: function (responce) {
              if (responce === 'success') {
                  window.location.href = '/login';
              }else {
                  alert("Something went wrong!")
              }
          }
        });
    });


    $("#post-activity").on('submit',function (e) {
        e.preventDefault();

        var form_data = $("#post-activity").serialize();
        $.ajax({
          type: "POST",
          url: '/save-post-activity',
          data: form_data,
          success: function (responce) {
              if (responce === 'error') {
                  $("#post-error").removeAttr("hidden")
              }else {
                  $("#post-success").removeAttr("hidden");
                  window.location.href = '/'
              }
              // console.log(responce)
          }
        });
    });

});