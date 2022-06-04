import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import toolStore from '../../store/modules/toolStore'

export default {
  getBookedtoolListByDate (place, date) {
    myAxios
      .get(Urls.tool_ByDate(place, date))
      .then(response => {
        toolStore.state.bookedToolLists = response.data
      })
      .catch(error => {
        console.log('getBookedtoolListByDate GET error', error.response)
      })
  },

  Booktool (component, postData) {
    myAxios
      .post(Urls.tool_All, postData)
      .then(response => {
        this.getBookedtoolListByDate(postData['place.name'], postData['time.date'])
        this.getLefttoolCounts(postData['place.name'], postData['time.date'])
        component.dialog.booktool = false
      })
      .catch(error => {
        console.log('Booktool POST error', error.response)
      })
  },

  DestroyBookedtool (destroyId, place, date) {
    myAxios
      .delete(Urls.tool_Destroy(destroyId))
      .then(response => {
        this.getBookedtoolListByDate(place, date)
        this.getLefttoolCounts(place, date)
      })
      .catch(error => {
        console.log('DestroyBookedtool DELETE error', error.response)
      })
  },

  getLefttoolCounts (place, date) {
    myAxios
      .get(Urls.tool_Left(place, date))
      .then(response => {
        toolStore.state.left = response.data
      })
      .catch(error => {
        console.log('getLefttoolCount GET error', error.response)
      })
  }
}
