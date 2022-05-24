import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import tabletsStore from '../../store/modules/tabletsStore'

export default {
  getBookedTabletsListByDate (place, date) {
    myAxios
      .get(Urls.tabletsByDate(place, date))
      .then(response => {
        tabletsStore.state.bookedTabletsLists = response.data
      })
      .catch(error => {
        console.log('getBookedTabletsListByDate GET error', error.response)
      })
  },

  BookTablets (component, postData) {
    myAxios
      .post(Urls.tabletsAll, postData)
      .then(response => {
        this.getBookedTabletsListByDate(postData['place.name'], postData['time.date'])
        this.getLeftTabletsCounts(postData['place.name'], postData['time.date'])
        component.dialog.bookTablets = false
      })
      .catch(error => {
        console.log('BookTablets POST error', error.response)
      })
  },

  DestroyBookedTablets (destroyId, place, date) {
    myAxios
      .delete(Urls.tabletDestroy(destroyId))
      .then(response => {
        this.getBookedTabletsListByDate(place, date)
        this.getLeftTabletsCounts(place, date)
      })
      .catch(error => {
        console.log('BookTablets DELETE error', error.response)
      })
  },

  getLeftTabletsCounts (place, date) {
    myAxios
      .get(Urls.tabletLeft(place, date))
      .then(response => {
        tabletsStore.state.left = response.data
      })
      .catch(error => {
        console.log('getLeftTabletsCount GET error', error.response)
      })
  }
}
