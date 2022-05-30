<template>
  <div>
    <v-app-bar
      app
      color="#FFFFFF"
      clipped-left

      style="border-bottom: 1px solid #d2d2d2 !important"
    >
      <a href="/"><v-toolbar-title>School Book</v-toolbar-title></a>

      <v-tabs centered class="pl-n12 black--text" color="primary">
        <v-tabs-slider></v-tabs-slider>
        <v-tab
          class="black--text"
          v-for="menu in menus"
          :key="menu.name"
          :to="menu.url"
          >{{ menu.name }}</v-tab
        >
      </v-tabs>

      <v-spacer></v-spacer>

    </v-app-bar>
  </div>
</template>

<script>

export default {

  data: () => ({
    menus: [
      { name: 'Home', url: '/' },
      { name: '태블릿', url: '/tablets' },
      { name: '컴퓨터실', url: '/classroom/computer' },
      { name: '기본 설정', url: '/setting' }
    ],
    notifications: 1
  }),

  computed: {
  },

  methods: {
  }
}
</script>

<style scoped>
.v-dialog .v-text-field--outlined >>> fieldset {
  border-color: #b4b4b4;
  border-width: 1px;
}

.v-tab,
.v-dialog .v-btn {
  font-weight: bold;
  font-size: 1em;
}
</style>
