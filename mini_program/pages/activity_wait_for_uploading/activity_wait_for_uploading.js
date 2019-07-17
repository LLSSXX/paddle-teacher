Page({
  data: {
    disabled: false,
    loading: false,
    information: [],
    colleges: []
  },

  onShow: function () {
    this.getCartList();
  },

  getCartList: function () {
    var colleges = wx.getStorageSync('colleges');
    var college = colleges[0]
    var that = this;
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_index/check_activity/wait_upload_activity',
      data: {
        college: JSON.stringify(college)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
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

  button: function (e) {
    wx.navigateTo({
      url: '../activity_wait_for_uploading_detail/activity_wait_for_uploading_detail?sequence_number=' + e.currentTarget.dataset.sequence_number,
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
      url: 'https://paddle-teacher.xyz/teacher_index/check_activity/wait_upload_activity/wait_upload_activity_upload',
      data: {
        college: JSON.stringify(college)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
    })

  }
})