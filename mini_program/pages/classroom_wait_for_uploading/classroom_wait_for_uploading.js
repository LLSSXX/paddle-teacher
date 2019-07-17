Page({
  data: {
    disabled: false,
    loading: false,
    information: [],
    colleges: []
  },

  onShow: function() {
    this.getCartList();
  },

  getCartList: function() {
    var colleges = wx.getStorageSync('colleges');
    var college = colleges[0]
    var that = this;
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_index/check_classroom/wait_upload_classroom',
      data: {
        college: JSON.stringify(college)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(res) {
        that.setData({
          information: res.data.i.list
        });
        if (res.data.i.list.length == 0) {
          wx.showModal({
            title: '提示',
            content: '无待上传记录',
            showCancel: false,
            confirmColor: '#F8931D'
          })
        }
      }
    })
  },

  button: function(e) {
    wx.navigateTo({
      url: '../classroom_wait_for_uploading_detail/classroom_wait_for_uploading_detail?sequence_number=' + e.currentTarget.dataset.sequence_number,
    })
  },
  button1: function (e) {
    this.setData({
      disabled: !this.data.disabled,
      loading: !this.data.loading
    })
    var colleges = wx.getStorageSync('colleges');
    var college = colleges[0]
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_index/check_classroom/wait_upload_classroom/wait_upload_classroom_upload',
      data: {
        college: JSON.stringify(college)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
    })
  },




  onLoad: function(options) {
    var that = this
    wx.login({
      success: function(data) {
        console.log(data.code, data)
        // 获取openid
        wx.request({
          url: 'https://api.weixin.qq.com/sns/jscode2session?appid=wxca9c32c5b47a5454&secret=edc8c4d71cdb4131d27728e305a8a1c9&js_code=' + data.code,
          header: {
            "Content-Type": "application/x-www-form-urlencoded"
          },
          method: "post",
          success: function(res) {
            console.log(res, "opind")
            that.setData({
              openid: res.data.openid,
              session_key: res.data.session_key,
            })
          }
        })

      }
    })

    // 获取access_token
    wx.request({
      url: 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxca9c32c5b47a5454&secret=edc8c4d71cdb4131d27728e305a8a1c9',
      method: "GET",
      success: function(res) {
        console.log(res, "res")
        console.log(res.data.access_token, "access_token")
        that.setData({
          access_token: res.data.access_token,
        })
      }
    })

  },

  // 点击执行方法
  form: function(e) {
    var that = this;
    var fId = e.detail.formId;
    // 网络请求
    var l = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=' + that.data.access_token;
    // 需要传的参数
    var d = {
      touser: that.data.openid, //用户的openid
      template_id: 'xEAzPA-RuKu5w7UqX6mwxXjXAkRGtdFBH5Lij4uEufc', //这个是申请的模板消息id，位置在微信公众平台/模板消息中添加并获取
      page: '/pages/teacher_index/teacher_index', //点击通知跳转的页面
      form_id: fId, //表单提交场景下，为 submit 事件带上的 formId

      //此处必须为data,只有人说value也可以,可能官方已经修复这个bug
      data: {
        "keyword1": {
          "value": "王晓丽"
        },
        "keyword2": {
          "value": "2019-03-22 20:54"
        },
        "keyword3": {
          "value": "教室"
        },
        "keyword4": {
          "value": "Y楼B区111"
        },
        "keyword5": {
          "value": "需要举办一场考研交流会"
        }
      }
    }
    wx.request({

      url: 'https://paddle-teacher.xyz/teacher_index/check_classroom/wait_upload_classroom/wait_upload_classroom_upload',
      data: {
        college: JSON.stringify(college)
      },
      method: "POST",
      success: function(res) {
        console.log(res, "push msg");
      },
      fail: function(err) {
        console.log(err, "push err");
      }
    });
  },
})