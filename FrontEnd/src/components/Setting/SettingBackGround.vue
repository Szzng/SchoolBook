<template>
  <div class="pt-2">
    <v-container>
      <v-row class="fill-height mx-12 mt-10">
        <v-col cols="12">
          <v-tabs v-model="activeTab" centered grow color="secondary">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="black--text"
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
      { name: '태블릿 예약 설정', path: 'tablets' },
      { name: '교실(장소) 예약 설정', path: 'classroom' }
    ]
  }),

  mounted () {
    this.activeTab = `/setting/${this.tabs.path}`
  },

  methods: {
    changeTab (tabName) {
    }
  }
}
</script>
