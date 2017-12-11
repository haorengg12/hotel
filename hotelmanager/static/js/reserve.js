$(document).ready(function() {
            var num = 0;
            var all_price = 0;
            for(var i = 1;i<=6;i++)
             {
                var p = $("td[id=price"+i+"]").text();

                p = parseFloat(p);

                var price_num = parseFloat($("td[id=price"+i+"]").prev().text());
                num+=price_num;
                var ps = p * price_num;
                $("td[id=price"+i+"]").text(ps);
                all_price += ps;
            }
            $("#r_num").html(num);
            $("#all_price").html(all_price);

            $("#book_reserve tr").mouseenter(function() {
              $(this).css("color","black");
              // alert();
            });
            $("#book_reserve tr").mouseout(function() {
              $(this).css("color","whitesmoke");
            });

            $("#pay").click(function() {
                var form = $('<form></form>');
                form.append($("#main > input"));
                form.attr('action','check_reserve');
                form.attr('method','post');
                form.attr('target','_self');
                $("body").append(form);
                var price = $("#all_price > span").text();
                var input1 = $('<input type="text" name="price" />');
                input1.attr("value",price);
                form.append(input1);
                var num = $("#r_num > span").text();
                var input2 = $('<input type="text" name="num"/>');
                input2.attr("value",num);
                form.append(input2);

                var datein = $("#in").val();
                var input3 = $('<input type="text" name="datein"/>');
                input3.attr("value",datein);
                form.append(input3);
                var dateout = $("#out").val();
                var input4 = $('<input type="text" name="dateout"/>');
                input4.attr("value",dateout);
                form.append(input4);
                var idnum = $("#id_num").val();
                var input5 = $('<input type="text" name="id_num"/>');
                input5.attr("value",idnum);
                form.append(input5);
                var book_phone = $("#book_phone").val();
                var input6 = $('<input type="text" name="book_phone"/>');
                input6.attr("value",book_phone);
                form.append(input6);

                for(var i =1;i<=6;i++)
                {
                    var input = $('<input type="text" name="lv'+i+'"/>');
                    var lv = $("td[id=price"+i+"]").prev().text();
                    input.attr("value",lv);
                    form.append(input);
                }

                form.submit();

            })
        });