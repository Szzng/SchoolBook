<template>
  <div>
    <v-app-bar
      app
      color="#FFFFFF"
      clipped-left
      style="border-bottom: 1px solid #d2d2d2 !important"
    >
      <a href="/"><v-toolbar-title style="color:#7B1FA2;">School Book</v-toolbar-title></a>

      <v-tabs
        v-model="activeTab"
        centered
        class="pl-n12 black--text"
        color="primary"
      >
        <v-tabs-slider></v-tabs-slider>
        <v-tab to="/">Home</v-tab>
        <v-tab to="/tool" class="success--text">물품 · 교구</v-tab>
        <v-tab to="/room" class="secondary--text">교실 · 장소</v-tab>
        <v-tab to="/setting/tool">기본 설정</v-tab>
      </v-tabs>

      <v-btn @click="dialog.school = true" class="white--text accent">
        {{ school.name }}
        <v-icon class="ml-2">mdi-town-hall</v-icon>
      </v-btn>

      <SchoolDialog />
    </v-app-bar>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import SchoolDialog from '@/components/General/SchoolDialog.vue'

export default {
  components: { SchoolDialog },

  data: () => ({
    activeTab: null
  }),

  computed: {
    ...mapState('generalStore', ['dialog', 'school'])
  },

  mounted () {
    console.log(this.activeTab)
  }
}
</script>

<style scoped>
.v-tab {
  font-weight: bold;
  font-size: 1em;
}
</style>
