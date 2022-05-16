// import Vue from 'vue'
import axios from 'axios'
import Urls from '@/api/urls'

function createAxiosInstance (baseUrl, timeOut) {
  const axiosInstance = axios.create({
    baseURL: baseUrl,
    timeout: timeOut
  })
  return axiosInstance
}

// function setInterceptors (instance) {
//   instance.interceptors.request.use(
//     function (config) {
//       return config
//     },
//     function (error) {
//       console.log(error)
//       return Promise.reject(error)
//     }
//   )

//   instance.interceptors.response.use(
//     function (response) {
//       Vue.$log.debug(`URL Check - ${response.config.baseURL}`)
//       return response
//     },
//     function (error) {
//       Vue.$log.error('!intercept error!', error)
//       Vue.$log.error('status : ', error.response.status)
//       Vue.$log.error('message : ', error.response.data.message)
//       // ErrorController(error)
//       return Promise.reject(error.response)
//     })

//   return instance
// }

const myAxios = createAxiosInstance(Urls.Django_API, 1000)

export default myAxios