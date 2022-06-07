<template>
  <div class="mt-16 pt-4 mr-10">
    <v-sheet v-show="!selected" outlined min-height="512">
      <v-card class="pl-3" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0 pt-1"
            >달력에서 예약 날짜를 선택하세요.
          </v-card-title>
          <v-spacer></v-spacer>
        </v-card-actions>

        <v-card
          v-for="period in periods"
          :key="period"
          flat
          class="my-0 py-0"
          min-height="82"
        >
          <v-row align="center">
            <v-col sm="12" md="3">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시
                <span class="purple--text">+ 잔여 대수</span>
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text class="pa-0 pl-6">
                <v-chip-group column>
                 <v-chip
                    v-if="[2, 3, 4].includes(period)"
                    :color="colors[0]"
                    outlined
                  >
                    <v-avatar left>
                      <v-icon>mdi-checkbox-marked-circle</v-icon>
                    </v-avatar>
                    예약자1 (OO대)
                  </v-chip>
                  <v-chip v-if="period == 3" :color="colors[1]" outlined>
                    <v-avatar left>
                      <v-icon>mdi-checkbox-marked-circle</v-icon>
                    </v-avatar>
                    예약자2 (OO대)
                  </v-chip>
                </v-chip-group>
              </v-card-text>
            </v-col>
          </v-row>
          <v-divider class="my-3 ml-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>

    <v-sheet v-show="selected" outlined min-height="512">
      <v-card class="pl-3" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0 pt-1"
            >{{ formatSelectedDate }}
            <v-card-subtitle class="purple--text ma-0 pa-0 pl-1 pt-2">
              {{ focusTool }}</v-card-subtitle
            >
          </v-card-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" class="pr-0 mr-2" @click="bookTool">
            예약
            <v-icon left class="ml-0"> mdi-clock-plus-outline </v-icon>
          </v-btn>
        </v-card-actions>

        <v-card
          v-for="period in periods"
          :key="period"
          flat
          class="my-0 py-0"
          min-height="82"
        >
          <v-row align="center">
            <v-col sm="12" md="3">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시
                <span class="purple--text">+ {{ left[period - 1] }}대</span>
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text class="pa-0 pl-6">
                <v-chip-group column>
                  <v-chip
                    v-for="(booking, i) in toolBookingLists[period]"
                    :key="i"
                    :color="colors[period - 1]"
                    outlined
                    class="mb-0"
                    @click="assertDestroyBooking(booking)"
                  >
                    <v-avatar left>
                      <v-icon>mdi-checkbox-marked-circle</v-icon>
                    </v-avatar>
                    {{ booking.booker }} ({{ booking.quantity }}대)
                  </v-chip>
                </v-chip-group>
              </v-card-text>
            </v-col>
          </v-row>
          <v-divider class="my-3 ml-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>

    <BookToolDialog />
    <DestroyToolBookingDialog :booking="bookingToDestory" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookToolDialog from '@/components/Tool/BookToolDialog.vue'
import DestroyToolBookingDialog from '@/components/Tool/DestroyToolBookingDialog.vue'

export default {
  components: { BookToolDialog, DestroyToolBookingDialog },

  data: () => ({
    bookingToDestory: {}
  }),

  computed: {
    ...mapState('toolStore', [
      'dialog',
      'periods',
      'focusTool',
      'focusDate',
      'toolBookingLists',
      'left',
      'colors'
    ]),

    selected () {
      return this.dialog.checkToolBooking && this.focusDate
    },

    formatSelectedDate () {
      const date = this.focusDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {
    bookTool () {
      this.dialog.bookTool = true
    },

    assertDestroyBooking (booking) {
      this.bookingToDestory = booking
      this.dialog.destroyToolBooking = true
    }
  }
}
</script>
