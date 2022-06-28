<template>
  <v-app id="inspire">
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <AppBar />
    <router-view/>
    <ErrorDialog/>
    <SuccessDialog/>
  </v-app>
</template>

<script>
import AppBar from './components/General/AppBar.vue'
import ErrorDialog from './components/General/ErrorDialog.vue'
import SuccessDialog from './components/General/SuccessDialog.vue'
import api from '@/api/modules/accounts'

export default {
  name: 'App',

  components: {
    AppBar,
    ErrorDialog,
    SuccessDialog
  },

  created () {
    if (this.$route.params.code) {
      this.$store.state.generalStore.code = this.$route.params.code
      api.login(this.$route.params.code)
    }
  },

  watch: {
    '$route' (to, from) {
      this.$store.state.generalStore.code = to.params.code
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
