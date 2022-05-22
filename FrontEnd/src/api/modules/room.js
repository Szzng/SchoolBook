import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import roomStore from '../../store/modules/roomStore'

export default {
  getBookedRoomLists () {
    myAxios
      .get(Urls.roomAll)
      .then(response => {
        roomStore.state.bookedRoomLists = response.data
      })
      .catch(error => {
        console.log('getBookedRoomList GET error', error.response)
      })
  },
  BookRoom (component, postData) {
    myAxios
      .post(Urls.roomAll, postData)
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
      .get(Urls.roomByDate(date))
      .then(response => {
        roomStore.state.bookedRoomLists = response.data
      })
      .catch(error => {
        console.log('getBookedRoomListByDate GET error', error.response)
      })
  },

  DestroyBookedRoom (destroyId) {
    myAxios
      .delete(Urls.roomDestroy(destroyId))
      .then(response => {
        this.getBookedRoomLists()
      })
      .catch(error => {
        console.log('BookTablets POST error', error.response)
      })
  }
}
