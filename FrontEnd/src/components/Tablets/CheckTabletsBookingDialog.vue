<template>
  <div class="mt-1">
    <v-sheet
      v-show="dialog.checkTabletsBooking"
      outlined
    >
      <v-card class="pl-5" flat>
        <v-card-actions class="mb-3">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0">{{ formatSelectedDate }}</v-card-title>
          <v-spacer></v-spacer>

          <v-btn color="primary" class="pr-0 mr-2" @click="bookTablets">
            예약
            <v-icon left class="ml-0"> mdi-clock-plus-outline </v-icon>
          </v-btn>
        </v-card-actions>

        <v-card v-for="period in periods" :key="period" flat class="my-0 py-0">
          <v-row align="center">
            <v-col sm="3" md="3">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시<br />
                <span class="purple--text">+ {{ left[period - 1] }}대</span>
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text>
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
          <v-divider class="my-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>

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
