import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import roomStore from '../../store/modules/roomStore'

export default {
  getBookedRoomLists () {
    myAxios
      .get(Urls.room_All)
      .then(response => {
        roomStore.state.bookedRoomLists = response.data
      })
      .catch(error => {
        console.log('getBookedRoomList GET error', error.response)
      })
  },

  BookRoom (component, postData) {
    myAxios
      .post(Urls.room_All, postData)
      .then(response => {
        this.getBookedRoomLists()
        component.dialog.bookRoom = false
      })
      .catch(error => {
        console.log('Bookroom POST error', error.response)
      })
  },

  getBookedRoomListByDate (date) {
    myAxios
      .get(Urls.room_ByDate(date))
      .then(response => {
        roomStore.state.bookedRoomLists = response.data
      })
      .catch(error => {
        console.log('getBookedRoomListByDate GET error', error.response)
      })
  },

  DestroyBookedRoom (destroyId) {
    myAxios
      .delete(Urls.room_Destroy(destroyId))
      .then(response => {
        this.getBookedRoomLists()
      })
      .catch(error => {
        console.log('Booktool POST error', error.response)
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
        roomStore.state.bookedRoomLists = response.data
      })
      .catch(error => {
        console.log('getRoomBookingsByDate GET error', error.response)
      })
  }
}
