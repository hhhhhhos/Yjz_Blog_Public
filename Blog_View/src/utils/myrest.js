import axios from 'axios'
import { v4 as uuidv4 } from 'uuid'

// 设定生产模式时前缀
const apiClient = axios.create({
  baseURL: process.env.VUE_APP_BASE_API
  // 其他配置...
})

// 封装了'axios'的post get请求方法 还有我很多其他方法
const myrest = {
  // 警告窗口函数 vuethis要调用api的vue的this才能正确显示
  err_win (vuethis, themessage) {
    vuethis.$message.error(themessage)
  },
  // 成功窗口函数
  suc_win (vuethis, themessage) {
    vuethis.$message({
      message: themessage,
      type: 'success'
    })
  },
  // 请求函数 实验
  rest_test ({ vuethis, method, url, data = {}, params = {} }) {
    return apiClient({
      method,
      url,
      timeout: 10000, // 设置超时时间为 10 秒
      data,
      params
    })
      .catch(error => {
        if (error.code === 'ECONNABORTED') {
          // 请求超时
          console.log('Request timed out')
          this.err_win(vuethis, 'Request timed out')
        } else {
          // 其他错误
          console.log(error)
          this.err_win(vuethis, error.message)
          setTimeout(() => {
            this.err_win(vuethis, error.response.data.detail)
          }, 500)
        }
        return error
      })
  },
  // 获取用户ip 和 地址
  Get_userip_lc () {
    let userIp
    let location
    let finallocation
    axios.get('https://api.ipify.org?format=json')
      .then(response => {
        userIp = response.data.ip
        axios.get(`https://api.vore.top/api/IPdata?ip=${userIp}`)
          .then(res => {
            location = res.data
            console.log(location)
            if (location.ipdata.info1) {
              if (location.ipdata.info2) {
                if (location.ipdata.info3) {
                  console.log(finallocation = location.ipdata.info2 + ' -' + location.ipdata.info3)
                } else {
                  console.log(finallocation = location.ipdata.info1 + ' -' + location.ipdata.info2)
                }
              } else {
                console.log(finallocation = location.ipdata.info1)
              }
            } else {
              if (location.ipdata.info2) {
                console.log(finallocation = location.ipdata.info2)
              } else {
                console.log(finallocation = '火星')
              }
            }
            console.log(userIp)
            // 在这里将用户IP发送到后端服务器
            // axios.post('/your-backend-api', { ip: userIp })
          })
          .catch(() => { console.log(finallocation = 'Unknow') })
      })
      .catch(() => { console.log(userIp = 'Unknow') })
    return { userIp, finallocation }
  },
  // 获取用户ip 和 地址 第二版
  Get_userip_lc2 () {
    let userIp
    let location = 'Unknow'
    let finallocation = 'Unknow'
    console.log('test111')
    axios.get('https://api.ipify.org?format=json')
      .then(response => {
        userIp = response.data.ip
        axios.get(`https://api.vore.top/api/IPdata?ip=${userIp}`)
          .then(res => {
            location = res.data
            console.log(location)
            let lis = [!!location.ipdata.info1, !!location.ipdata.info1, !!location.ipdata.info1]
            console.log(lis)
            lis = lis.map(info => info ? '1' : '0').join('')// map类似for
            if (/11$/.test(lis) && location.ipdata.info2 !== location.ipdata.info3) finallocation = location.ipdata.info2 + '.' + location.ipdata.info3
            else if (/101$/.test(lis)) finallocation = location.ipdata.info1 + '.' + location.ipdata.info3
            else if (/1$/.test(lis)) finallocation = location.ipdata.info3
            else if (/^11/.test(lis)) finallocation = location.ipdata.info1 + '.' + location.ipdata.info2
            else if (/10$/.test(lis)) finallocation = location.ipdata.info1
            else if (/010$/.test(lis)) finallocation = location.ipdata.info2
            else finallocation = '火星'
            console.log(finallocation)
          })
          .catch(() => { console.log(finallocation = 'Unknow') })
      })
      .catch(err => { console.log('test222'); console.log(err) })
    console.log('test333')
    return { userIp, finallocation }
  },
  // 获取用户ip 和 地址 第三版 如果获取成功会返回ip和城市 失败返回两个unknow
  async Get_userip_lc3 () {
    let userIp = 'Unknow' // 指定默认值 不然传空给后台会442 实体不合法
    let location
    let finallocation = 'Unknow' // 指定默认值 不然传空给后台会442 实体不合法
    try {
      const response = await axios.get('https://api.ipify.org?format=json')
      userIp = response.data.ip
      const res = await axios.get(`https://api.vore.top/api/IPdata?ip=${userIp}`)
      location = res.data
      console.log(location)
      let lis = [!!location.ipdata.info1, !!location.ipdata.info1, !!location.ipdata.info1]
      console.log(lis)
      lis = lis.map(info => info ? '1' : '0').join('') // map类似for
      if (/11$/.test(lis) && location.ipdata.info2 !== location.ipdata.info3) finallocation = location.ipdata.info2 + '.' + location.ipdata.info3
      else if (/101$/.test(lis)) finallocation = location.ipdata.info1 + '.' + location.ipdata.info3
      else if (/1$/.test(lis)) finallocation = location.ipdata.info3
      else if (/^11/.test(lis)) finallocation = location.ipdata.info1 + '.' + location.ipdata.info2
      else if (/10$/.test(lis)) finallocation = location.ipdata.info1
      else if (/010$/.test(lis)) finallocation = location.ipdata.info2
      else finallocation = '火星'
      console.log(finallocation)
    } catch (error) {
      console.log('Error:', error)
    }
    return { userIp, finallocation }
  },
  // 把访问记录传到后端吧 改成nginx传到后端处理了 废弃
  async user_history (to) {
    // 用户独特id
    let userid = window.localStorage.getItem('userid')
    if (!userid) {
      userid = uuidv4()
      window.localStorage.setItem('userid', userid)
    }
    const res = await this.Get_userip_lc3()
    axios.post('/iphistory/info', {
      userid: userid,
      userIp: res.userIp,
      unicode: userid,
      finallocation: res.finallocation,
      url: to
    })
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })
  }
}
export default myrest
