var util = require('../../utils/util');
Page({
  data: {
    disabled: false,
    loading: false,
    usernames: []
  },

  onLoad: function (options) {
    var that = this
    that.setData({
      application_reason: options.application_reason
    });
    var TIME = util.formatTime_date(new Date())
    this.setData({
      date_time: TIME
    })
    var usernames = wx.getStorageSync('usernames');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var that = this
    wx.request({
      url: 'https://paddle-teacher.xyz/student_index/apply_school_certificate/preview',
      data: {
        username: JSON.stringify(username),
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (information) {
        that.setData({
          name: information.data.name,
          school_number: information.data.school_number,
          college: information.data.college,
          profession: information.data.profession,
          grade: information.data.grade,
          date: that.data.date_time
        })
      }
    })
  },

  ensure: function () {
    this.setData({
      disabled: !this.data.disabled,
      loading: !this.data.loading
    })
    wx.navigateBack({
      delta: 1
    })
  }

})