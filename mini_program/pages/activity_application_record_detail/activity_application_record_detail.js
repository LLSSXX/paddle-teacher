Page({
  data: {
    disabled: false,
    loading: false,
    name: '',
    school_number: '',
    choose_college: '',
    profession: '',
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
      url: 'https://paddle-teacher.xyz/student_my/application_record/activity_application_record/activity_application_record_detail',
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
          choose_college: information.data.college,
          profession: information.data.profession,
          area: information.data.area,
          use_date: information.data.use_date,
          begin_time: information.data.begin_time,
          end_time: information.data.end_time,
          purpose: information.data.purpose,
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
    }),
    wx.navigateBack({
      delta: 1
    })
  }
})