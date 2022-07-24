<template>
  <div class="pt-2">
    <v-sheet class="mx-12" v-if="tools.length > 0">
      <v-row class="fill-height mx-10 mt-16 mb-8">
          <v-tabs v-model="activeTab" centered grow color="success" class="mx-12">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="success--text"
              v-for="tool in tools"
              :key="tool.name"
              :to="{
                path: `/${$store.state.generalStore.code}/tool/${tool.name}`,
              }"
              exact
              @click="changeTab(tool.name)"
            >
              {{ tool.name }}
            </v-tab>
          </v-tabs>
      </v-row>

      <router-view />

    </v-sheet>

    <v-container v-else class="mt-16">
      <v-card class="mt-10" flat>
        <v-row align="center" justify="center">
          <v-card-title style="font-size: 30px">
            <strong> {{ $store.state.generalStore.school.name }}</strong
            >의 등록된 물품 · 교구가 없습니다.
            <v-icon x-large class="ml-2" color="black">mdi-tab-search</v-icon>
          </v-card-title>

          <v-card-title style="font-size: 30px">
            <router-link
              :to="{
                name: 'settingTool',
                params: { code: $store.state.generalStore.code },
              }"
              >기본 설정</router-link
            >에서 물품 · 교구를 등록하고 관리해보세요.
          </v-card-title>
        </v-row>
        <v-img src="/static/images/empty.png" contain aspect-ratio="2.8" class="mt-16"></v-img>
      </v-card>
    </v-container>

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: () => ({
    activeTab: null
  }),

  created () {
    this.activeTab = `/${this.$store.state.generalStore.code}/tool/${this.$route.params.tool}`
    this.$store.commit('toolStore/focusToolSetter', this.$route.params.tool)
  },

  computed: {
    ...mapState('toolStore', ['tools'])
  },

  methods: {
    changeTab (tabName) {
      this.$store.commit('toolStore/focusDateSetter', '')
      this.$store.commit('toolStore/focusToolSetter', tabName)
    }
  }
}
</script>

<style scoped>
</style>
