Page({
  data: {
    name: '',
    school_number: '',
    choose_college: '',
    application_reason: '',
    submit_time: '',
    sequence_numbers: [],
    disabled: false
  },
  onLoad: function (options) {
    var that = this
    that.setData({
      sequence_number: options.sequence_number
    });
    var sequence_number = options.sequence_number
    this.data.sequence_numbers.push(sequence_number)
    try {
      // 同步接口立即写入
      wx.setStorageSync('sequence_numbers', this.data.sequence_numbers)
      console.log('写入value2成功')
    } catch (e) {
      console.log('写入value2发生错误')
    }
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_index/check_school_certificate/wait_upload_school_certificate/wait_upload_school_certificate_detail',
      data: {
        sequence_number: JSON.stringify(that.data.sequence_number),
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      method: "POST",
      success: function (information) {
        that.setData({
          name: information.data.name,
          school_number: information.data.school_number,
          choose_college: information.data.choose_college,
          profession: information.data.profession,
          application_reason: information.data.application_reason,
          submit_time: information.data.submit_time,
        });
      }
    })
  },

  // 通过 
  choose_pass: function () {
    var usernames = wx.getStorageSync('usernames');
    var sequence_numbers = wx.getStorageSync('sequence_numbers');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var sequence_number = sequence_numbers[0]
    var that = this
    that.setData({
      sequence_number: sequence_number
    });
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_index/check_school_certificate/check_school_certificate_choose_pass',
      data: {
        username: JSON.stringify(username),
        sequence_number: JSON.stringify(sequence_number)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data);
        that.setData({
          disabled: !that.data.disabled
        }),

          console.log(res.data);

        wx.showToast({
          title: '更改为通过',
          icon: 'success',
          duration: 2000
        })

      }
    })
  },

  // 不通过 
  choose_dispass: function () {
    var usernames = wx.getStorageSync('usernames');
    var sequence_numbers = wx.getStorageSync('sequence_numbers');
    // 然后存到本地数据区对应的数组中
    var username = usernames[0]
    var sequence_number = sequence_numbers[0]
    var that = this
    that.setData({
      sequence_number: sequence_number
    });
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_index/check_school_certificate/check_school_certificate_choose_dispass',
      data: {
        username: JSON.stringify(username),
        sequence_number: JSON.stringify(sequence_number)
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success: function (res) {
        console.log(res.data);
        that.setData({
          disabled: !that.data.disabled
        }),

          console.log(res.data);

        wx.showToast({
          title: '更改为不通过',
          icon: 'success',
          duration: 2000
        })

      }
    })
  },
})