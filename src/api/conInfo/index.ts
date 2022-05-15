import axios from '@/api/axios'

export function getConInfo() {
  return axios.get('/api/conInfo')
}