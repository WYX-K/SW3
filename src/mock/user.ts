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
        window.localStorage.setItem('userRole', 'user')
        return successResponseWrap({
          name: '王立群',
          avatar:
            '//lf1-xgcdn-tos.pstatp.com/obj/vcloud/vadmin/start.8e0e4855ee346a46ccff8ff3e24db27b.png',
          email: 'wangliqun@email.com',
          job: 'frontend',
          jobName: '前端艺术家',
          organization: 'Frontend',
          organizationName: '前端',
          location: 'beijing',
          locationName: '北京',
          introduction: '人潇洒，性温存',
          personalWebsite: 'https://www.arco.design',
          phone: '150****0000',
          registrationDate: '2013-05-10 12:10:00',
          accountId: '15012312300',
          certification: 1,
          role: 'user',
        })
      }
      return failResponseWrap(null, '账号或者密码错误', 500)
    })
  },
})
