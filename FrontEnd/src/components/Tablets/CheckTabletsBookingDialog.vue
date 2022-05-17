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

          <v-btn color="primary" class="pr-0 mr-0" @click="book">
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

    <v-dialog v-model="showDestroyDialog" max-width="400" persistent>
      <v-card>
        <v-row align="center" justify="center">
          <v-chip color="red darken-2" class="white--text mt-10">
            <v-avatar left>
              <v-icon>mdi-close-circle-outline</v-icon>
            </v-avatar>
            {{ destroyItem.borrower }} ({{ destroyItem.quantity }}대)
          </v-chip>
        </v-row>
        <v-row
          align="center"
          justify="center"
          class="mt-8 mb-6"
          :style="{ fontSize: '18px' }"
        >
          정말 예약을 취소하시겠어요?
        </v-row>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" class="white--text" @click="destroyBooking"
            >예약 취소하기</v-btn
          >
          <v-btn @click="showDestroyDialog = false">아니요</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <BookTabletsDialog :selectedDate="selectedDate" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookTabletsDialog from '@/components/Tablets/BookTabletsDialog.vue'
import api from '@/api/modules/tablets'

export default {
  components: { BookTabletsDialog },

  props: {
    selectedDate: String
  },

  data: () => ({
    showDestroyDialog: false,
    destroy: false,
    destroyItem: '',
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green', 'indigo']
  }),

  computed: {
    ...mapState('bookStore', [
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

    book () {
      this.dialog.bookTablets = true
    },

    assertDestroyBooking (item) {
      this.destroyItem = item
      console.log(this.destroyId)
      this.showDestroyDialog = true
    },

    destroyBooking () {
      api.DestroyBookedTablets(this.destroyItem.id, this.selectedDate)
      this.showDestroyDialog = false
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
