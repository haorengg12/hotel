 $(document).ready(function(){
      $("#in").datepicker({

                  dateFormat:"yy/mm/dd",
                  showButtonPanel:true,
                    minDate:-0

              });
      $("#out").datepicker({

                    dateFormat:"yy/mm/dd",
                    showButtonPanel:true,
                    minDate:-0
              });
      $("#cart").click(function () {
            $("#sl").text(sl_num);
            $("#sm").text(sm_num);
            $("#sh").text(sh_num);
            $("#dl").text(dl_num);
            $("#dm").text(dm_num);
            $("#dh").text(dh_num);
            $("#slide").fadeToggle();
      });
      var sl_num = 0;
      var sm_num = 0;
      var sh_num = 0;
      var dl_num = 0;
      var dm_num = 0;
      var dh_num = 0;


      $("#room_num>div>input").click(function () {
          // console.log(width);
          var cart = $("#cartflag");
          cart.css({
              "right":"100%",
              "bottom":"100%"
          });
          cart.show();


          var right = $("#cart").css("right");
          var bottom = $("#cart").css("bottom");
          cart.animate({
            "right":right,
              "bottom":bottom
          });
          //cart.hide();
            num = $(this).prev().text();
            if(num>0){
                $(this).prev().text(--num);
                if($(this).prev().attr("id")=='siglelow_num')
                {
                    sl_num++;
                }
                else if($(this).prev().attr("id")=='siglemid_num')
                {
                    sm_num++;
                }
                else if($(this).prev().attr("id")=='siglehigh_num')
                {
                    sh_num++;
                }
                else if($(this).prev().attr("id")=='doublelow_num')
                {
                    dl_num++;
                }
                else if($(this).prev().attr("id")=='doublemid_num')
                {
                    dm_num++;
                }
                else if($(this).prev().attr("id")=='doublehigh_num')
                {
                    dh_num++;
                }





            }else{
                alert("房间数不够！")
            }

      });
      $("#submit").click(function () {
            var datein =  $("#in").val();
            var dateout =  $("#out").val();
            console.log(datein);
            var form = $('<form></form>');
            form.append($("#main > input"));
            form.attr('action','reserve');
            form.attr('method','post');
            form.attr('target','_self');
            $("body").append(form);
            var input1=$('<input type="text" name="sl"/>');
            input1.attr('value',sl_num);
            form.append(input1);
            var input2=$('<input type="text" name="sm"/>');
            input2.attr('value',sm_num);
            form.append(input2);
            var input3=$('<input type="text" name="sh"/>');
            input3.attr('value',sh_num);
            form.append(input3);
            var input4=$('<input type="text" name="dl"/>');
            input4.attr('value',dl_num);
            form.append(input4);
            var input5=$('<input type="text" name="dm"/>');
            input5.attr('value',dm_num);
            form.append(input5);
            var input6=$('<input type="text" name="dh"/>');
            input6.attr('value',dh_num);
            form.append(input6);
            var input7=$('<input type="text" name="datein"/>');
            input7.attr('value',datein);
            form.append(input7);
            var input8=$('<input type="text" name="dateout"/>');
            input8.attr('value',dateout);
            form.append(input8);

            form.submit();

      })

  });

