import axios from '@/api/axios'

export interface LoginData {
  username: string;
  password: string;
}

export interface LoginRes {
  data: any;
  token: string;
}

export function getLoginData(prama: FormData) {
  // return axios.post<LoginRes>('/api/login', data)
  return axios.post<LoginRes>('/mock/login', prama)
}
