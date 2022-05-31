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
              :to="`/classroom/computer/${tab.name}`"
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
    tabs: [{ name: '컴퓨터실1' }, { name: '컴퓨터실2' }]
  }),

  mounted () {
    this.activeTab = `/classroom/computer/${this.$route.params.place}`
  },

  computed: {},

  created () {
    this.$store.commit(
      'classroomStore/focusPlaceSetter',
      this.$route.params.place
    )
  },

  methods: {
    changeTab (tabName) {
      this.$store.commit('classroomStore/focusDateSetter', '')
      this.$store.commit('classroomStore/focusPlaceSetter', tabName)
    }
  }
}
</script>
