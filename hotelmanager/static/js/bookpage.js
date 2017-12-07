 $(document).ready(function(){
      $("#in").datepicker();
      $("#out").datepicker();
      $("#cart").click(function () {
            $("#slide").fadeToggle();
      });
      $("#room_num>div>input").click(function () {
          var left = $("#room_num>div>input").css("left");
          var top = $("#room_num>div>input").css("top");
          // console.log(width);
          var cart = $("#cartflag");
          cart.css({
              "left":left,
              "top":top
          });
          cart.show();

          $("#cart").css("top");
          cart.animate({
            "left":"473px",
              "top":"432px"
          });

      });
      $("#submit").click(function () {
            location.href = "reserve";
      })

  });

