// import Vue from 'vue'
import axios from 'axios'
import Urls from '@/api/urls'
import generalStore from '@/store/modules/generalStore'

function createAxiosInstance (baseUrl, timeOut) {
  const axiosInstance = axios.create({
    baseURL: baseUrl,
    timeout: timeOut
  })
  return axiosInstance
}

function setInterceptors (instance) {
  instance.interceptors.request.use(
    function (config) {
      const code = generalStore.state.code
      if (code) {
        config.headers['Authorization'] = code
      }
      return config
    },
    function (error) {
      return Promise.reject(error)
    }
  )

  instance.interceptors.response.use(
    function (response) {
      // Vue.$log.debug(`URL Check - ${response.config.baseURL}`)
      return response
    },
    function (error) {
      // ErrorController(error)

      // if (error.response.data.message === 'EXPIRED_TOKEN') {
      //   accountsApi.refreshToken()
      // }
      generalStore.state.errorMsg = error.response.data.detail
      generalStore.state.dialog.error = true

      // Vue.$log.error('!intercept error!', error)
      // Vue.$log.error('status : ', error.response.status)
      // Vue.$log.error('message : ', error.response.data.message)
      return Promise.reject(error.response)
    })

  return instance
}

const myAxios = setInterceptors(createAxiosInstance(Urls.Django_API, 1000))

export default myAxios
