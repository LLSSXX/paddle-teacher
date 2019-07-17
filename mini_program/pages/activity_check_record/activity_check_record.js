Page({
  data: {
    date1: '请选择起始日期',
    time1: '时间',
    date2: '请选择截止日期',
    time2: '时间',
  },
  onLoad: function (options) {
    this.app = getApp()
    var colleges = wx.getStorageSync('colleges');
    var college = colleges[0]
    var that = this;
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_my/check_record/activity_check_record/activity_check_record_load',
      data: {
        college: JSON.stringify(college)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data.i.list)
        that.setData({
          information: res.data.i.list
        });
      }
    })
  },
  //页面展示时，触发动画
  onShow: function () {
    this.app.slideupshow(this, 'slide_up2', 400, 1)

    setTimeout(function () {
      this.app.slideupshow(this, 'slide_up2', 400, 1)
    }.bind(this), 50);
  },
  bindDateChange1(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date1: e.detail.value
    })
  },
  bindTimeChange1(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      time1: e.detail.value
    })
  },
  bindDateChange2(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      date2: e.detail.value
    })
  },
  bindTimeChange2(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      time2: e.detail.value
    })
  },
  search: function () {
    this.app = getApp()
    var colleges = wx.getStorageSync('colleges');
    var college = colleges[0]
    var that = this;
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_my/check_record/activity_check_record/activity_check_record_select',
      data: {
        college: JSON.stringify(college),
        begin_date: JSON.stringify(this.data.date1),
        begin_time: JSON.stringify(this.data.time1),
        end_date: JSON.stringify(this.data.date2),
        end_time: JSON.stringify(this.data.time2),
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data.i.list)
        that.setData({
          information: res.data.i.list
        });
      }
    })
  },
  button: function (e) {
    wx.navigateTo({
      url: '../activity_check_record_detail/activity_check_record_detail?sequence_number=' + e.currentTarget.dataset.sequence_number,
    })
  }
})