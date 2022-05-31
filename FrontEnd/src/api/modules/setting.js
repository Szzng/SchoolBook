import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import tabletsStore from '../../store/modules/tabletsStore'
import classroomStore from '../../store/modules/classroomStore'

export default {
  setTabletsPlaces (postData) {
    myAxios
      .post(Urls.settingTabletsPlaces, postData)
      .then(response => {
        tabletsStore.state.places = response.data
      })
      .catch(error => {
        console.log('setTabletsPlaces POST error', error.response)
      })
  },

  setClassroomPlaces (postData) {
    myAxios
      .post(Urls.settingClassroomPlaces, postData)
      .then(response => {
        classroomStore.state.places = response.data
      })
      .catch(error => {
        console.log('setClassroomPlaces POST error', error.response)
      })
  },

  setFixedTimeTable (postData) {
    myAxios
      .post(Urls.settingFixedTimeTable, postData)
      .then(response => {
        //
      })
      .catch(error => {
        console.log('setFixedTimeTable POST error', error.response)
      })
  }
}
