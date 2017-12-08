$(document).ready(function()
{
    $("#search").click(function () {
       datein =  $("#in").val();
       dateout =  $("#out").val();
       if(datein==''||dateout=='')
       {
           alert("请选择日期！");
       }


    siglelow = $("#siglelow").prop("checked");
    siglemid = $("#siglemid").prop("checked");
    siglehigh = $("#siglehigh").prop("checked");
    doublelow = $("#doublelow").prop("checked");
    doublemid = $("#doublemid").prop("checked");
    doublehigh = $("#doublehigh").prop("checked");

    // console.log(siglelow)
    // console.log(siglehigh)

    $.ajax({
			type:"post",
			url:"/search_room",
			dataType:"json",
			data:{
                "datein" : datein,
                "dateout" : dateout ,
                "siglelow" : siglelow,
                "siglemid" : siglemid,
                "siglehigh" : siglehigh,
                "doublelow" : doublelow,
                "doublemid" : doublemid,
                "doublehigh" : doublehigh
			},
			async:false,
			success:function(data){
				$.each(data, function(index,element) {


				});
			},
			error:function(){
				alert("查询出错！");
			}

					});
    });
});


