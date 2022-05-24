<template>
  <div class="pt-2">
    <v-container>
    <v-row class="fill-height mx-12 mt-10">
        <v-col cols="12">
          <v-tabs centered grow color="secondary">
            <v-tabs-slider></v-tabs-slider>
            <v-tab
              class="black--text"
              v-for="place in places"
              :key="place.name"
              :to="`/tablets/${place.name}`"
              exact
            >
              {{ place.name }}
            </v-tab>
          </v-tabs>
        </v-col>
      </v-row>
    </v-container>

    <router-view/>
  </div>
</template>

<script>
// import { mapState } from 'vuex'

export default {

  data: () => ({
    places: [
      { name: '전산실' },
      { name: '준비물실' }
    ]
  }),

  computed: {
    // ...mapState('tabletsStore', ['places']),
  }
}
</script>
