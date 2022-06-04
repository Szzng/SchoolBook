import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import toolStore from '../../store/modules/toolStore'
import roomStore from '../../store/modules/roomStore'

export default {
  setToolPlaces (postData) {
    myAxios
      .post(Urls.setting_toolPlaces, postData)
      .then(response => {
        toolStore.state.places = response.data
      })
      .catch(error => {
        console.log('settoolPlaces POST error', error.response)
      })
  },

  createRoom (postData) {
    myAxios
      .post(Urls.setting_Room, postData)
      .then(response => {
        this.getRoomPlaces()
      })
      .catch(error => {
        console.log('createRoom POST error', error.response)
      })
  },

  getRoomPlaces () {
    myAxios
      .get(Urls.setting_Room)
      .then(response => {
        roomStore.state.places = response.data
      })
      .catch(error => {
        console.log('getRoomPlaces GET error', error.response)
      })
  },

  DestroyRoomPlace (placeName) {
    myAxios
      .delete(Urls.setting_DestroyRoom, { data: { 'placeName': placeName } })
      .then(response => {
        this.getRoomPlaces()
      })
      .catch(error => {
        console.log('DestroyRoomPlace DELETE error', error.response)
      })
  },

  getTimetable (room) {
    myAxios
      .get(Urls.setting_GetTimetableByRoom(room))
      .then(response => {
        roomStore.state.timetable = response.data
        roomStore.state.dialog.updateTimetable = true
      })
      .catch(error => {
        console.log('getTimetable GET error', error.response)
      })
  },

  updateTimetable (postData) {
    myAxios
      .post(Urls.setting_UpdateTimetable, postData)
      .then(response => {
        this.getTimetable(postData.placeName)
      })
      .catch(error => {
        console.log('updateTimetable POST error', error.response)
      })
  }

}
