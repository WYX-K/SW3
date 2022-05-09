import { AxiosRequestConfig } from 'axios'
import axios from '@/api/axios'

export function getVote(prama: AxiosRequestConfig) {
  return axios.get('/api/vote', prama)
}

export function postVote(data: FormData) {
  return axios.post('/api/vote', data)
}

export function getPostersVote() {
  return axios.get('/api/pVote')
}
