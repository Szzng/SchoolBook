<template>
  <v-app id="inspire">
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <AppBar />
    <router-view/>
  </v-app>
</template>

<script>
import AppBar from './components/AppBar.vue'

export default {
  name: 'App',

  components: {
    AppBar
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
