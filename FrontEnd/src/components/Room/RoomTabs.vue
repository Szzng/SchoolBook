<template>
  <div class="pt-2">
    <v-container>
      <v-row class="fill-height mx-12 mt-10">
        <v-col cols="12">
          <v-tabs v-model="activeTab" centered grow color="secondary">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="secondary--text"
              v-for="room in rooms"
              :key="room.name"
              :to="{path: `/${$store.state.generalStore.code}/room/${room.name}`}"
              exact
              @click="changeTab(room.name)"
            >
              {{ room.name }}
            </v-tab>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>

    <router-view />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/room'

export default {
  data: () => ({
    activeTab: null
  }),

  computed: {
    ...mapState('roomStore', ['rooms'])
  },

  created () {
    this.activeTab = `/${this.$store.state.generalStore.code}/room/${this.$route.params.room}`
    this.$store.commit('roomStore/focusRoomSetter', this.$route.params.room)
  },

  methods: {
    changeTab (roomName) {
      this.$store.commit('roomStore/focusDateSetter', '')
      this.$store.commit('roomStore/focusRoomSetter', roomName)

      var today = new Date()
      var year = today.getFullYear()
      var month = ('0' + (today.getMonth() + 1)).slice(-2)
      var day = ('0' + today.getDate()).slice(-2)
      api.getAvailableEvents(roomName, year + '-' + month + '-' + day)
    }
  }
}
</script>
