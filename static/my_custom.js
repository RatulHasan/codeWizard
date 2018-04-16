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

        console.log(form_data);
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
});