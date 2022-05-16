<template>
  <div>
    <v-dialog
      v-model="dialog.checkTabletsBooking"
      max-width="600"
      content-class="check-booking-dialog"
    >
      <v-card class="pl-2">
        <v-card-actions>
          <v-card-title class="pl-0">{{ formatSelectedDate }}</v-card-title>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            class="pr-0 mr-0"
            text
            x-large
            @click="book"
          >
            예약
            <v-icon left class="ml-0"> mdi-clock-plus-outline </v-icon>
          </v-btn>
        </v-card-actions>

        <v-card v-for="period in periods" :key="period" flat class="my-0 py-0">
          <v-card-subtitle class="py-3 black--text"
            >{{ period }}교시</v-card-subtitle
          >
          <v-card-text class="pa-0">
            <v-row
              v-for="(arrayByPlaces, j) in bookedTabletsLists[period]"
              :key="j"
              class="ml-2"
              align="center"
            >
              <v-col cols="3" class="ml-2 indigo--text">
                {{ places[j] }} + 대
              </v-col>
              <v-col>
                <v-chip-group column>
                  <v-chip
                    v-for="(item, i) in arrayByPlaces"
                    :key="i"
                    :color="colors[i]"
                    outlined
                    class="white--text"
                  >
                    <v-avatar left>
                      <v-icon>mdi-checkbox-marked-circle</v-icon>
                    </v-avatar>
                    {{ item.borrower }} ({{ item.quantity }}대)
                  </v-chip>
                </v-chip-group>
              </v-col>
            </v-row>
          </v-card-text>
          <!-- </v-col>
          </v-row> -->

          <v-divider class="my-3"></v-divider>
        </v-card>
      </v-card>
      <!-- {{bookedTabletsLists[Object.keys(bookedTabletsLists)[0]].전산실}} -->
    </v-dialog>

    <BookTabletsDialog :selectedDate="selectedDate" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookTabletsDialog from '@/components/Tablets/BookTabletsDialog.vue'

export default {
  components: { BookTabletsDialog },

  props: {
    selectedDate: String
  },

  data: () => ({
    periods: [1, 2, 3, 4, 5, 6],
    places: ['전산실', '준비물실'],
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green']
  }),

  computed: {
    ...mapState('bookStore', ['dialog', 'bookedTabletsLists']),

    formatSelectedDate () {
      const date = this.selectedDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {
    book () {
      this.dialog.bookTablets = true
    }
  }
}
</script>

<style scoped>
>>> .check-booking-dialog {
  position: absolute;
  left: 0;
}
</style>
