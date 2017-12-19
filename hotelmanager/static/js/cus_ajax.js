$(document).ready(function()
{
    var bg_width = $("#customer").css("width");
    var bg_height = $("#customer").css("height");
    console.log(bg_width);
    $("#customer>#bg,#reserve>#bg,#room>#bg").css({
        "width":bg_width,
        "height":bg_height
    });

    $("#mananger_cus").click(function () {
        $("#customer").show();
        $("#reserve").hide();
        $("#room").hide();
    });
        $("#mananger_res").click(function () {
        $("#customer").hide();
        $("#reserve").show();
        $("#room").hide();
    });
        $("#mananger_room").click(function () {
        $("#customer").hide();
        $("#reserve").hide();
        $("#room").show();
    });

    $("#start_name").click(function () {
        $("#cus").show();
        $("#info").hide();
        var name = $("#name").val();
        $.post("cus_search",{name:name,flag:"name"},function (data,status) {
            // console.log(data)
            $("#cus_item").html("<tr><th>id</th><th>昵称</th><th>电话</th></tr>");
            var num = data[0];
            if(num==0)
            {
                $("#cus_item").html("<h2>查询无果！</h2>")
            }
            for(var i = 1;i<=num;i++)
            {
                var tr = $("<tr></tr>");

                var td = $("<td></td>");
                td.attr("id","cus_id");
                td.text(data[i]["id"]);
                tr.append(td);
                td = $("<td></td>");
                td.attr("id","name");
                td.text(data[i]["name"]);
                tr.append(td);
                td = $("<td></td>");
                td.attr("id","phone");
                td.text(data[i]["phone"]);
                tr.append(td);
                $("#cus_item").append(tr);
            }

        });


    });

$("#start_phone").click(function () {
        $("#cus").show();
        $("#info").hide();
        var phone = $("#phone").val();
        $.post("cus_search",{phone:phone,flag:"phone"},function (data,status) {
            // console.log(data)
            $("#cus_item").html("<tr><th>id</th><th>昵称</th><th>电话</th></tr>");
            var num = data[0];
            if(num==0)
            {
                $("#cus_item").html("<h2>查询无果！</h2>")
            }
            for(var i = 1;i<=num;i++)
            {
                var tr = $("<tr></tr>");

                var td = $("<td></td>");
                td.attr("id","cus_id");
                td.text(data[i]["id"]);
                tr.append(td);
                td = $("<td></td>");
                td.attr("id","name");
                td.text(data[i]["name"]);
                tr.append(td);
                td = $("<td></td>");
                td.attr("id","phone");
                td.text(data[i]["phone"]);
                tr.append(td);

                $("#cus_item").append(tr);
            }

        });

    });
    $(document).on("click","#cus_item>tbody>tr",function(){
        var cus_id = $(this).children("#cus_id").text();
        $("#id").text(cus_id);
        $("#cus_name").text($(this).children("#name").text());
        $("#cus_phone").text($(this).children("#phone").text());
        $("#info").toggle();
        $("#cus").toggle();


        $.post("all_reserve",{cus_id:cus_id},function (data,status) {
             $("#res_item").html("<tr><th>订单号</th><th>订单日期</th><th>订单价格</th><th>订购数量</th></tr>");
            // console.log(data);
            var num = data[0];
            if(num==0)
            {
                $("#res_item").html("<h2>查询无果！</h2>")
            }
            for(var i = 1;i<=num;i++)
            {
                var tr = $("<tr></tr>");

                var td = $("<td></td>");
                 td.attr("id","book_id");
                td.text(data[i]["book_id"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["book_time"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["book_price"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["book_num"]);
                tr.append(td);
                $("#res_item").append(tr);
            }

        });
    });
    $(document).on("click","#res_item>tbody>tr",function(){
        var book_id = $(this).children("#book_id").text();
        // console.log(book_id);
        if(book_id=='')
            return;
        $.post("all_check",{book_id:book_id},function (data,status) {
            $("#check_item>tbody").html("<tr><th>订单号</th><th>入住时间</th><th>离开时间</th><th>入住状态</th><th>房间号</th></tr>");
            var num = data[0];
            for(var i = 1;i<=num;i++)
            {
                var tr = $("<tr></tr>");

                var td = $("<td></td>");
                td.text(book_id);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["check_time"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["leave_time"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["check_statu"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["room_id"]);
                tr.append(td);

                $("#check_item>tbody").append(tr);
            }

        });
        $("#customer").hide();
        $("#reserve").show();
        $("#res_table").hide();
        $("#check_table").show();
    });
$(document).on("click","#reserve_item>tbody>tr",function(){
        var book_id = $(this).children("#book_id").text();
        // console.log(book_id);
        if(book_id=='')
            return;
        $.post("all_check",{book_id:book_id},function (data,status) {
            $("#check_item>tbody").html("<tr><th>订单号</th><th>入住时间</th><th>离开时间</th><th>入住状态</th><th>房间号</th></tr>");
            var num = data[0];
            for(var i = 1;i<=num;i++)
            {
                var tr = $("<tr></tr>");

                var td = $("<td></td>");
                td.text(book_id);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["check_time"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["leave_time"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["check_statu"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["room_id"]);
                tr.append(td);

                $("#check_item>tbody").append(tr);
            }

        });
        $("#customer").hide();
        $("#reserve").show();
        $("#res_table").hide();
        $("#check_table").show();
    });
        $(document).on("click","#start_res_phone",function(){
            $("#res_table").show();
            $("#check_table").hide();
            var phone = $("#res_phone").val();
            $.post("res_reserve",{phone:phone,flag:"phone"},function (data,status) {
            // console.log(data)
            $("#reserve_item").html("<tr><th>订单号</th><th>订单日期</th><th>订单价格</th><th>订购数量</th></tr>");
            var num = data[0];
            if(num==0)
            {
                $("#reserve_item").html("<h2>查询无果！</h2>")
            }
            for(var i = 1;i<=num;i++)
            {
                var tr = $("<tr></tr>");

                var td = $("<td></td>");
                td.attr("id","book_id");
                td.text(data[i]["book_id"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["book_time"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["book_price"]);
                tr.append(td);
                td = $("<td></td>");
                td.text(data[i]["book_num"]);
                tr.append(td);
                $("#reserve_item").append(tr);
            }

            });
        });
        $(document).on("click","#check_item > tbody > tr",function(){
                // console.log($("#check_item > tbody > tr").children("td:eq(1)").text())

                var it = $(this);
                var check_id = it.children("td:eq(0)").text();
                // console.log(check_id);
                $("#check_id").text(check_id);
                var ctime = it.children("td:eq(1)").text();
                    // console.log(ctime);
                var ltime = it.children("td:eq(2)").text();
                var room_id = it.children("td:eq(4)").text();
                console.log(room_id);
                $("#f_ctime").val(ctime);
                $("#f_ltime").val(ltime);
                $("#f_room_id").val(room_id);
                $("#float").show();
                $("#blur").show();

        });
        $("#no").click(function () {
            $("#float").hide();
            $("#blur").hide();
        })
        $("#yes").click(function () {
            var name = $("#f_name").val();
            var phone = $("#f_phone").val();
            var idnum = $("#f_idnum").val();
            var ctime = $("#f_ctime").val();
            var ltime = $("#f_ltime").val();
            var room_id = $("#f_room_id").val();
            var statu = $("#f_statu").val();
            var check_id = $("#check_id").text();

            $.post("insert_check",{
                check_id:check_id,
                name:name,
                phone:phone,
                idnum:idnum,
                ctime:ctime,
                ltime:ltime,
                room_id:room_id,
                statu:statu
            },function (data) {
                console.log(data);
                if(data["info"]=="0")
                {
                    alert("信息填写有误");
                }
                else
                {
                    var name = $("#f_name").val('');
                    var phone = $("#f_phone").val('');
                    var idnum = $("#f_idnum").val('');
                    var ctime = $("#f_ctime").val('');
                    var ltime = $("#f_ltime").val('');
                    var room_id = $("#f_room_id").val('');
                    var statu = $("#f_statu").val('');
                    var check_id = $("#check_id").text('');
                    $("#float").hide();
                    $("#blur").hide();
                }
            })
        });

        $("#get_room_by_id").click(function () {
            var room_id = $("#room_id").val();
            $.post("get_room_by_id",{room_id:room_id},function (data) {
                // console.log(data);
                if(data[0]==0)
                {
                    alert("请输入房间号！");
                }
                else
                {
                   var num = data[1];
                    var index = ["room_id","name","phone","ctime","ltime","check_id","book_id","statu","level","price"];
                    console.log(data[2]["room_id"]);
                    $("#room_item > tbody").html("<tr><th>房间号</th><th>姓名</th><th>电话号</th><th>入住时间</th><th>离开时间</th><th>入住订单号</th><th>订单号</th><th>入住状态</th><th>房间类型</th><th>房间价格</th></tr>");
                    for(var i = 2;i<num;i++)
                    {
                        var tr = $("<tr></tr>");
                        for(var j=0;j<10;j++)
                        {
                            var td = $("<td></td>");
                            td.text(data[i][index[j]]);
                            tr.append(td);
                        }

                        $("#room_item > tbody").append(tr);
                    }
                }
            })
        });
        $("#start").datepicker({

                  dateFormat:"yy-mm-dd",
                  showButtonPanel:true,

              });
        $("#end").datepicker({

                  dateFormat:"yy-mm-dd",
                  showButtonPanel:true,

              });
        $("#get_room").click(function () {
            var datein = $("#start").val();
            var dateout = $("#end").val();
            $.post("get_room_by_date",{datein:datein,dateout:dateout},function (data) {
                console.log(data);
                if(data[0]==0)
                {
                    alert("请输入房间号！");
                }
                else
                {
                   var num = data[1];
                    var index = ["room_id","name","phone","ctime","ltime","check_id","book_id","statu","level","price"];
                    $("#room_item > tbody").html("<tr><th>房间号</th><th>姓名</th><th>电话号</th><th>入住时间</th><th>离开时间</th><th>入住订单号</th><th>订单号</th><th>入住状态</th><th>房间类型</th><th>房间价格</th></tr>");
                    for(var i = 2;i<num;i++)
                    {
                        var tr = $("<tr></tr>");
                        for(var j=0;j<10;j++)
                        {
                            var td = $("<td></td>");
                            td.text(data[i][index[j]]);
                            tr.append(td);
                        }

                        $("#room_item > tbody").append(tr);
                    }
                }
            })

        });
        $("#update_room").click(function () {
            $("#room_update").show();
        });
        $("#cancel").click(function () {
            $("#room_update").hide();
        });
        $("#add").click(function () {
           var room_id = $("#add_room_id").val();
           var room_level = $("#add_room_level").val();

           $.post("add_room",{room_id:room_id,room_level:room_level},function (data) {
               // console.log(data);
               if(data["info"]==0)
               {
                   alert("请输入三位房间号");
               }
               else
               {
                   alert("成功！")
               }
           })

        });
        $("#delete").click(function () {
           var room_id = $("#add_room_id").val();

           $.post("delete_room",{room_id:room_id},function (data) {
               // console.log(data);
               if(data["info"]==0)
               {
                   alert("房间不存在!");
               }
               else
               {
                   alert("成功！")
               }
           })

        });
});


