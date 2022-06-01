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
        <v-tab to="/">Home</v-tab>
        <v-tab class="indigo--text" to="/tablets">태블릿 예약</v-tab>
        <v-tab
          class="black--text"
          v-for="place in places"
          :key="place.name"
          :to="`/classroom/${place.name}`"
          >{{ place.name }}</v-tab
        >
        <v-tab to="/setting">기본 설정</v-tab>
      </v-tabs>

      <v-spacer></v-spacer>
    </v-app-bar>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: () => ({}),

  computed: {
    ...mapState('classroomStore', ['places'])
  },

  methods: {}
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
