Page({
  data: {
    disabled: false,
    loading: false,
    name: '',
    school_number: '',
    choose_college: '',
   
    application_reason: '',
    submit_time: '',
    condition: ''
  },
  onLoad: function (options) {
    var that = this
    that.setData({
      sequence_number: options.sequence_number
    });
    wx.request({
      url: 'https://paddle-teacher.xyz/teacher_my/check_record/school_certificate_check_record/school_certificate_check_record_detail',
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
          check_method: information.data.check_method,
          result: information.data.result
        });
      }
    })
  },

  ensure: function () {
    this.setData({
      disabled: !this.data.disabled,
      loading: !this.data.loading
    })
    wx.navigateBack({
      delta: 1
    })
  }
})