$(document).ready(function () {
  $("#shut").click(function () {
    close_slide_bar();
  });
  $("#menu").click(function () {
    open_slide_bar();
  });
  $(".login-btn").click(function () {
    if (!$(this).hasClass("active")) {
      $(this).toggleClass("active");
      $(".register-btn").removeClass("active");
      $(".login-form-view").toggleClass("block");
      $(".register-form-view").toggleClass("block");
      check("login-radio", true);
    } else {
      // $(".register-btn").removeClass("active");
    }
  });
  $(".register-btn").click(function () {
    if (!$(this).hasClass("active")) {
      $(this).toggleClass("active");
      $(".login-btn").removeClass("active");
      $(".login-form-view").toggleClass("block");
      $(".register-form-view").toggleClass("block");
      check("register-radio", true);
    } else {
      // $(".login-btn").removeClass("active");
    }
  });
  $(".register-form-view .submit-btn").click(function () {
    password = $("#create_password").val();
    confirm_password = $("#confirm_password").val();
    if (password != "" && password != confirm_password) {
      alert("Error: Passwords do not match");
    } else {
      // alert("about to submit");
      $("#registeration_form_submit").submit();
    }
  });
  $(".exercise").click(function () {
    var day = $(this).find(".day").text();
    var exercise_name = $(this).find(".exercise-name").text();
    $(".day-input").val(day);
    $(".workout-input").val(exercise_name);
    $(".scheduler-hidden-form").submit();
  });
  var counter = 0;

  $("#exercise-add").click(function () {
    $("disappear").css("display", "none");
    var con = $(".exercise-form");
    add_exercise_input(".exercise-form", ++counter, "exercise");
    add_exercise_input(".exercise-form", counter, "reps");
    add_exercise_input(".exercise-form", counter, "sets");
    $("#count").val(counter);
    var br = $("<br>");
    con.append(br);
  });
});
function close_slide_bar() {
  $(".sidebar").css("left", "-300px");
  $("#menu").css("opacity", "1");
}
function open_slide_bar() {
  $(".sidebar").css("left", "0px");
  $("#menu").css("opacity", "0");
}
function check(element, boolean) {
  document.getElementById(element).checked = true;
}
function add_exercise_input(container, counter, name) {
  var con = $(container);
  var exercise_label = $("<label>")
    .attr({
      for: name + counter,
    })
    .text(name + counter + ":");
  var new_exercise = $("<input>").attr({
    type: "text",
    name: name + counter,
    id: name + counter,
  });
  con.append(exercise_label);
  con.append(new_exercise);
}
