Page({
  data: {
    disabled: false,
    loading: false,
    new_password: '',
    ensure_new_password: '',
    usernames: []
  },

  // 获取新密码 
  new_password: function (e) {
    this.setData({
      new_password: e.detail.value
    })
  },

  // 确定新密码 
  ensure_new_password: function (e) {
    this.setData({
      ensure_new_password: e.detail.value
    })
  },

  ensure: function () {
    this.setData({
      disabled: !this.data.disabled,
      loading: !this.data.loading
    })
    var usernames = wx.getStorageSync('usernames');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var that = this
    wx.request({
      url: 'https://paddle-teacher.xyz/public_login/forget_password/set_new_password',
      data: {
        username: JSON.stringify(username),
        new_password: JSON.stringify(this.data.new_password),
        ensure_new_password: JSON.stringify(this.data.ensure_new_password)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data);
        if (res.data == "两次输入的新密码不一致，请重新输入！") {
          that.setData({
            infoMess: res.data
          });
        } else {
          wx.reLaunch({
            url: '../change_password_success/change_password_success',
          });
        }
      }
    })
  }
})