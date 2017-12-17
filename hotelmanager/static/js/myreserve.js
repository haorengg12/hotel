$(document).ready(function () {

    $("#my_reserve > tbody > tr").click(function () {
        var book_id = $(this).children("#book_id").text();
        if(book_id=='')
            return;
        $.post("all_check",{book_id:book_id},function (data,status) {
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
        $("#check_item").toggle();
        $("#my_reserve").toggle();
        $("#back").toggle();
    });
    $("#back").click(function () {
        $("#check_item>tbody").html("<tr><th>订单号</th><th>入住时间</th><th>离开时间</th><th>入住状态</th><th>房间号</th></tr>");
        $("#check_item").toggle();
        $("#my_reserve").toggle();
        $("#back").toggle();
    });
});