export const showMessage = (status:number|string) : string => {
  let message = ''
  switch (status) {
    case 400:
      message = 'Request Error(400)'
      break
    case 401:
      message = 'Access Denied(403)'
      break
    case 404:
      message = 'Request Error(404)'
      break
    case 500:
      message = 'Server Error(500)'
      break
    default:
      message = `Connection Error(${ status })!`
  }
  return `${ message }, Please check the network or contact your administrator!`
}