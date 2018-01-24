
function mysubmit() {
    let text = $('.editormd-markdown-textarea').val()
    let name = document.getElementById("name").value;
    let mail = document.getElementById("mail").value;
    let a_id = $('#a_id').val()
    // alert(form)

    let reg = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/
    if(!reg.test(mail)){
        alert('检查邮箱地址')
        return
    }

    let data = {
        text,name,mail,a_id
    }
    $.post('/index/comment', data, function(data){
    console.log(data);
    if (data === '0'){
        window.location.reload();
    }else {
        alert('表单不能留空')
    }
});
}
