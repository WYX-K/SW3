/* eslint-disable @typescript-eslint/ban-ts-comment */
import axios from 'axios'
import { Message } from '@arco-design/web-vue' // 引入el 提示框，这个项目里用什么组件库这里引什么
import { showMessage } from './status' // 引入状态码文件

// 设置接口超时时间
axios.defaults.timeout = 5000

// 请求地址，这里是动态赋值的的环境变量，下一篇会细讲，这里跳过
// @ts-ignore
axios.defaults.baseURL = '/api'   

// http request 拦截器
axios.interceptors.request.use(
  config => {
    config.headers = {
      'Content-Type': 'application/json;charset=UTF-8',
      'Access-Control-Allow-Origin': '*',
    }
    // if (storage.get('JWT_TOKEN')) {
    //   config.headers.common.Authorization = `Bearer ${ storage.get('JWT_TOKEN') }`
    // }
    return config
  },
  error => {
    console.log(`request error, ${ error }`)
    Promise.reject(error)
  }
)

// http response 拦截器
axios.interceptors.response.use(
  response => response,
  error => {
    const { response } = error
    if (response) {
      // 请求已发出，但是不在2xx的范围
      showMessage(response.status) // 传入响应码，匹配响应码对应信息
      return Promise.reject(response.data)
    } 
    Message.warning('Networking error')
  }
)

// 封装 GET POST 请求并导出
export function request(url = '', params = {}, type = 'POST') {
// 设置 url params type 的默认值
  return new Promise((resolve, reject) => {
    let promise
    if (type.toUpperCase() === 'GET') {
      promise = axios({
        url,
        params
      })
      promise.then(res => {
        resolve(res)
      }).catch(err => {
        reject(err)
      })
    } else if (type.toUpperCase() === 'POST') {
      promise = axios({
        method: 'POST',
        url,
        data: params
      })
      promise.then(res => {
        resolve(res)
      }).catch(err => {
        reject(err)
      })
    }
  })
}