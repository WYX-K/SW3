import Mock from 'mockjs'
import setupMock, {
  successResponseWrap,
  failResponseWrap,
} from '@/utils/setup-mock'

import { MockParams } from '@/types/mock'

setupMock({
  setup() {
    Mock.mock(new RegExp('/mock/poster/get'), (params: MockParams) => {
      const value:FormData = params.body
      const username = value.get('pageNum')
      const password = value.get('user')

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