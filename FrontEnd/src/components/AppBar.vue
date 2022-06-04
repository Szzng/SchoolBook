<template>
  <div>
    <v-app-bar
      app
      color="#FFFFFF"
      clipped-left
      style="border-bottom: 1px solid #d2d2d2 !important"
    >
      <a href="/"><v-toolbar-title>School Book</v-toolbar-title></a>

      <v-tabs
        v-model="activeTab"
        centered
        class="pl-n12 black--text"
        color="primary"
      >
        <v-tabs-slider></v-tabs-slider>
        <v-tab to="/">Home</v-tab>
        <v-tab class="indigo--text" to="/tablets">태블릿</v-tab>
        <v-tab
          class="black--text"
          v-for="place in places"
          :key="place.name"
          :to="`/classroom/${place.name}`"
          exact
          @click="changeTab(place.name)"
        >
          {{ place.name }}
        </v-tab>
        <v-tab to="/setting">기본 설정</v-tab>
      </v-tabs>
    </v-app-bar>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import classroomApi from '@/api/modules/classroom'

export default {
  data: () => ({
    activeTab: null
  }),

  mounted () {
    console.log(this.activeTab)
    this.activeTab = `/classroom/${this.$route.params.place}`
  },

  computed: {
    ...mapState('classroomStore', ['places'])
  },

  created () {
    this.activeTab = `/classroom/${this.$route.params.place}`

    this.$store.commit(
      'classroomStore/focusPlaceSetter',
      this.$route.params.place
    )
  },

  methods: {
    changeTab (tabName) {
      this.$store.commit('classroomStore/focusDateSetter', '')
      this.$store.commit('classroomStore/focusPlaceSetter', tabName)
      var today = new Date()
      var year = today.getFullYear()
      var month = ('0' + (today.getMonth() + 1)).slice(-2)
      var day = ('0' + today.getDate()).slice(-2)
      classroomApi.getAvailableBookingEvents(
        this,
        this.$route.params.place,
        year + '-' + month + '-' + day
      )
    }
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
