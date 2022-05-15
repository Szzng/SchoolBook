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

        <v-card
          v-for="list in bookedTabletsLists"
          :key="list.period"
          flat
          class="my-0 py-0"
        >
          <v-card-subtitle class="py-3 black--text">
            {{ list.period }}교시</v-card-subtitle
          >
          <v-row
            v-for="place in list.place"
            :key="place.name"
            align="center"
            class="ml-2"
          >
            <v-col cols="3" class="ml-2 indigo--text">
              {{ place.name }} + {{ place.left }}대
            </v-col>
            <v-col>
              <v-card-text class="pa-0">
                <v-chip-group column>
                  <v-chip
                    v-for="(item, i) in place.classes"
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
              </v-card-text>
            </v-col>
          </v-row>
          <v-divider class="my-3"></v-divider>
        </v-card>
      </v-card>
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
    selectedDate: String,
    bookedTabletsLists: Array
  },

  data: () => ({
    periods: [1, 2, 3, 4, 5, 6],
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green']
  }),

  computed: {
    ...mapState('bookStore', ['dialog']),
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
