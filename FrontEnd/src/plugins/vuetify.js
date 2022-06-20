import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

const opts = {
  theme: {
    themes: {
      light: {
        primary: '#BA68C8', // purple lighten-2
        secondary: '#C2185B', // pink darken-2
        accent: '#7B1FA2', // purple darken-2
        error: '#FF1744', // red accent-3
        info: '#616161', // grey darken-2
        success: '#3F51B5', // indigo
        warning: '#F57C00' // orange darken-2
      }
    }
  },
  icons: {
    iconfont: 'mdi'
  }
}

export default new Vuetify(opts)
