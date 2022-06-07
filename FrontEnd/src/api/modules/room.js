import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import roomStore from '../../store/modules/roomStore'

export default {
  getRoomBookingLists () {
    myAxios
      .get(Urls.room_All)
      .then(response => {
        roomStore.state.roomBookingLists = response.data
      })
      .catch(error => {
        console.log('getBookedRoomList GET error', error.response)
      })
  },

  BookRoom (component, postData) {
    myAxios
      .post(Urls.room_All, postData)
      .then(response => {
        this.getRoomBookingLists()
        component.dialog.bookRoom = false
      })
      .catch(error => {
        console.log('Bookroom POST error', error.response)
      })
  },

  DestroyBookedRoom (destroyId) {
    myAxios
      .delete(Urls.room_Destroy(destroyId))
      .then(response => {
        this.getRoomBookingLists()
      })
      .catch(error => {
        console.log('DestroyBookedRoom DELETE error', error.response)
      })
  },

  getAvailableEvents (component, room, date) {
    myAxios
      .get(Urls.room_AvailableEvents(room, date))
      .then(response => {
        roomStore.state.availableBookingEvents = response.data
      })
      .catch(error => {
        console.log('getAvailableEvents GET error', error.response)
      })
  },

  getRoomBookingsByDate (room, date) {
    myAxios
      .get(Urls.room_BookingByDate(room, date))
      .then(response => {
        roomStore.state.roomBookingLists = response.data
      })
      .catch(error => {
        console.log('getRoomBookingsByDate GET error', error.response)
      })
  }
}
