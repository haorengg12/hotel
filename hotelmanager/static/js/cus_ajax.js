$(document).ready(function()
{
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

});


