import Vue from 'vue'
import Vuex from 'vuex'
import tabletsStore from './modules/tabletsStore'
import classroomStore from './modules/classroomStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    tabletsStore,
    classroomStore
  }
})
