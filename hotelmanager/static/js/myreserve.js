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
                td.text(data[i]["check_id"]);
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
        $("#check_item>tbody").html("<tr><th>预约号</th><th>入住时间</th><th>离开时间</th><th>入住状态</th><th>房间号</th></tr>");
        $("#check_item").toggle();
        $("#my_reserve").toggle();
        $("#back").toggle();
    });
    var check_id;
    $(document).on("click","#check_item > tbody > tr",function(){
        check_id = $(this).children("td:eq(0)").text();
        $("#bg").show();
        $("#cancel").show();
    });
    $("#no").click(function () {
        $("#bg").hide();
        $("#cancel").hide();
    });
    $("#yes").click(function () {
        $.post("delete_check",{check_id:check_id},function (data) {
            alert("成功！");
            console.log(data);
        });
        $("#bg").hide();
        $("#cancel").hide();
    });
});