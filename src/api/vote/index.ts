import { AxiosRequestConfig } from 'axios'
import axios from '@/api/axios'

export function getVote(prama: AxiosRequestConfig) {
  return axios.get('/api/vote', prama)
}

export function postVote(prama: FormData) {
  return axios.post('/api/vote', prama)
}