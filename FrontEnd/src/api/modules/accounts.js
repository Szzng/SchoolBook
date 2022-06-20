import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import generalStore from '@/store/modules/generalStore'

export default {
  register (postData) {
    myAxios
      .post(Urls.accounts_Register, postData)
      .then(response => {
        generalStore.state.successMsg = '학교 이름( ' + response.data.name + ' )과 IP 주소가 등록되었습니다. 학교 이름으로 로그인하세요.'
        generalStore.state.dialog.success = true
      })
      .catch(error => {
        console.log('register POST error', error.response)
      })
  },

  getSchoolDetail () {
    myAxios
      .get(Urls.account_Detail)
      .then(response => {
        generalStore.state.school = response.data
        generalStore.state.dialog.login = false
      })
      .catch(error => {
        console.log('getSchoolDetail GET error', error.response)
      })
  },

  login (postData) {
    myAxios
      .post(Urls.accounts_Login, postData)
      .then(response => {
        localStorage.setItem('access_token', response.data['access_token'])
        this.getSchoolDetail()
      })
      .catch(error => {
        console.log('login POST error', error.response)
      })
  },

  logout () {
    myAxios
      .get(Urls.accounts_Logout)
      .then(response => {
        localStorage.removeItem('access_token')
        generalStore.state.school = { name: 'Guest' }
        generalStore.state.dialog.logout = false
      })
      .catch(error => {
        console.log('logout GET error.response', error.response)
      })
  }
}
