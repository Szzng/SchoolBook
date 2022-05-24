<template>
  <div>
    <v-row class="fill-height mx-12">
      <v-col sm="12" md="6">
        <v-sheet height="80">
          <v-toolbar flat class="pt-0">
            <v-spacer></v-spacer>
            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click="$refs.calendar.prev()"
              ><v-icon small> mdi-chevron-left </v-icon>
            </v-btn>
            <v-toolbar-title v-if="$refs.calendar">
              {{ $refs.calendar.title }}
            </v-toolbar-title>
            <v-toolbar-title v-else>
              {{ initCalendarTitle }}
            </v-toolbar-title>
            <v-btn
              fab
              text
              small
              color="grey darken-2"
              @click="$refs.calendar.next()"
              ><v-icon small> mdi-chevron-right </v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              outlined
              class="mr-0"
              color="grey darken-2"
              @click="setToday"
            >
              Today
            </v-btn>
          </v-toolbar>
        </v-sheet>

        <v-sheet height="530">
          <v-calendar
            ref="calendar"
            v-model="focusDate"
            :weekdays="weekday"
            color="primary"
            type="month"
            @click:date="checkTabletsBooking"
          ></v-calendar>
        </v-sheet>
      </v-col>

      <v-col sm="12" md="6">
         <CheckTabletsBookingDialog :focusDate="focusDate" :focusPlace="focusPlace"/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import CheckTabletsBookingDialog from '@/components/Tablets/CheckTabletsBookingDialog.vue'
import { mapState } from 'vuex'
import api from '@/api/modules/tablets'

export default {
  components: { CheckTabletsBookingDialog },

  data: () => ({
    initCalendarTitle: '',
    focusDate: '',
    focusPlace: '',
    weekday: [1, 2, 3, 4, 5]
    // events: [
    //   {
    //     name: '38 & 20',
    //     start: '2022-05-10'},
    //   {
    //     name: '38 & 20',
    //     start: '2022-05-10'},
    //   {
    //     name: '38 & 20',
    //     start: '2022-05-10'}]
  }),

  computed: {
    ...mapState('tabletsStore', ['dialog'])
  },

  async created () {
    await this.$nextTick()
    this.initCalendarTitle = this.$refs.calendar.title
  },

  methods: {
    checkTabletsBooking ({ date }) {
      this.focusPlace = this.$route.params.place
      this.focusDate = date
      api.getBookedTabletsListByDate(this.focusPlace, this.focusDate)
      api.getLeftTabletsCounts(this.focusPlace, this.focusDate)
      this.dialog.checkTabletsBooking = true
    },
    setToday () {
      this.focusDate = ''
    }
  }
}
</script>
