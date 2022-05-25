<template>
  <div class="mt-2 mr-10">
    <v-sheet v-show="!selected" outlined height="603">
      <v-card class="pl-5" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0 pt-1"
            >달력에서 예약 날짜를 선택하세요.
          </v-card-title>
          <v-spacer></v-spacer>
        </v-card-actions>

        <v-card v-for="period in periods" :key="period" flat class="my-0 py-0">
          <v-row align="center">
            <v-col sm="3" md="3">
              <v-card-subtitle class="pb-0 black--text">
                {{ period }}교시<br />
                <span class="purple--text">+ 잔여 대수</span>
              </v-card-subtitle>
            </v-col>

            <v-col class="pa-0">
              <v-card-text>
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

    <v-sheet v-show="selected" outlined>
      <v-card class="pl-5" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
          <v-card-title class="pl-0 pt-1"
            >{{ formatSelectedDate }}
            <v-card-subtitle class="purple--text ma-0 pa-0 pl-1 pt-2">
              {{ focusPlace }}</v-card-subtitle
            >
          </v-card-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" class="pr-0 mr-1" @click="bookTablets">
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
          <v-divider class="my-3 ml-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>

    <BookTabletsDialog />
    <DestroyTabletDialog :destroyItem="destroyItem" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookTabletsDialog from '@/components/Tablets/BookTabletsDialog.vue'
import DestroyTabletDialog from '@/components/Tablets/DestroyTabletDialog.vue'

export default {
  components: { BookTabletsDialog, DestroyTabletDialog },

  data: () => ({
    destroyItem: {},
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green', 'indigo']
  }),

  computed: {
    ...mapState('tabletsStore', [
      'dialog',
      'periods',
      'focusPlace',
      'focusDate',
      'bookedTabletsLists',
      'left'
    ]),

    selected () {
      return this.dialog.checkTabletsBooking && this.focusDate
    },

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
