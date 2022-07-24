import myAxios from '@/api/AxiosInstanceController'
import Urls from '@/api/urls'
import roomStore from '@/store/modules/roomStore'
import toolStore from '@/store/modules/toolStore'
import generalStore from '@/store/modules/generalStore'

export default {
  getTools () {
    myAxios
      .get(Urls.setting_Tool_ListCreate)
      .then(response => {
        toolStore.state.tools = response.data
      })
      .catch(error => {
        console.log('getTools GET error', error)
      })
  },

  createTool (postData) {
    myAxios
      .post(Urls.setting_Tool_ListCreate, postData)
      .then(response => {
        this.getTools()
      })
  },

  getTool (component, tool) {
    myAxios
      .get(Urls.setting_Tool_RetrieveUpdateDestory(tool))
      .then(response => {
        delete response.data['school']
        component.tool = response.data
        component.dialog.updateTool = true
      })
      .catch(error => {
        console.log('getTool GET error', error)
      })
  },

  destroyTool (tool) {
    myAxios
      .delete(Urls.setting_Tool_RetrieveUpdateDestory(tool))
      .then(response => {
        this.getTools()
      })
      .catch(error => {
        console.log('destroyTool DELETE error', error)
      })
  },

  updateTool (updateData, tool) {
    myAxios
      .put(Urls.setting_Tool_RetrieveUpdateDestory(tool), updateData)
      .then(response => {
        generalStore.state.successMsg = '수정 완료!'
        generalStore.state.dialog.success = true
      })
      .catch(error => {
        console.log('updateTool patch error', error)
      })
  },

  createRoom (postData) {
    myAxios
      .post(Urls.setting_Room, postData)
      .then(response => {
        this.getRooms()
      })
      .catch(error => {
        console.log('createRoom POST error', error)
      })
  },

  getRooms () {
    myAxios
      .get(Urls.setting_Room)
      .then(response => {
        roomStore.state.rooms = response.data
      })
      .catch(error => {
        console.log('getRooms GET error', error)
      })
  },

  destroyRoom (room) {
    myAxios
      .delete(Urls.setting_DestroyRoom, { data: { 'room': room } })
      .then(response => {
        this.getRooms()
      })
      .catch(error => {
        console.log('destroyRoom DELETE error', error)
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
        console.log('getTimetable GET error', error)
      })
  },

  updateTimetable (postData) {
    myAxios
      .post(Urls.setting_UpdateTimetable, postData)
      .then(response => {
        generalStore.state.successMsg = '수정 완료!'
        generalStore.state.dialog.success = true
      })
      .catch(error => {
        console.log('updateTimetable POST error', error)
      })
  }

}
