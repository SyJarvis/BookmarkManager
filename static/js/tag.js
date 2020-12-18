;
var tag_list_ops = {
  init:function () {
      this.eventBind()

  },
    eventBind:function(){
      var that = this;
      // var str = document.cookie.split(';')[0];
      // var csrf = str.split('=')[1];
      //console.log(csrf)
      $(".remove").click(function () {
          that.ops("remove", $(this).attr('data'));
      });
    },

    ops:function (act, id) {

        var callback = {
            'ok':function () {
                $.ajax({
                    url:common_ops.buildUrl("/tag/delete"),
                    type:'POST',
                    data:{
                        act:act,
                        id:id,
                    },
                    dataType:'json',
                    success:function (res) {
                        var callback = null;
                        if (res.code == 200){
                            callback = function () {
                                window.location.href = window.location.href;
                            }
                        }
                        common_ops.alert(res.msg, callback)
                    }
                });
            },
            'cancel':null
        };
        common_ops.confirm((act == "remove" ? "确定删除":"确定恢复"), callback);
    }
};

$(document).ready(function () {
    tag_list_ops.init()
});