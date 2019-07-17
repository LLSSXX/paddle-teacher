Page({
  data: {
    information: [],
    usernames: []
  },

  onShow: function() {
    this.getCartList();
  },

  getCartList: function() {
    var usernames = wx.getStorageSync('usernames');
    var username = usernames[0]
    var that = this;
    wx.request({
      url: 'https://paddle-teacher.xyz/student_my/application_record/school_certificate_application_record/school_certificate_application_record_load',
      data: {
        username: JSON.stringify(username),
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function(res) {
        that.setData({
          information: res.data.i.list
        });
      }
    })
  },

  button: function(e) {
    wx.navigateTo({
      url: '../school_certificate_application_record_detail/school_certificate_application_record_detail?sequence_number=' + e.currentTarget.dataset.sequence_number,
    })
  }
})