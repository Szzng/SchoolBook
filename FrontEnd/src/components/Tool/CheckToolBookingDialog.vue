<template>
  <div>
    <div v-show="!selected">
      <v-sheet height="10vh">
        <v-toolbar flat>
          <v-spacer></v-spacer>
          <v-toolbar-title class="pl-0 pt-1"
            >달력에서 예약 날짜를 선택하세요.
          </v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-sheet>

      <v-sheet outlined min-height="68vh">
        <v-row class="mx-1 mt-3">
          <v-col cols="6" v-for="period in periods" :key="period" class="my-1">
            <v-card flat min-height="14vh">
              <v-row align="center" justify="center">
                <v-col cols="3" class="px-0 text-center">
                  <v-card-subtitle class="black--text">
                    {{ period }}교시 <br />
                    <span class="accent--text">+잔여 수량</span>
                  </v-card-subtitle>
                </v-col>

                <v-col cols="9" class="px-3 pt-0">
                  <v-chip-group column>
                    <v-chip
                      v-if="[2, 3, 4, 5, 6, 7].includes(period)"
                      :color="colors[0]"
                      outlined
                    >
                      <v-avatar left>
                        <v-icon>mdi-checkbox-marked-circle</v-icon>
                      </v-avatar>
                      예약자1 (O대)
                    </v-chip>
                    <v-chip
                      v-if="[3, 4, 5].includes(period)"
                      :color="colors[1]"
                      outlined
                    >
                      <v-avatar left>
                        <v-icon>mdi-checkbox-marked-circle</v-icon>
                      </v-avatar>
                      예약자2 (O대)
                    </v-chip>
                    <v-chip v-if="period == 5" :color="colors[2]" outlined>
                      <v-avatar left>
                        <v-icon>mdi-checkbox-marked-circle</v-icon>
                      </v-avatar>
                      예약자3 (O대)
                    </v-chip>
                  </v-chip-group>
                </v-col>
              </v-row>
              <v-divider class="mx-5 mt-2"></v-divider>
            </v-card>
          </v-col>
        </v-row>
      </v-sheet>
    </div>

    <div v-show="selected">
      <v-sheet height="10vh">
        <v-toolbar flat>
          <v-btn disabled text x-large class="pl-3 mt-2">
            {{ focusTool }}
          </v-btn>

          <v-spacer></v-spacer>

          <v-toolbar-title class="pl-0 pt-1"
            >{{ formatSelectedDate }}
          </v-toolbar-title>

          <v-spacer></v-spacer>

          <v-btn color="primary" class="pr-0 mr-2" @click="bookTool">
            예약
            <v-icon left class="ml-0"> mdi-clock-plus-outline </v-icon>
          </v-btn>
        </v-toolbar>
      </v-sheet>

      <v-sheet outlined min-height="68vh">
        <v-row class="mx-1 mt-3">
          <v-col cols="6" v-for="period in periods" :key="period" class="my-1">
            <v-card flat min-height="14vh">
              <v-row align="center" justify="center">
                <v-col cols="3" class="px-0 text-center">
                  <v-card-subtitle class="black--text">
                    {{ period }}교시 <br />
                    <span class="accent--text">+{{ left[period - 1] }}대</span>
                  </v-card-subtitle>
                </v-col>

                <v-col cols="9" class="px-3 pt-0">
                  <v-chip-group column>
                    <v-chip
                      v-for="(booking, i) in toolBookingLists[period]"
                      :key="i"
                      :color="colors[i]"
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
                </v-col>
              </v-row>
              <v-divider class="mx-5 mt-2"></v-divider>
            </v-card>
          </v-col>
        </v-row>
      </v-sheet>
    </div>

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
