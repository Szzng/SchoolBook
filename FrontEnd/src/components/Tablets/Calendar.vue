<template>
  <div>
    <v-row class="fill-height mx-12 my-12">
      <v-col>
        <v-sheet height="80">
          <v-toolbar flat class="pt-2">
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

        <v-sheet height="600">
          <v-calendar
            ref="calendar"
            v-model="focus"
            :weekdays="weekday"
            color="primary"
            type="month"
            @click:date="checkTabletsBooking"
          ></v-calendar>
        </v-sheet>
      </v-col>
    </v-row>
    <CheckTabletsBookingDialog :selectedDate="focus" />
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
    focus: '',
    weekday: [1, 2, 3, 4, 5]
  }),

  computed: {
    ...mapState('bookStore', ['dialog'])
  },

  async created () {
    await this.$nextTick()
    this.initCalendarTitle = this.$refs.calendar.title
  },

  methods: {
    checkTabletsBooking ({ date }) {
      this.focus = date
      api.getBookedTabletsListByDate(date)
      this.dialog.checkTabletsBooking = true
    },
    setToday () {
      this.focus = ''
    }
  }
}
</script>
