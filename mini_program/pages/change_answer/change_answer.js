Page({
  data: {
    disabled: false,
    loading: false,
    question: '',
    answer: '',
    new_answer: '',
    ensure_new_answer: '',
    usernames: []
  },

  //获取问题
  onLoad: function (options) {
    var usernames = wx.getStorageSync('usernames');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var that = this
    wx.request({
      url: 'https://paddle-teacher.xyz/public_my/account_manage/change_answer/select_question',
      data: {
        username: JSON.stringify(username)
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (question) {
        that.setData({
          question: question.data
        });
      }
    })
  },

  // 获取答案
  answer: function (e) {
    this.setData({
      answer: e.detail.value
    })
  },

  // 获取新答案
  new_answer: function (e) {
    this.setData({
      new_answer: e.detail.value
    })
  },

  // 确认新答案
  ensure_new_answer: function (e) {
    this.setData({
      ensure_new_answer: e.detail.value
    })
  },

  // 确定
  ensure: function () {
    if (this.data.answer.length == 0 || this.data.new_answer.length == 0) {
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
      var that = this
      wx.request({
        url: 'https://paddle-teacher.xyz/public_my/account_manage/change_answer/submit_answer',
        data: {
          username: JSON.stringify(username),
          answer: JSON.stringify(this.data.answer),
          new_answer: JSON.stringify(this.data.new_answer),
          ensure_new_answer: JSON.stringify(this.data.ensure_new_answer)
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function (res) {
          console.log(res.data);
          if (res.data == "原答案错误！") {
            that.setData({
              infoMess: res.data
            });
          } else if (res.data == "两次输入的新答案不一致，请重新输入！") {
            that.setData({
              infoMess: res.data
            });
          }else {
            wx.reLaunch({
              url: '../change_answer_success/change_answer_success',
            });
          }
        }
      })
    }
  }
})