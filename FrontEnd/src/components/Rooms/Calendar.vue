<template>
  <div>
    <v-row class="fill-height mx-12 my-16">
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
            :events="notYetBooked"
            :event-more="false"
            :weekdays="weekday"
            color="primary"
            type="month"
            @click:date="checkRoomBooking"
            @click:event="bookRoom"
          ></v-calendar>
        </v-sheet>
      </v-col>
    </v-row>
    <CheckRoomBookingDialog :selectedDate="focus" />
    <BookRoomDialog :eventBooking="eventBooking"/>
    <DestroyRoomBookingDialog :eventDestroying="eventDestroying" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CheckRoomBookingDialog from '@/components/Rooms/CheckRoomBookingDialog.vue'
import BookRoomDialog from '@/components/Rooms/BookRoomDialog.vue'
import DestroyRoomBookingDialog from '@/components/Rooms/DestroyRoomBookingDialog.vue'
// import api from '@/api/modules/room'

export default {
  components: { CheckRoomBookingDialog, BookRoomDialog, DestroyRoomBookingDialog },

  data: () => ({
    initCalendarTitle: '',
    focus: '',
    eventBooking: {},
    eventDestroying: {},
    weekday: [1, 2, 3, 4, 5],
    notYetBooked: [
      {
        name: '1교시',
        start: '2022-05-18' },
      {
        name: '2교시',
        start: '2022-05-18' },
      {
        name: '3교시',
        start: '2022-05-18' },
      {
        name: '4교시',
        start: '2022-05-18' },
      {
        name: '5교시',
        start: '2022-05-18' },
      {
        name: '6교시',
        start: '2022-05-18' }
    ]
  }),

  created () {
    // api.getBookedRoomLists()
  },

  computed: {
    ...mapState('roomStore', ['dialog', 'bookedRoomLists'])
  },
  methods: {
    checkRoomBooking ({ date }) {
      this.focus = date
      // api.getBookedTabletsListByDate(date)
      this.dialog.checkRoomBooking = true
    },

    bookRoom ({nativeEvent, event}) {
      this.eventBooking = event
      this.dialog.bookRoom = true
    },

    assertDestroyRoomBooking ({nativeEvent, event}) {
      this.eventDestroying = event
      this.dialog.destroyRoomBooking = true
    },

    getEventName (event) {
      return event.input.name
    },
    getEventColor (event) {
      return event.color
    },
    setToday () {
      this.focus = ''
    },
    formatInterval (interval) {
      return interval.time[1] + '교시'
    },
    showInterval (interval) {
      return true
    }
  }
}
</script>

<style scoped>
>>> .v-event {
  max-width: 32%;
  margin-right: 1px;
  margin-left: 2px;
  float: left;
  text-align: center;
}
</style>
