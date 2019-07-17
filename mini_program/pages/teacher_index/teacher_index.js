Page({
  school: function() {
    wx.navigateTo({
      url: '../check_school_certificate/check_school_certificate',
    })
  },

  classroom: function () {
    wx.navigateTo({
      url: '../check_classroom/check_classroom',
    })
  },

  action: function () {
    wx.navigateTo({
      url: '../check_action/check_action',
    })
  },


  my: function(){
    wx.redirectTo({
      url: '../teacher_my/teacher_my',
    })
  }
})