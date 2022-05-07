import { AxiosRequestConfig } from 'axios'
import axios from '@/api/axios'

export function postPoster(data: FormData) {
  return axios.post('/api/poster', data)
}

export function deletePoster(data: AxiosRequestConfig) {
  return axios.delete('/api/poster/', data)
}

export function getPoster(prama: AxiosRequestConfig) {
  return axios.get('/api/poster', prama)
}

export function editPoster(data: FormData) {
  return axios.post('/api/editPoster', data)
}