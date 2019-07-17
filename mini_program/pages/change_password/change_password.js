Page({
  data: {
    disabled: false,
    loading: false,
    old_password: '',
    new_password: '',
    ensure_new_password: '',
    usernames: []
  },

  // 获取旧密码 
  old_password: function(e) {
    this.setData({
      old_password: e.detail.value
    })
  },

  // 获取新密码 
  new_password: function(e) {
    this.setData({
      new_password: e.detail.value
    })
  },

  // 确定新密码 
  ensure_new_password: function(e) {
    this.setData({
      ensure_new_password: e.detail.value
    })
  },

  ensure: function() {
    if (this.data.old_password.length == 0 || this.data.new_password.length == 0 || this.data.ensure_new_password.length == 0) {
      this.setData({
        infoMess: '请填写完整！'
      })
    }else {
      this.setData({
        disabled: !this.data.disabled,
        loading: !this.data.loading
      })
      var usernames = wx.getStorageSync('usernames');
      // 然后存到本地数据区对应的数组中
      var username = usernames[0]
      var that = this
      wx.request({
        url: 'https://paddle-teacher.xyz/public_my/account_manage/change_password',
        data: {
          username: JSON.stringify(username),
          //将数据格式转为JSON
          old_password: JSON.stringify(this.data.old_password),
          new_password: JSON.stringify(this.data.new_password),
          ensure_new_password: JSON.stringify(this.data.ensure_new_password)
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function(res) {
          console.log(res.data);
          if (res.data == "原密码错误！") {
            that.setData({
              infoMess: res.data
            });
          } else if (res.data == "两次输入的新密码不一致，请重新输入！") {
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
  }
})