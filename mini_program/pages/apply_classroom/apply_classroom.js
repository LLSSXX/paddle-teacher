var util = require('../../utils/util.js');

Page({
  data: {
    time1: "请选择",
    time2: "请选择",
    date_time: '',
    usernames: [],
    date: '请选择日期',

    multiArray: [
      ['请选择教室', '博理楼', '劝学楼'],
      [''],
      ['']
    ],
    objectMultiArray: [
      [{
          id: 0,
          name: '请选择教学楼'
        },
        {
          id: 1,
          name: '博理楼'
        },
        {
          id: 2,
          name: '劝学楼'
        }
      ]
    ],
    multiIndex: [0, 0, 0],
  },
  onLoad: function() {
    var TIME = util.formatDate(new Date())
    this.setData({
      date_time: TIME
    })
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
  bindMultiPickerChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      multiIndex: e.detail.value
    })
  },
  bindMultiPickerColumnChange(e) {
    console.log('修改的列为', e.detail.column, '，值为', e.detail.value)
    const data = {
      multiArray: this.data.multiArray,
      multiIndex: this.data.multiIndex
    }
    data.multiIndex[e.detail.column] = e.detail.value
    switch (e.detail.column) {
      case 0:
        switch (data.multiIndex[0]) {
          case 0:
            data.multiArray[1] = ['']
            data.multiArray[2] = ['']
            break
          case 1:
            data.multiArray[1] = ['A区', 'B区', 'C区', 'D区']
            data.multiArray[2] = ['101', '102', '103', '104']
            break
          case 2:
            data.multiArray[1] = ['A区', 'B区', 'C区']
            data.multiArray[2] = ['101', '102', '103', '104']
            break
        }
        data.multiIndex[1] = 0
        data.multiIndex[2] = 0
        break
      case 1:
        switch (data.multiIndex[0]) {
          case 0:
            switch (data.multiIndex[1]) {
              case 0:
                data.multiArray[2] = ['门牌号']
                break
            }
            break
          case 1:
            switch (data.multiIndex[1]) {
              case 0:
                data.multiArray[2] = []
                break
              case 1:
                data.multiArray[2] = ['111', '222']
                break
              case 2:
                data.multiArray[2] = ['210', '211', '212']
                break
              case 3:
                data.multiArray[2] = ['220', '221', '222']
                break
            }
          case 2:
            switch (data.multiIndex[1]) {
              case 0:
                data.multiArray[2] = ['101', '102', '103']
                break
              case 1:
                data.multiArray[2] = ['111', '222']
                break
              case 2:
                data.multiArray[2] = ['210', '211', '212']
                break
            }
            break
        }
        data.multiIndex[2] = 0
        break
    }
    console.log(data.multiIndex)
    this.setData(data)
  },

  // 获取申请用途 
  application_reasonInput: function(e) {
    this.setData({
      application_reason: e.detail.value
    })
  },

  // 提交 
  submit: function() {
      var TIME = util.formatTime(new Date())
      this.setData({
        date_time: TIME
      })
      var usernames = wx.getStorageSync('usernames');
      // 然后存到本地数据区对应的数组中
      var username = usernames[0]
      var that = this
      wx.request({
        url: 'https://paddle-teacher.xyz/student_index/apply_classroom/submit_classroom_application',
        data: {
          username: JSON.stringify(username),
          date_time: JSON.stringify(this.data.date_time),
          date: JSON.stringify(this.data.date),
          begin_time: JSON.stringify(this.data.time1),
          end_time: JSON.stringify(this.data.time2),
          classroom: JSON.stringify(this.data.multiIndex),
          purpose: JSON.stringify(this.data.application_reason),
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function(res) {
          console.log(res.data);
          if (res.data == "已有人申请") {
            wx.showModal({
              title: '提示',
              content:'此教室和时间段已有人申请' ,
              showCancel:false,
              confirmColor: '#F8931D'
            })
          }
          else{
            wx.reLaunch({
              url: '../need_teacher_check/need_teacher_check',
            });
          }
        }
      })
    
  },

  onLoad: function(options) {
    this.app = getApp()
  },
  //页面展示时，触发动画
  onShow: function() {
    this.app.slideupshow(this, 'slide_up2', 370, 1)

    setTimeout(function() {
      this.app.slideupshow(this, 'slide_up2', 370, 1)
    }.bind(this), 10);
  },

})