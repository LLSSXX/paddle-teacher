var app = getApp()
Page({
  data: {
    disabled: false,
    loading: false,
    username: '',
    password: '',
    usernames: [],
    colleges: [],
    identity_s: [],
    loading: false
  },

  // 获取输入账号 
  usernameInput: function(e) {
    this.setData({
      username: e.detail.value
    })
  },

  // 获取输入密码 
  passwordInput: function(e) {
    this.setData({
      password: e.detail.value
    })
  },

  setLoading(e) {
    this.setData({
      loading: !this.data.loading
    })
  },

  // 登录 
  login: function(e) {
    if (this.data.username.length == 0 || this.data.password.length == 0) {
      this.setData({
        infoMess: '用户名和密码不能为空！',
      })

    } else {
      this.setData({
        disabled: !this.data.disabled,
        loading: !this.data.loading
      })
      var that = this
      wx.request({
        url: 'https://paddle-teacher.xyz/public_login/login',
        data: {
          username: JSON.stringify(this.data.username),
            //将数据格式转为JSON
          password: JSON.stringify(this.data.password)
        },
        method: "POST",
        header: {
          'content-type': 'application/x-www-form-urlencoded',
          'chartset': 'utf-8'
        },
        success: function(res) {
          console.log(res.data);
          if (res.data == "用户名或密码错误!") {
            that.setData({
              infoMess: res.data
            });
          } else if (res.data == "需设置密保问题"){
            var username = that.data.username
            that.data.usernames.push(username)
            try {
              // 同步接口立即写入
              wx.setStorageSync('usernames', that.data.usernames)
              console.log('写入value2成功')
            } catch (e) {
              console.log('写入value2发生错误')
            }
            var identity = res.data
            that.data.identity_s.push(identity)
            try {
              // 同步接口立即写入
              wx.setStorageSync('identity_s', that.data.identity_s)
              console.log('写入value2成功')
            } catch (e) {
              console.log('写入value2发生错误')
            }
            wx.navigateTo({
              url: '../set_question/set_question',
            });
          } else if (res.data == "学生"){
            var username = that.data.username
            that.data.usernames.push(username)
            try {
              // 同步接口立即写入
              wx.setStorageSync('usernames', that.data.usernames)
              console.log('写入value2成功')
            } catch (e) {
              console.log('写入value2发生错误')
            }
            var identity = res.data
            that.data.identity_s.push(identity)
            try {
              // 同步接口立即写入
              wx.setStorageSync('identity_s', that.data.identity_s)
              console.log('写入value2成功')
            } catch (e) {
              console.log('写入value2发生错误')
            }
            wx.switchTab({
              url: '../index/index',
            });
          } else {
            var username = that.data.username
            that.data.usernames.push(username)
            try {
              // 同步接口立即写入
              wx.setStorageSync('usernames', that.data.usernames)
              console.log('写入value2成功')
            } catch (e) {
              console.log('写入value2发生错误')
            }
            var college = res.data.college
            that.data.colleges.push(college)
            try {
              // 同步接口立即写入
              wx.setStorageSync('colleges', that.data.colleges)
              console.log('写入value2成功')
            } catch (e) {
              console.log('写入value2发生错误')
            }
            var identity = res.data.identity
            that.data.identity_s.push(identity)
            try {
              // 同步接口立即写入
              wx.setStorageSync('identity_s', that.data.identity_s)
              console.log('写入value2成功')
            } catch (e) {
              console.log('写入value2发生错误')
            }
            wx.switchTab({
              url: '../teacher_index/teacher_index',
            });
          }
        }
      })
    }
  },

  //忘记密码
  forget_password: function() {
    wx.navigateTo({
      url: '../forget_password_number/forget_password_number',
    })
  }
})