Page({
  data: {
    disabled: false,
    loading: false,
    question: '',
    answer: '',
    usernames: []
  },

  //获取问题
  onLoad: function(options) {
    var usernames = wx.getStorageSync('usernames');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var that = this
    wx.request({
      url: 'https://paddle-teacher.xyz/public_login/forget_password/select_question',
      data: {
        username: JSON.stringify(username)
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(question) {
        that.setData({
          question: question.data
        });
      }
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
    if (this.data.answer.length == 0) {
      this.setData({
        infoMess: '请输入答案！',
      })

    } else {
      this.setData({
        disabled: !this.data.disabled,
        loading: !this.data.loading
      })
      var usernames = wx.getStorageSync('usernames');
      // 然后存到本地数据区对应的数组中
      var username = usernames[0];
      var that = this
      wx.request({
        url: 'https://paddle-teacher.xyz/public_login/forget_password/check_answer',
        data: {
          username: JSON.stringify(username),
          answer: JSON.stringify(this.data.answer)
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function(res) {
          console.log(res.data);
          if (res.data == "答案错误") {
            that.setData({
              infoMess: res.data
            });
          } else {
            wx.navigateTo({
              url: '../forget_password_new_password/forget_password_new_password',
            });
          }
        }
      })
    }
  }
})