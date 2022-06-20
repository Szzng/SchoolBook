// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import vuetify from '@/plugins/vuetify'
import App from './App'
import router from './router'
import store from './store'
import settingApi from '@/api/modules/setting'
import accountsApi from '@/api/modules/accounts'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  vuetify,
  el: '#inspire',
  router,
  store,
  beforeCreate () {
    settingApi.getRooms()
    settingApi.getTools()
    accountsApi.getSchoolDetail()
  },
  components: { App },
  template: '<App/>'
}).$mount('#inspire')
