import { request } from '@/utils/axios'

export class UserService { // 模块一
  /**
   * @description 用户登录
   * @param {string} username - 用户名
   */
  static async login(params: object) { // 接口一
    return request('/login', params, 'post')
  }
}