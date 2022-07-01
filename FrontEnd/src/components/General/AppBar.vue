<template>
  <div>
    <v-app-bar
      app
      color="#FFFFFF"
      clipped-left
      style="border-bottom: 1px solid #d2d2d2 !important"
    >
      <a :href="`/${code}`">
        <v-toolbar-title class="mt-1 ml-1" style="color: #7b1fa2">
          <span style="font-size: 23px">스쿨북</span>
          <v-icon large class="ml-0 mb-3" color="accent">mdi-town-hall</v-icon>
        </v-toolbar-title>
      </a>

      <v-tabs
        v-model="activeTab"
        centered
        class="pl-n12 black--text"
        color="primary"
      >
        <v-tabs-slider></v-tabs-slider>
        <v-tab :to="`/${code}`">환영합니다</v-tab>
        <v-tab :disabled="guest" :to="toolPath" class="success--text"
          >물품 · 교구</v-tab
        >
        <v-tab :disabled="guest" :to="roomPath" class="secondary--text"
          >교실 · 장소</v-tab
        >
        <v-tab :disabled="guest" :to="{ name: 'settingTool', params: {code: code} }">기본 설정</v-tab>
      </v-tabs>

      <v-btn @click="account" class="white--text accent">
        {{ school.name }}
        <v-icon class="ml-2">mdi-town-hall</v-icon>
      </v-btn>

      <RegisterDialog />
      <LogoutDialog />
    </v-app-bar>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import RegisterDialog from '@/components/General/RegisterDialog.vue'
import LogoutDialog from '@/components/General/LogoutDialog.vue'

export default {
  components: { RegisterDialog, LogoutDialog },

  data: () => ({
    activeTab: null
  }),

  computed: {
    ...mapState('generalStore', ['dialog', 'school', 'code']),
    toolPath () {
      if (this.$store.state.toolStore.tools[0]) {
        return { name: 'tool', params: {code: this.code, tool: this.$store.state.toolStore.tools[0].name} }
      } else {
        return {name: 'tools', params: {code: this.code}}
      }
    },
    roomPath () {
      if (this.$store.state.roomStore.rooms[0]) {
        return { name: 'room', params: {code: this.code, room: this.$store.state.roomStore.rooms[0].name} }
      } else {
        return {name: 'rooms', params: {code: this.code}}
      }
    },

    guest () {
      if (this.school.name === 'Guest') {
        return true
      } else {
        return false
      }
    }
  },

  methods: {
    account () {
      if (this.school.name === 'Guest') {
        this.dialog.register = true
      } else {
        this.dialog.logout = true
      }
    }
  }
}
</script>

<style scoped>
.v-tab {
  font-weight: bold;
  font-size: 1em;
}
</style>
