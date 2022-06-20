<template>
  <div class="pt-2">
    <v-container>
      <v-row class="fill-height mx-12 mt-10">
        <v-col cols="12">
          <v-tabs v-model="activeTab" centered grow color="success">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="success--text"
              v-for="tool in tools"
              :key="tool.name"
              :to="`/tool/${tool.name}`"
              exact
              @click="changeTab(tool.name)"
            >
              {{ tool.name }}
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

export default {
  data: () => ({
    activeTab: null
  }),

  mounted () {
    this.activeTab = `/tool/${this.$route.params.tool}`
  },

  created () {
    this.activeTab = `/tool/${this.$route.params.tool}`
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
