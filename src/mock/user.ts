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
          name: '王立群',
          role: 'user',
        })
      }
      return failResponseWrap(null, '账号或者密码错误', 500)
    })
  },
})
