import axios from '@/api/axios'
import { RoleType } from '@/store/modules/user/types'

export interface LoginData {
  username: string;
  password: string;
}

export interface LoginRes {
  name: string;
  role: RoleType;
  major: string;
}

export function getLoginData(prama: FormData) {
  return axios.post<LoginRes>('/api/login', prama)
  // return axios.post<LoginRes>('/mock/login', prama)
}
