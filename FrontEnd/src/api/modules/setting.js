import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import tabletsStore from '../../store/modules/tabletsStore'
import classroomStore from '../../store/modules/classroomStore'

export default {
  setTabletsPlaces (postData) {
    myAxios
      .post(Urls.setting_TabletsPlaces, postData)
      .then(response => {
        tabletsStore.state.places = response.data
      })
      .catch(error => {
        console.log('setTabletsPlaces POST error', error.response)
      })
  },

  setClassroomPlaces (postData) {
    myAxios
      .post(Urls.setting_ClassroomPlaces, postData)
      .then(response => {
        classroomStore.state.places = response.data
      })
      .catch(error => {
        console.log('setClassroomPlaces POST error', error.response)
      })
  },

  getClassroomPlaces () {
    myAxios
      .get(Urls.setting_ClassroomPlaces)
      .then(response => {
        classroomStore.state.places = response.data
      })
      .catch(error => {
        console.log('getClassroomPlaces GET error', error.response)
      })
  },

  DestroyClassroomPlace (placeName) {
    myAxios
      .delete(Urls.setting_DestroyClassroomPlace(placeName))
      .then(response => {
        this.getClassroomPlaces()
      })
      .catch(error => {
        console.log('DestroyClassroomPlace DELETE error', error.response)
      })
  },

  getFixedTimeTable (component, placeName) {
    myAxios
      .get(Urls.setting_ByPlaceFixedTimeTable(placeName))
      .then(response => {
        component.fixedTimeTable = response.data
      })
      .catch(error => {
        console.log('setFixedTimeTable GET error', error.response)
      })
  },

  setFixedTimeTable (component, postData) {
    myAxios
      .post(Urls.setting_FixedTimeTable, postData)
      .then(response => {
        this.getFixedTimeTable(component, postData.placeName)
      })
      .catch(error => {
        console.log('setFixedTimeTable POST error', error.response)
      })
  }

}
