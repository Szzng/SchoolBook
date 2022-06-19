import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

const opts = {
  theme: {
    themes: {
      light: {
        primary: '#BA68C8',
        secondary: '#C2185B',
        accent: '#7B1FA2',
        error: '#FF5252',
        // info: '#7B1FA2',
        success: '#3F51B5',
        warning: '#F29930'
      }
    }
  },
  icons: {
    iconfont: 'mdi'
  }
}

export default new Vuetify(opts)
