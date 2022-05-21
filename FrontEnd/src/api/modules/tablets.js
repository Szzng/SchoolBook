import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import bookStore from '../../store/modules/bookStore'

export default {
  getBookedTabletsListByDate (date) {
    myAxios
      .get(Urls.tabletsByDate(date))
      .then(response => {
        bookStore.state.bookedTabletsLists = response.data
      })
      .catch(error => {
        console.log('getBookedTabletsListByDate GET error', error.response)
      })
  },

  BookTablets (component, postData) {
    myAxios
      .post(Urls.tabletsAll, postData)
      .then(response => {
        this.getBookedTabletsListByDate(postData['time.date'])
        component.dialog.bookTablets = false
      })
      .catch(error => {
        console.log('BookTablets POST error', error.response)
      })
  },

  DestroyBookedTablets (destroyId, date) {
    myAxios
      .delete(Urls.tabletDestroy(destroyId))
      .then(response => {
        this.getBookedTabletsListByDate(date)
      })
      .catch(error => {
        console.log('BookTablets POST error', error.response)
      })
  },

  getLeftTabletsCounts (component, date) {
    myAxios
      .get(Urls.tabletLeft(date))
      .then(response => {
        component.left = response.data
      })
      .catch(error => {
        console.log('getLeftTabletsCount GET error', error.response)
      })
  }
}
