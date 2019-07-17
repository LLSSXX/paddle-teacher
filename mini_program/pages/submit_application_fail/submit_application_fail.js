Page({
  data: {
    disabled: false,
    loading: false
  },
  ensure: function () {
    this.setData({
      disabled: !this.data.disabled,
      loading: !this.data.loading
    })
    wx.reLaunch({
      url: '../index/index',
    })
  }
})