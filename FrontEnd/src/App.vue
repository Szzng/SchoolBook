<template>
  <v-app id="inspire">
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <AppBar />
    <router-view/>
  </v-app>
</template>

<script>
import AppBar from './components/General/AppBar.vue'
import api from '@/api/modules/accounts'
import generalStore from '@/store/modules/generalStore'

export default {
  name: 'App',

  components: {
    AppBar
  },

  created () {
    if (this.$route.params.code) {
      api.login(this.$route.params.code)
      generalStore.state.code = this.$route.params.code
    }
  },

  watch: {
    '$route' (to, from) {
      generalStore.state.code = to.params.code
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

a {
  text-decoration: none;
  font-weight: bold;
}
a:hover {
  color: #d4525d;
}
</style>
