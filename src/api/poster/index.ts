import axios from '@/api/axios'

export function postPoster(prama: FormData) {
  return axios.post('/api/poster', prama)
}