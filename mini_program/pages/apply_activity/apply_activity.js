var util = require('../../utils/util');

Page({
  data: {
    date_time: '',
    usernames: [],
    date: '请选择日期',
    time1: "请选择",
    time2: "请选择",
    array: ['请选择活动地点', '图书馆', '时间广场', '风雨操场'],
    objectArray: [
      {
        id: 0,
        name: '请选择活动地点'
      },
      {
        id: 1,
        name: '图书馆'
      },
      {
        id: 2,
        name: '时间广场'
      },
      {
        id: 3,
        name: '风雨操场'
      }
    ],
    index: 0,
  },
  bindDateChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date: e.detail.value
    })
  },
  bindTimeChange(e) {
    let that = this;
    console.log(e.detail.value)
    that.setData({
      time1: e.detail.value,
    })
  },
  bindTimeChange2(e) {
    let that = this;
    console.log(e.detail.value)
    that.setData({
      time2: e.detail.value,
    })
  },
  bindPickerChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index: e.detail.value
    })
  },
 

  // 获取申请理由 
  application_reasonInput: function (e) {
    this.setData({
      application_reason: e.detail.value
    })
  },

 
  // 提交 
  submit: function () {
    var TIME = util.formatTime(new Date())
    this.setData({
      date_time: TIME
    })
    var usernames = wx.getStorageSync('usernames');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var that = this
    wx.request({
      url: 'https://paddle-teacher.xyz/student_index/apply_activity/submit_activity_application',
      data: {
        username: JSON.stringify(username),
        date_time: JSON.stringify(this.data.date_time),
        date: JSON.stringify(this.data.date),
        begin_time: JSON.stringify(this.data.time1),
        end_time: JSON.stringify(this.data.time2),
        area: JSON.stringify(this.data.index),
        purpose: JSON.stringify(this.data.application_reason),
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data);
        if (res.data == "已有人申请") {
          wx.showModal({
            title: '提示',
            content: '此地点和时间段已有人申请',
            showCancel: false,
            confirmColor: '#F8931D'
          })
        }
        else {
          wx.reLaunch({
            url: '../need_teacher_check/need_teacher_check',
          });
        }
      }
    })

  },


  onLoad: function (options) {
    this.app = getApp()
  },
  //页面展示时，触发动画
  onShow: function () {
    this.app.slideupshow(this, 'slide_up2', 400, 1)

    setTimeout(function () {
      this.app.slideupshow(this, 'slide_up2', 400, 1)
    }.bind(this), 10);
  }
})