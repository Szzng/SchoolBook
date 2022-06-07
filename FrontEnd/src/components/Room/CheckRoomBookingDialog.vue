<template>
  <div class="mt-16 pt-4 mr-10">
    <v-sheet v-show="!selected" height="520" outlined>
      <v-card class="pl-3" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0 pt-1" style="font-size: 16px">
            <span
              >달력에서<span
                class="indigo--text"
                style="font-size: 18px; font-weight: bold"
              >
                예약 날짜</span
              >
              또는
              <span
                class="indigo--text"
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
            <v-col sm="12" md="5">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text class="py-0">
                <v-btn
                  v-if="[1, 2, 3].includes(period)"
                  color="black"
                  width="100"
                  height="40"
                  class="font-weight-bold"
                  outlined
                  disabled
                >
                  <v-icon class="mr-1">mdi-checkbox-marked-circle</v-icon>
                  예약완료
                </v-btn>
                <v-btn v-else width="100" height="40" outlined color="primary">
                  <v-icon class="mr-1"> mdi-clock-plus-outline </v-icon>
                  예약
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
            <v-card-subtitle class="purple--text ma-0 pa-0 pl-1 pt-2">
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
            <v-col sm="12" md="5">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text class="py-0">
                <v-btn
                  v-if="roomBookingLists[period]"
                  color="black"
                  width="100"
                  height="40"
                  class="font-weight-bold"
                  style="font-size: 16px"
                  outlined
                  disabled
                  @click="assertDestroyBooking(item)"
                >
                  <v-icon class="mr-1">mdi-checkbox-marked-circle</v-icon>
                  {{ roomBookingLists[period] }}
                </v-btn>

                <v-btn
                  v-else
                  width="100"
                  height="40"
                  outlined
                  color="primary"
                  @click="bookRoom(period)"
                >
                  <v-icon class="mr-1"> mdi-clock-plus-outline </v-icon>
                  예약
                </v-btn>
              </v-card-text>
            </v-col>
          </v-row>
          <v-divider class="my-3 ml-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>

    <BookRoomDialog />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookRoomDialog from '@/components/Room/BookRoomDialog.vue'

export default {
  components: { BookRoomDialog },

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
    bookRoom (period) {
      this.$store.commit('roomStore/bookingSetter', {
        name: period,
        start: this.focusDate
      })

      this.dialog.bookRoom = true
    }
  }
}
</script>
