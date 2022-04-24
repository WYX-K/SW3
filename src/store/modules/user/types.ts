export type RoleType = 'admin' | 'uicer' | 'dean' | 'judge'| 'head_judge' | 'con_coor'
export interface UserState {
  name?: string;
  role: RoleType;
  isLogin: boolean;
}
