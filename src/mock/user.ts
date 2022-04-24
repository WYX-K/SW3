import Mock from 'mockjs'
import setupMock, {
  successResponseWrap,
  failResponseWrap,
} from '@/utils/setup-mock'

import { MockParams } from '@/types/mock'

setupMock({
  setup() {
    // 登录
    Mock.mock(new RegExp('/mock/login'), (params: MockParams) => {
      const value:FormData = params.body
      const username = value.get('username')
      const password = value.get('pwd')

      if (username === 'simon' && password === 'simon') {
        return successResponseWrap({
          name: 'Simon',
          role: 'uicer', // 类型有 'admin' | 'uicer' | 'dean' | 'judge'| 'head_judge' | 'con_coor'
        })
      }
      return failResponseWrap(null, '账号或者密码错误', 404)
    })
  },
})
