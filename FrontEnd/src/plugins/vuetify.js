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
        accent: '#54B1CE',
        error: '#F4512D',
        info: '#5067B7',
        success: '#51C169',
        warning: '#F29930'
      }
    }
  },
  icons: {
    iconfont: 'mdi'
  }
}

export default new Vuetify(opts)
