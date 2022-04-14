import axios from '@/api/axios'

export interface LoginData {
  username: string;
  password: string;
}

export interface LoginRes {
  token: string;
}
export function login(data: object) {
  return axios.post<LoginRes>('/api/login', data)
}
