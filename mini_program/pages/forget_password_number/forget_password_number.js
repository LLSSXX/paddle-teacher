Page({
  data: {
    disabled: false,
    loading: false,
    username: '',
    usernames: []
  },

  // 获取用户名
  username: function(e) {
    this.setData({
      username: e.detail.value
    })
  },

  // 确定
  ensure: function(e) {
    if (this.data.username.length == 0) {
      this.setData({
        infoMess: '请填写用户名！',
      })

    } else {
      this.setData({
        disabled: !this.data.disabled,
        loading: !this.data.loading
      })
      var username = this.data.username
      this.data.usernames.push(username)
      try {
        // 同步接口立即写入
        wx.setStorageSync('usernames', this.data.usernames)
        console.log('写入value2成功')
      } catch (e) {
        console.log('写入value2发生错误')
      }
      wx.navigateTo({
        url: '../forget_password_answer/forget_password_answer',
      });
    }
  }
})