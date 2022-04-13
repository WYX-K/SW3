export type RoleType = '' | 'admin' | 'user';
export interface UserState {
  name?: string;
  role: RoleType;
}
