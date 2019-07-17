Page({
  data: {
    disabled: false,
    loading: false,
    array: ['请选择问题', '你最喜欢的颜色', '你最喜欢的动物', '你最喜欢的运动'],
    objectArray: [{
        id: 0,
        name: '请选择问题'
      },
      {
        id: 1,
        name: '你最喜欢的颜色'
      },
      {
        id: 2,
        name: '你最喜欢的动物'
      },
      {
        id: 3,
        name: '你最喜欢的运动'
      }
    ],
    choose_question: 0,
    answer: '',
    usernames: []
  },

  //获取问题
  question:function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      choose_question: e.detail.value
    })
  },

  // 获取答案
  answer: function(e) {
    this.setData({
      answer: e.detail.value
    })
  },

  // 确定
  ensure: function() {
    if (this.data.choose_question == 0 || this.data.answer.length == 0) {
      this.setData({
        infoMess: '请填写完整！',
      })

    } else {
      this.setData({
        disabled: !this.data.disabled,
        loading: !this.data.loading
      })
      var usernames = wx.getStorageSync('usernames');
      // 然后存到本地数据区对应的数组中
      var username = usernames[0];
      var identity_s = wx.getStorageSync('identity_s');
      // 然后存到本地数据区对应的数组中
      var identity = identity_s[0];
      var that = this
      wx.request({
        url: 'https://paddle-teacher.xyz/public_login/first_login_set_question',
        data: {
          username: JSON.stringify(username),
          choose_question: JSON.stringify(this.data.choose_question),
          answer: JSON.stringify(this.data.answer)
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function(res) {
          console.log(res.data);
          if (res.data == "学生"){
            wx.reLaunch({
              url: '../index/index',
            });
          }
          else{
            wx.reLaunch({
              url: '../teacher_index/teacher_index',
            });
          }
        }
      })
    }
  }
})