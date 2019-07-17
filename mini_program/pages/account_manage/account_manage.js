Page({
  data:{
    disabled: false,
    loading: false
  },
  button: function(){
    this.setData({
      disabled: !this.data.disabled,
      loading: !this.data.loading
    })
    wx.removeStorageSync("usernames")
    wx.removeStorageSync("colleges")
    wx.removeStorageSync("identity_s")
    wx.reLaunch({
      url: '../login/login',
    })
  }
})