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
        <v-tab to="/tool" class="indigo--text">물품 · 교구</v-tab>
        <v-tab to="/room" class="secondary--text">교실 · 장소</v-tab>
        <v-tab to="/setting">기본 설정</v-tab>
      </v-tabs>

    </v-app-bar>
  </div>
</template>

<script>
export default {
  data: () => ({
    activeTab: null
  }),

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
