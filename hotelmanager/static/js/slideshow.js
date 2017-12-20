

var count = 1;
var img = ["", "img/1.jpg" ,"img/2.jpg","img/3.jpg","img/4.jpg","img/5.jpg"];
function change(){

    var select = $("#select");
    var img1 = $("#image1");
    var img2 = $("#image2");
    var img3 = $("#image3");
    var img4 = $("#image4");
	count++;
	if(count>4){
		count = 1;
	}
	if(count==1)
	{
		select.css("background","darkred");
		select.next().css("background","white");
		select.next().next().css("background","white");
		select.next().next().next().css("background","white");
		select.next().next().next().next().css("background","white");
		img1.css("display"," ");
		img2.css("display","none");
		img3.css("display","none");
		img4.css("display","none");

	}
	else if(count==2)
	{
		select.css("background","white");
		select.next().css("background","darkred");
		select.next().next().css("background","white");
		select.next().next().next().css("background","white");
		select.next().next().next().next().css("background","white");
		img2.css("display"," ");
		img1.css("display","none");
		img3.css("display","none");
		img4.css("display","none");
	}
	else if(count==3)
	{
		select.css("background","white");
		select.next().css("background","white");
		select.next().next().css("background","darkred");
		select.next().next().next().css("background","white");
		select.next().next().next().next().css("background","white");
		img3.css("display"," ");
		img2.css("display","none");
		img1.css("display","none");
		img4.css("display","none");
	}
	else if(count==4)
	{
		select.css("background","white");
		select.next().css("background","white");
		select.next().next().css("background","white");
		select.next().next().next().css("background","darkred");
		select.next().next().next().next().css("background","white");
		img4.css("display"," ");
		img2.css("display","none");
		img3.css("display","none");
		img1.css("display","none");
	}

}
$(document).ready(function(){
    var select = $("#img div");
    var img1 = $("#image1");
    var img2 = $("#image2");
    var img3 = $("#image3");
    var img4 = $("#image4");

	timer = setInterval("change()",3000);
	select.mouseenter(function(){
		count = $(this).html();
		$("#image").attr("src",img[count]);
		if(count==1)
	{
		select.css("background","darkred");
		select.next().css("background","white");
		select.next().next().css("background","white");
		select.next().next().next().css("background","white");
		select.next().next().next().next().css("background","white");
		img1.css("display"," ");
		img2.css("display","none");
		img3.css("display","none");
		img4.css("display","none");

	}
	else if(count==2)
	{
		select.css("background","white");
		select.next().css("background","darkred");
		select.next().next().css("background","white");
		select.next().next().next().css("background","white");
		select.next().next().next().next().css("background","white");
		img2.css("display"," ");
		img1.css("display","none");
		img3.css("display","none");
		img4.css("display","none");
	}
	else if(count==3)
	{
		select.css("background","white");
		select.next().css("background","white");
		select.next().next().css("background","darkred");
		select.next().next().next().css("background","white");
		select.next().next().next().next().css("background","white");
		img3.css("display"," ");
		img2.css("display","none");
		img1.css("display","none");
		img4.css("display","none");
	}
	else if(count==4)
	{
		select.css("background","white");
		select.next().css("background","white");
		select.next().next().css("background","white");
		select.next().next().next().css("background","darkred");
		select.next().next().next().next().css("background","white");
		img4.css("display"," ");
		img2.css("display","none");
		img3.css("display","none");
		img1.css("display","none");
	}
		clearInterval(timer);
	});

	select.mouseout(function(){
		timer = setInterval("change()",3000);
	});



});