Page({
  school: function() {
    wx.navigateTo({
      url: '../apply_school_certificate/apply_school_certificate',
    })
  },
  classroom: function () {
    wx.navigateTo({
      url: '../apply_classroom/apply_classroom',
    })
  },
  activity: function () {
    wx.navigateTo({
      url: '../apply_activity/apply_activity',
    })
  }
})