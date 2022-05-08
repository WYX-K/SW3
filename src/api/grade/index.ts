import { AxiosRequestConfig } from 'axios'
import axios from '@/api/axios'

export function postGrade(data: FormData) {
  return axios.post('/api/grade', data)
}

export function getGrade(prama: AxiosRequestConfig) {
  return axios.get('/api/grade', prama)
}
