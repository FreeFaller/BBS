// //必填项
// $("form :input.required").each(function(){
// 	var $required = $("<strong class = 'high'>*</strong>");
// 	$(this).parent().append($required);
// });
//表单验证
$('form :input').blur(function(){
	var $parent = $(this).parent();
	//验证用户名
	if ($(this).is('#nickName')) {
		if (this.value == "" || this.value.length < 2) {
			var errorMsg = '请输入至少2位的昵称';
			$parent.append('<span class = "formtips onError">'+errorMsg+'</span>');
		}else{
			var okMsg = '输入正确';
			$parent.append('<span class = "formtips onSuccess">'+okMsg+'</span>');
		}
	}
	//邮箱验证
	if ($(this).is('#email')) {
		if (this.value ==""||(this.value!="" && !/.+@.+\.[a-zA-Z] {2,4}$/.test(this.value))) {
			var errorMsg = "请输入正确的Email地址";
			$parent.append('<span class = "formtips onError">'+errorMsg+'</span>');
		}else{
			var okMsg = '输入正确';
			$parent.append('<span class = "formtips onSuccess"'+okMsg+'</span>');
		}
	}
});
// //避免错误提示堆积
// $('form :input').blur(function(){
// 	var $parent = $(this).parent();
// 	$parent.find(".formtips").remove();
// });
//提交
$('#send').click(function(){
	$("form .required:input").trigger('blur');
	var numError = $('form .onError').length;
	if(numError){
		return false;
	}
	alert("注册成功");
});
//重置
 $('#res').click(function(){
        $(".formtips").remove();      
 });