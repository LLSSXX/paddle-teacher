Page({
  data: {
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
      url: 'https://paddle-teacher.xyz/teacher_index/check_classroom/wait_check_classroom',
      data: {
        college: JSON.stringify(college)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data);
        that.setData({
          information: res.data.i.list
        });
        if (res.data.i.list.length==0) {
          wx.showModal({
            title: '提示',
            content: '无待审核记录',
            showCancel: false,
            confirmColor: '#F8931D'
          })
        }
      }
    })
  },

  button: function (e) {
    wx.navigateTo({
      url: '../classroom_wait_for_audit_detail/classroom_wait_for_audit_detail?sequence_number=' + e.currentTarget.dataset.sequence_number,
    })
  }
})