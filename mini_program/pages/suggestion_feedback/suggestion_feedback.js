var util = require('../../utils/util');

var app = getApp()
Page({
  data: {
    disabled: false,
    loading: false,
    suggestion: '',
    phone_number: '',
    date_time: ''
  },

  // 获取建议 
  suggestionInput: function(e) {
    this.setData({
      suggestion: e.detail.value
    })
  },

  // 获取联系电话
  phone_numberInput: function(e) {
    this.setData({
      phone_number: e.detail.value
    })
  },

  //获取日期和时间
  onLoad: function (options) {
    var TIME = util.formatTime(new Date())
    this.setData({
      date_time: TIME
    })
  },

  // 提交
  submit: function() {
    if (this.data.suggestion.length == 0) {
      this.setData({
        infoMess: '请填写意见或建议！',
      })

    } else {
      this.setData({
        disabled: !this.data.disabled,
        loading: !this.data.loading
      })
      var that = this
      wx.request({
        url: 'https://paddle-teacher.xyz/public_my/suggestion_feedback/submit_suggestion_feedback',
        data: {
          suggestion: JSON.stringify(this.data.suggestion),
          //将数据格式转为JSON
          phone_number: JSON.stringify(this.data.phone_number),
          date_time: JSON.stringify(this.data.date_time)
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function(res) {
          console.log(res.data);
          wx.reLaunch({
            url: '../suggestion_feedback_sunbmit_success/suggestion_feedback_sunbmit_success',
          });
        }
      })
    }
  }
})