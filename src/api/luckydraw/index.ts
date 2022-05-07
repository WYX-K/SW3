import axios from '@/api/axios'

export function postLuckyDraw() {
  return axios.post('/api/luckydraw')
}

export function getLuckyDraw() {
  return axios.get('/api/luckydraw')
}
