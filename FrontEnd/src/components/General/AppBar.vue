<template>
  <div>
    <v-app-bar
      app
      color="#FFFFFF"
      clipped-left
      style="border-bottom: 1px solid #d2d2d2 !important"
    >
      <a :href="`/${$store.state.generalStore.code}`">
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
        <v-tab :to="`/${$store.state.generalStore.code}`">환영합니다</v-tab>
        <v-tab :disabled="guest" :to="{ name: 'tool', params: {code: $store.state.generalStore.code} }" class="success--text"
          >물품 · 교구</v-tab
        >
        <v-tab :disabled="guest" :to="{ name: 'room', params: {code: $store.state.generalStore.code} }" class="secondary--text"
          >교실 · 장소</v-tab
        >
        <v-tab :disabled="guest" :to="{ name: 'setting', params: {code: $store.state.generalStore.code} }">기본 설정</v-tab>
      </v-tabs>

      <v-btn @click="account" class="white--text accent">
        {{ school.name }}
        <v-icon class="ml-2">mdi-town-hall</v-icon>
      </v-btn>

      <RegisterLoginDialog />
      <LogoutDialog />
    </v-app-bar>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import RegisterLoginDialog from '@/components/General/RegisterLoginDialog.vue'
import LogoutDialog from '@/components/General/LogoutDialog.vue'

export default {
  components: { RegisterLoginDialog, LogoutDialog },

  data: () => ({
    activeTab: null
  }),

  computed: {
    ...mapState('generalStore', ['dialog', 'school']),

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
        this.dialog.login = true
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
