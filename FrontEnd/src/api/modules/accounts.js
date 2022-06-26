import myAxios from '@/api/AxiosInstanceController'
// import router from '@/router'
import Urls from '@/api/urls'
import generalStore from '@/store/modules/generalStore'
import settingApi from '@/api/modules/setting'

export default {
  register (postData) {
    myAxios
      .post(Urls.accounts_Register, postData)
      .then(response => {
        generalStore.state.successMsg = '학교가 등록되었습니다. ' + response.data.name + '의 학교 링크 ' + response.data.code + '로 접속해주세요.'
        generalStore.state.dialog.success = true
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
  },

  // refreshToken () {
  //   console.log(Request.Cookies)

  //   myAxios
  //     .get(Urls.accounts_Login)
  //     .then(response => {
  //       this.setToken(response)
  //     })
  //     .catch(error => {
  //       console.log('refreshToken GET error', error)
  //       if (error.data.message === 'NEED_LOGIN') {
  //         generalStore.state.dialog.login = true
  //       }
  //     })
  // },

  // setToken (response) {
  //   generalStore.state.access.token = response.data['access_token']
  //   generalStore.state.access.exp = response.data['access_token_expiration']
  //   // setTimeout(this.refreshToken, generalStore.state.access.exp - 60000)
  //   this.getUser()
  // },

  getUser () {
    myAxios
      .get(Urls.accounts_Info)
      .then(response => {
        generalStore.state.school = response.data
        generalStore.state.dialog.login = false
      })
      .catch(error => {
        console.log('getUser GET error', error)
      })
  }

  // logout () {
  //   myAxios
  //     .get(Urls.accounts_Logout)
  //     .then(response => {
  //       generalStore.state.access = {token: '', exp: ''}
  //       generalStore.state.school = { name: 'Guest' }
  //       generalStore.state.dialog.logout = false
  //       router.push('/')
  //     })
  //     .catch(error => {
  //       console.log('logout GET error.response', error)
  //     })
  // }
}
