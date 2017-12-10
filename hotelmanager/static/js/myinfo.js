$(document).ready(function () {
   $("#update").click(function () {
        $("#security>div").toggle();
   });
   $("#ajax_update").click(function () {
      var pwd = $("#pwd").val();
      var cus_name = $("#_cus_name").val();
      var id_num = $("#_id_num").val();

      $.ajax({
			type:"post",
			url:"/update_myinfo",
			dataType:"json",
			data:{
                "pwd" : pwd,
                "cus_name":cus_name,
                "id_num":id_num
			},
			async:false,
			success:function(data){
				// $.each(data, function(index,element) {
                 //     $("#"+index).text(element);
                //
				// });
                window.location.href = "myinfo"
			},
			error:function(){
				alert("查询出错！");
			}
			});
      $("#security>div").toggle();
   });
});