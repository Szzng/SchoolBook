<template>
  <div>
    <v-dialog
      v-model="dialog.checkTabletsBooking"
      max-width="700"
      content-class="check-booking-dialog"
    >
      <v-card class="pl-2">
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-card-title class="pl-0">{{ formatSelectedDate }}</v-card-title>
          <v-spacer></v-spacer>

          <v-btn color="primary" class="pr-0 mr-0" @click="bookTablets">
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
              v-for="place in Object.keys(places)"
              :key="place"
              class="ml-2"
              align="center"
            >
              <v-col cols="3" class="ml-2 purple--text">
                {{ place }} + {{ getLeft(period, place) }}대
              </v-col>
              <v-col>
                <v-chip-group column>
                  <v-chip
                    v-for="(item, i) in getListsByPeriodPlace(period, place)"
                    :key="i"
                    :color="colors[i]"
                    outlined
                    class="white--text"
                    @click="assertDestroyBooking(item)"
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
          <v-divider class="my-3"></v-divider>
        </v-card>
      </v-card>
    </v-dialog>

    <BookTabletsDialog :selectedDate="selectedDate" :left="left" />
    <DestroyTabletDialog :destroyItem="destroyItem" :selectedDate="selectedDate"/>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookTabletsDialog from '@/components/Tablets/BookTabletsDialog.vue'
import DestroyTabletDialog from '@/components/Tablets/DestroyTabletDialog.vue'
import api from '@/api/modules/tablets'

export default {
  components: { BookTabletsDialog, DestroyTabletDialog },

  props: {
    selectedDate: String
  },

  data: () => ({
    left: {},
    destroyItem: {id: '', borrower: '', quantity: ''},
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green', 'indigo']
  }),

  computed: {
    ...mapState('tabletsStore', [
      'dialog',
      'periods',
      'places',
      'bookedTabletsLists'
    ]),

    formatSelectedDate () {
      const date = this.selectedDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {

    getListsByPeriodPlace (period, place) {
      let a = this.bookedTabletsLists[period]
      if (a) {
        return a[place].classes
      }
    },

    getLeft (period, place) {
      let a = this.bookedTabletsLists[period]
      if (a) {
        return a[place].left
      } else {
        return this.places[place]
      }
    },

    bookTablets () {
      this.left = api.getLeftTabletsCounts(this, this.selectedDate)
      this.dialog.bookTablets = true
    },

    assertDestroyBooking (item) {
      this.destroyItem = item
      this.dialog.destroyTablet = true
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
