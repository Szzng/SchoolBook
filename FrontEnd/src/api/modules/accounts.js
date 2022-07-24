import myAxios from '@/api/AxiosInstanceController'
// import router from '@/router'
import Urls from '@/api/urls'
import generalStore from '@/store/modules/generalStore'
import settingApi from '@/api/modules/setting'

export default {
  register (postData, component) {
    myAxios
      .post(Urls.accounts_Register, postData)
      .then(response => {
        component.name = response.data.name
        component.code = response.data.code
        generalStore.state.dialog.registerSuccess = true
      })
      .catch(error => {
        console.log('register POST error', error)
      })
  },

  login (code) {
    myAxios
      .get(Urls.accounts_Login(code))
      .then(response => {
        generalStore.state.school = { name: response.data.name, code: response.data.code }
        generalStore.state.code = response.data.code
        settingApi.getRooms()
        settingApi.getTools()
      })
      .catch(error => {
        console.log('login GET error', error)
      })
  }
}
