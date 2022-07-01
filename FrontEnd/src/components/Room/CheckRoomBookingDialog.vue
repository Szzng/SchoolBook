<template>
  <div class="mt-16 pt-4 mr-10">
    <v-sheet v-show="!selected" height="520" outlined>
      <v-card class="pl-3" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0 pt-1" style="font-size: 16px">
            <span
              >달력에서<span
                class="success--text"
                style="font-size: 18px; font-weight: bold"
              >
                예약 날짜</span
              >
              또는
              <span
                class="success--text"
                style="font-size: 18px; font-weight: bold"
                >교시</span
              >
              를 선택하세요.</span
            >
          </v-card-title>
          <v-spacer></v-spacer>
        </v-card-actions>

        <v-card
          v-for="period in periods"
          :key="period"
          flat
          class="my-0 py-0"
          height="83"
        >
          <v-row align="center" justify="center">
            <v-col sm="5" md="5">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text class="py-0">
                <v-btn
                  v-if="[1, 2].includes(period)"
                  disabled
                  width="100"
                  height="40"
                  class="font-weight-bold"
                  outlined
                >
                  <v-icon class="mr-1">mdi-checkbox-marked-circle</v-icon>
                  고정시간
                </v-btn>
                <v-btn
                  v-if="[3, 4].includes(period)"
                  color="success darken-2"
                  width="100"
                  height="40"
                  class="font-weight-bold"
                  outlined
                >
                  <v-icon class="mr-1">mdi-checkbox-marked-circle</v-icon>
                  예약완료
                </v-btn>
                <v-btn
                  v-if="[5, 6].includes(period)"
                  width="100"
                  height="40"
                  outlined
                  color="primary"
                  class="font-weight-bold"
                >
                  <v-icon class="mr-1"> mdi-clock-plus-outline </v-icon>
                  예약가능
                </v-btn>
              </v-card-text>
            </v-col>
          </v-row>
          <v-divider class="my-3 ml-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>

    <v-sheet v-show="selected" height="520" outlined>
      <v-card class="pl-3" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0 pt-1"
            >{{ formatSelectedDate }}
            <v-card-subtitle class="accent--text ma-0 pa-0 pl-1 pt-2">
              {{ focusRoom }}</v-card-subtitle
            >
          </v-card-title>
          <v-spacer></v-spacer>
        </v-card-actions>

        <v-card
          v-for="period in periods"
          :key="period"
          flat
          class="my-0 py-0"
          height="83"
        >
          <v-row align="center" justify="center">
            <v-col sm="5" md="5">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text class="py-0">
                <v-btn
                  v-if="roomBookingLists[period]"
                  :disabled="disabled(roomBookingLists[period].id)"
                  color="success darken-2"
                  width="100"
                  height="40"
                  class="font-weight-bold"
                  style="font-size: 16px"
                  outlined
                  @click="assertDestroyBooking(roomBookingLists[period])"
                >
                  <v-icon class="mr-1">mdi-checkbox-marked-circle</v-icon>
                  {{ roomBookingLists[period].booker }}
                </v-btn>

                <v-btn
                  v-else
                  width="100"
                  height="40"
                  outlined
                  color="primary"
                  class="font-weight-bold"
                  @click="bookRoom(period)"
                >
                  <v-icon class="mr-1"> mdi-clock-plus-outline </v-icon>
                  예약가능
                </v-btn>
              </v-card-text>
            </v-col>
          </v-row>
          <v-divider class="my-3 ml-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>

    <BookRoomDialog />
    <DestroyRoomBookingDialog :booking="bookingToDestory" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookRoomDialog from '@/components/Room/BookRoomDialog.vue'
import DestroyRoomBookingDialog from '@/components/Room/DestroyRoomBookingDialog.vue'

export default {
  components: { BookRoomDialog, DestroyRoomBookingDialog },

  data: () => ({
    bookingToDestory: {}
  }),

  computed: {
    ...mapState('roomStore', [
      'dialog',
      'periods',
      'focusDate',
      'focusRoom',
      'roomBookingLists',
      'booking'
    ]),

    selected () {
      return this.dialog.checkRoomBooking && this.focusDate
    },

    formatSelectedDate () {
      const date = this.focusDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {
    disabled (bookingId) {
      if (bookingId === 'fixed') {
        return true
      } else {
        return false
      }
    },

    bookRoom (period) {
      this.$store.commit('roomStore/bookingSetter', {
        name: period,
        start: this.focusDate
      })

      this.dialog.bookRoom = true
    },

    assertDestroyBooking (booking) {
      this.bookingToDestory = booking
      this.dialog.destroyRoomBooking = true
    }
  }
}
</script>
