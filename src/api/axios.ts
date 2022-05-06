/* eslint-disable @typescript-eslint/ban-ts-comment */
import axios, { AxiosRequestConfig, AxiosResponse } from 'axios'
import { Message } from '@arco-design/web-vue' // 引入el 提示框，这个项目里用什么组件库这里引什么
import { showMessage } from './status'
// 引入状态码文件
export interface HttpResponse<T = unknown> {
  msg: string;
  code: number;
  data: T;
}
// 设置接口超时时间
axios.defaults.timeout = 5000

// 请求地址，这里是动态赋值的的环境变量，下一篇会细讲，这里跳过
// @ts-ignore
// axios.defaults.baseURL = '/api'   
if (import.meta.env.VITE_API_BASE_URL) {
  axios.defaults.baseURL = import.meta.env.VITE_API_BASE_URL
}
// http request 拦截器
axios.interceptors.request.use(
  (config: AxiosRequestConfig) => config,
  error => {
    console.log(`request error, ${ error }`)
    Promise.reject(error)
  }
)

// http response 拦截器
axios.interceptors.response.use(
  (response: AxiosResponse<HttpResponse>) => response,
  error => {
    const { response } = error
    if (response) {
      // 请求已发出，但是不在2xx的范围
      // showMessage(response.status) // 传入响应码，匹配响应码对应信息
      Message.warning(showMessage(response.status))
      return Promise.reject(response.data)
    } 
    Message.warning('Networking error')
  }
)

export default axios