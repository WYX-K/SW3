import axios from '@/api/axios'

export function postRules(data: FormData) {
  return axios.post('/api/changeRules', data)
}