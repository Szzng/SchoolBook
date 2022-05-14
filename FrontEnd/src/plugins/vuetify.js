import '@mdi/font/css/materialdesignicons.css'
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

const opts = {
  theme: {
    themes: {
      light: {
        primary: '#589290',
        secondary: '#D4525D',
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
