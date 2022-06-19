import Vue from 'vue'
import Vuex from 'vuex'
import toolStore from './modules/toolStore'
import roomStore from './modules/roomStore'
import generalStore from './modules/generalStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    toolStore,
    roomStore,
    generalStore
  }
})
