var util = require('../../utils/util');

Page({
  data: {
    date_time: '',
    usernames: [],
    disabled: false,
    loading: false
  },

  // 获取申请理由 
  application_reasonInput: function(e) {
    this.setData({
      application_reason: e.detail.value
    })
  },

  // 提交 
  submit: function(e) {
    this.setData({
      disabled: !this.data.disabled,
      loading: !this.data.loading
    })
    var TIME = util.formatTime(new Date())
    this.setData({
      date_time: TIME
    })
    var usernames = wx.getStorageSync('usernames');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var that = this;
    wx.request({
      url: 'https://paddle-teacher.xyz/student_index/apply_school_certificate/submit_school_certificate_application',
      data: {
        username: JSON.stringify(username),
        application_reason: JSON.stringify(this.data.application_reason),
        date_time: JSON.stringify(this.data.date_time)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(res) {
        console.log(res.data);
        if (res.data == "Pass") {
          wx.reLaunch({
            url: '../automatic_pass/automatic_pass',
          });
        } else if (res.data == "Undetermined") {
          wx.reLaunch({
            url: '../need_teacher_check/need_teacher_check',
          });
        }
        if (res.data == "Dispass") {
          wx.reLaunch({
            url: '../submit_application_fail/submit_application_fail',
          });
        }
      }
    })
  },

  preview: function(e) {
    var that = this;
    wx.navigateTo({
      url: '../preview/preview?application_reason=' + that.data.application_reason,
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
      }),

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
      }),

      this.app = getApp()
    var usernames = wx.getStorageSync('usernames');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    wx.request({
      url: 'https://paddle-teacher.xyz/student_index/apply_school_certificate/school_certificate_load',
      data: {
        username: JSON.stringify(username),
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(information) {
        that.setData({
          name: information.data.name,
          school_number: information.data.school_number,
          college: information.data.college,
          profession: information.data.profession
        })
      }
    })
  },

  //页面展示时，触发动画
  onShow: function() {
    this.app.slideupshow(this, 'slide_up2', 400, 1)

    setTimeout(function() {
      this.app.slideupshow(this, 'slide_up2', 400, 1)
    }.bind(this), 50);
  }
})