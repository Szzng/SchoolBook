import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'

export default {
  getBookedTabletsListByDate (component, date) {
    console.log('getBookedTabletsListByDate()...')
    myAxios
      .get(Urls.bookedTabletsByDate(date))
      .then(response => {
        console.log('getBookedTabletsListByDate GET response', response)
        component.bookedTabletsLists = response.data
        // component.dialog.checkTabletsBooking = true
      })
      .catch(error => {
        console.log('getBookedTabletsListByDate GET error', error.response)
      })
  },

  BookTablets (component, postData) {
    console.log('BookTablets()...')
    myAxios
      .post(Urls.allBookedTablets, postData)
      .then(response => {
        console.log('BookTablets POST response', response)
        component.bookedTabletsLists = response.data
        component.dialog.bookTablets = false
      })
      .catch(error => {
        console.log('BookTablets POST error', error.response)
      })
  }
}
