<template>
  <div class="pt-2">
    <v-container v-if="rooms.length > 0">
      <v-row class="fill-height mx-12 mt-10">
        <v-col cols="12">
          <v-tabs v-model="activeTab" centered grow color="secondary">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="secondary--text"
              v-for="room in rooms"
              :key="room.name"
              :to="{
                path: `/${$store.state.generalStore.code}/room/${room.name}`,
              }"
              exact
              @click="changeTab(room.name)"
            >
              {{ room.name }}
            </v-tab>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>

    <v-container v-else class="mt-16">
      <v-card class="mt-10" flat>
        <v-row align="center" justify="center">
          <v-card-title style="font-size: 30px">
            <v-icon x-large class="mr-2">mdi-google-classroom</v-icon>
            등록된 교실 · 장소가 없습니다.
            <v-icon x-large class="ml-2">mdi-google-classroom</v-icon>
          </v-card-title>

          <v-card-title style="font-size: 30px">
            <router-link
              :to="{
                name: 'settingRoom',
                params: { code: $store.state.generalStore.code },
              }"
              >기본 설정</router-link
            >에서 교실 · 장소를 등록하고 관리해보세요.
          </v-card-title>
        </v-row>
      </v-card>
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
