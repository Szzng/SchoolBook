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
          <v-row align="center" class="pa-0">
            <v-col cols="3">
              <v-card-subtitle class="py-3 black--text">
                {{ period }}교시
                <span class="purple--text">
                  + {{ left[period - 1]}}대
                </span>
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text class="">
                <v-chip-group column>
                  <v-chip
                    v-for="(item, i) in bookedTabletsLists[period]"
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
              </v-card-text>
            </v-col>
          </v-row>
          <v-divider class="my-3"></v-divider>
        </v-card>
      </v-card>
    </v-dialog>

    <BookTabletsDialog
      :focusPlace="focusPlace"
      :focusDate="focusDate"
      :left="left"
    />
    <DestroyTabletDialog
      :destroyItem="destroyItem"
      :focusPlace="focusPlace"
      :focusDate="focusDate"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookTabletsDialog from '@/components/Tablets/BookTabletsDialog.vue'
import DestroyTabletDialog from '@/components/Tablets/DestroyTabletDialog.vue'

export default {
  components: { BookTabletsDialog, DestroyTabletDialog },

  props: {
    focusDate: String,
    focusPlace: String
  },

  data: () => ({
    destroyItem: { id: '', borrower: '', quantity: '' },
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green', 'indigo']
  }),

  computed: {
    ...mapState('tabletsStore', [
      'dialog',
      'periods',
      'places',
      'bookedTabletsLists',
      'left'
    ]),

    formatSelectedDate () {
      const date = this.focusDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {
    bookTablets () {
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
