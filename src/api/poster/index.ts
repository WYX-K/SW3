/* eslint-disable @typescript-eslint/ban-ts-comment */
import { AxiosRequestConfig } from 'axios'
import axios from '@/api/axios'

export function postPoster(prama: FormData) {
  return axios.post('/api/poster', prama)
}

export function deletePoster(prama: FormData) {
  // @ts-ignore
  return axios.delete('/api/poster', prama)
}

export function getPoster(prama: AxiosRequestConfig) {
  return axios.get('/api/poster', prama)
}