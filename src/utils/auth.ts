const TOKEN_KEY = 'TOKEN'

const isLogin = () => !!sessionStorage.getItem(TOKEN_KEY)

const getToken = () => sessionStorage.getItem(TOKEN_KEY)

const setToken = (token: string) => {
  sessionStorage.setItem(TOKEN_KEY, token)
}

const clearToken = () => {
  sessionStorage.removeItem(TOKEN_KEY)
}

const clearSession = () => {
  sessionStorage.clear()
}

export { isLogin, getToken, setToken, clearToken, clearSession }
