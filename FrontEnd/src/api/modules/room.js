import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import roomStore from '../../store/modules/roomStore'

export default {
  getRoomBookingsByDate (room, date) {
    myAxios
      .get(Urls.room_BookingByDate(room, date))
      .then(response => {
        roomStore.state.roomBookingLists = response.data
      })
      .catch(error => {
        console.log('getRoomBookingsByDate GET error', error)
      })
  },

  BookRoom (component, postData) {
    myAxios
      .post(Urls.room_All, postData)
      .then(response => {
        this.getRoomBookingsByDate(postData.room, postData.date)
        this.getAvailableEvents(postData.room, postData.date)
        component.dialog.bookRoom = false
      })
      .catch(error => {
        console.log('BookRoom POST error', error)
      })
  },

  DestroyRoomBooking (bookingId, password, room, date) {
    myAxios
      .delete(Urls.room_DestroyBooking(bookingId), { data: {'password': password} })
      .then(response => {
        this.getRoomBookingsByDate(room, date)
        this.getAvailableEvents(room, date)
      })
      .catch(error => {
        console.log('DestroyRoomBooking DELETE error', error)
      })
  },

  getAvailableEvents (room, date) {
    myAxios
      .get(Urls.room_AvailableEvents(room, date))
      .then(response => {
        roomStore.state.availableBookingEvents = response.data
      })
      .catch(error => {
        console.log('getAvailableEvents GET error', error)
      })
  }
}
