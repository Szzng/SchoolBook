import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import bookStore from '../../store/modules/bookStore'

export default {
  getBookedTabletsListByDate (date) {
    console.log('getBookedTabletsListByDate()...')
    myAxios
      .get(Urls.bookedTabletsByDate(date))
      .then(response => {
        console.log('getBookedTabletsListByDate GET response', response)
        bookStore.state.bookedTabletsLists = response.data
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
        this.getBookedTabletsListByDate(postData['time.date'])
        component.dialog.bookTablets = false
      })
      .catch(error => {
        console.log('BookTablets POST error', error.response)
      })
  },

  DestroyBookedTablets (destroyId, date) {
    console.log('BookTablets()...')
    myAxios
      .delete(Urls.destroyBookedTablet(destroyId))
      .then(response => {
        console.log('BookTablets POST response', response)
        this.getBookedTabletsListByDate(date)
      })
      .catch(error => {
        console.log('BookTablets POST error', error.response)
      })
  }
}
