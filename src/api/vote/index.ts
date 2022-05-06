/* eslint-disable @typescript-eslint/ban-ts-comment */
import axios from '@/api/axios'

export function getVote(prama: FormData) {
  // @ts-ignore
  return axios.get('/api/vote', prama)
}

export function postVote(prama: FormData) {
  return axios.post('/api/vote', prama)
}