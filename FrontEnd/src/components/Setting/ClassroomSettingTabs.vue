<template>
  <div class="pt-0">
    <v-container>
      <v-row class="fill-height mx-12">
        <v-col cols="12">
          <v-tabs v-model="activeTab" centered color="indigo">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="black--text px-16"
              v-for="tab in tabs"
              :key="tab.name"
              :to="tab.path"
              exact
              @click="changeTab(tab.name)"
            >
              {{ tab.name }}
            </v-tab>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>

    <router-view />
  </div>
</template>

<script>
export default {
  data: () => ({
    activeTab: null,
    tabs: [
      { name: '교실(장소) 설정', path: 'place' },
      { name: '고정 시간표 설정', path: 'fixtimetable' }
    ]
  }),

  mounted () {
    this.activeTab = `/setting/classroom/${this.tabs.path}`
  },

  methods: {
    changeTab (tabName) {
    }
  }
}
</script>
