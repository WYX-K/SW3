import debug from './env'

export default ({ mock, setup }: { mock?: boolean; setup: () => void }) => {
  if (mock !== false && debug) setup()
}

export const successResponseWrap = (data: unknown) => ({
  data,
  status: 'ok',
  msg: '请求成功',
  code: 20000,
})

export const failResponseWrap = (data: unknown, msg: string, code = 50000) => ({
  data,
  status: 'fail',
  msg,
  code,
})
