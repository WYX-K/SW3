import axios from '@/api/axios'

export interface LoginData {
  username: string;
  password: string;
}

export function getLoginData(prama: FormData) {
  return axios.post('/api/login', prama)
  // return axios.post<LoginRes>('/mock/login', prama)
}
