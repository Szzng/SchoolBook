import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import toolStore from '../../store/modules/toolStore'
import roomStore from '../../store/modules/roomStore'

export default {
  settoolPlaces (postData) {
    myAxios
      .post(Urls.setting_toolPlaces, postData)
      .then(response => {
        toolStore.state.places = response.data
      })
      .catch(error => {
        console.log('settoolPlaces POST error', error.response)
      })
  },

  setRoomPlaces (postData) {
    myAxios
      .post(Urls.setting_RoomPlaces, postData)
      .then(response => {
        roomStore.state.places = response.data
      })
      .catch(error => {
        console.log('setRoomPlaces POST error', error.response)
      })
  },

  getRoomPlaces () {
    myAxios
      .get(Urls.setting_RoomPlaces)
      .then(response => {
        roomStore.state.places = response.data
      })
      .catch(error => {
        console.log('getRoomPlaces GET error', error.response)
      })
  },

  DestroyRoomPlace (placeName) {
    myAxios
      .delete(Urls.setting_DestroyRoomPlace(placeName))
      .then(response => {
        this.getRoomPlaces()
      })
      .catch(error => {
        console.log('DestroyRoomPlace DELETE error', error.response)
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
