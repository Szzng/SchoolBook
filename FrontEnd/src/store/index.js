import Vue from 'vue'
import Vuex from 'vuex'
import tabletsStore from './modules/tabletsStore'
import roomStore from './modules/roomStore'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    tabletsStore,
    roomStore
  }
})
