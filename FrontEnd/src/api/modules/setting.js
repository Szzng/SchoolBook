import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import roomStore from '@/store/modules/roomStore'
import toolStore from '@/store/modules/toolStore'

export default {
  createTool (postData) {
    myAxios
      .post(Urls.setting_Tool, postData)
      .then(response => {
        this.getTools()
      })
      .catch(error => {
        console.log('createTool POST error', error.response)
      })
  },

  getTools () {
    myAxios
      .get(Urls.setting_Tool)
      .then(response => {
        toolStore.state.tools = response.data
      })
      .catch(error => {
        console.log('getTools GET error', error.response)
      })
  },

  destroyTool (tool) {
    myAxios
      .delete(Urls.setting_DestroyTool, { data: { 'tool': tool } })
      .then(response => {
        this.getTools()
      })
      .catch(error => {
        console.log('destroyTool DELETE error', error.response)
      })
  },

  createRoom (postData) {
    myAxios
      .post(Urls.setting_Room, postData)
      .then(response => {
        this.getRooms()
      })
      .catch(error => {
        console.log('createRoom POST error', error.response)
      })
  },

  getRooms () {
    myAxios
      .get(Urls.setting_Room)
      .then(response => {
        roomStore.state.rooms = response.data
      })
      .catch(error => {
        console.log('getRooms GET error', error.response)
      })
  },

  destroyRoom (room) {
    myAxios
      .delete(Urls.setting_DestroyRoom, { data: { 'room': room } })
      .then(response => {
        this.getRooms()
      })
      .catch(error => {
        console.log('destroyRoom DELETE error', error.response)
      })
  },

  getTimetable (room) {
    myAxios
      .get(Urls.setting_TimetableByRoom(room))
      .then(response => {
        roomStore.state.timetable = response.data
        roomStore.state.dialog.updateTimetable = true
      })
      .catch(error => {
        console.log('getTimetable GET error', error.response)
      })
  },

  updateTimetable (postData) {
    myAxios
      .post(Urls.setting_UpdateTimetable, postData)
      .then(response => {
        this.getTimetable(postData.room)
      })
      .catch(error => {
        console.log('updateTimetable POST error', error.response)
      })
  }

}
