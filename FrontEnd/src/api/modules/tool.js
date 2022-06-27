import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import toolStore from '../../store/modules/toolStore'

export default {
  BookTool (component, postData) {
    myAxios
      .post(Urls.tool_All, postData)
      .then(response => {
        this.getToolBookingsByDate(postData['tool'], postData['date'])
        component.dialog.bookTool = false
      })
      .catch(error => {
        console.log('BookTool POST error', error.response)
      })
  },

  getToolBookingsByDate (tool, date) {
    myAxios
      .get(Urls.tool_BookingByDate(tool, date))
      .then(response => {
        toolStore.state.toolBookingLists = response.data
        this.getAvailableLeft(tool, date)
        toolStore.state.dialog.checkToolBooking = true
      })
      .catch(error => {
        console.log('getToolBookingsByDate GET error', error.response)
      })
  },

  DestroyToolBooking (bookingId, tool, date) {
    myAxios
      .delete(Urls.tool_DestroyBooking(bookingId))
      .then(response => {
        this.getToolBookingsByDate(tool, date)
      })
      .catch(error => {
        console.log('DestroyToolBooking DELETE error', error.response)
      })
  },

  getAvailableLeft (tool, date) {
    myAxios
      .get(Urls.tool_Left(tool, date))
      .then(response => {
        toolStore.state.left = response.data
      })
      .catch(error => {
        console.log('getAvailableLeft GET error', error.response)
      })
  }
}
