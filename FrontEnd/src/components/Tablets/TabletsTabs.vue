<template>
  <div class="pt-2">
    <v-container>
      <v-row class="fill-height mx-12 mt-10">
        <v-col cols="12">
          <v-tabs v-model="activeTab" centered grow color="secondary">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="black--text"
              v-for="place in places"
              :key="place.name"
              :to="`/tablets/${place.name}`"
              exact
              @click="changeTab(place.name)"
            >
              {{ place.name }}
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
    this.activeTab = `/tablets/${this.$route.params.place}`
  },

  computed: {
    ...mapState('tabletsStore', ['places'])
  },

  created () {
    this.$store.commit(
      'tabletsStore/focusPlaceSetter',
      this.$route.params.place
    )
  },

  methods: {
    changeTab (tabName) {
      this.$store.commit('tabletsStore/focusDateSetter', '')
      this.$store.commit('tabletsStore/focusPlaceSetter', tabName)
    }
  }
}
</script>
