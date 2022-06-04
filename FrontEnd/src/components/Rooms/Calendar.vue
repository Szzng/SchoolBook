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
            color="primary"
            type="week"
            :weekdays="weekday"
            first-time="1"
            interval-height="80"
            interval-minutes="60"
            interval-count="6"
            :interval-format="formatInterval"
            :show-interval-label="showInterval"
            :events="bookedRoomLists"
            :event-name="getEventName"
            @click:date="bookRoom"
            @click:event="assertDestroyRoomBooking"
          ></v-calendar>
        </v-sheet>
      </v-col>
    </v-row>
    <BookRoomDialog :selectedDate="focus" />
    <DestroyRoomBookingDialog :destroyEvent="destroyEvent" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookRoomDialog from '@/components/Rooms/BookRoomDialog.vue'
import DestroyRoomBookingDialog from '@/components/Rooms/DestroyRoomBookingDialog.vue'
import api from '@/api/modules/room'

export default {
  components: { BookRoomDialog, DestroyRoomBookingDialog },

  data: () => ({
    initCalendarTitle: '',
    focus: '',
    destroyEvent: {},
    weekday: [1, 2, 3, 4, 5]
  }),

  created () {
    api.getBookedRoomLists()
  },

  computed: {
    ...mapState('roomStore', ['dialog', 'bookedRoomLists'])
  },
  methods: {
    bookRoom () {
      this.dialog.bookRoom = true
    },

    assertDestroyRoomBooking ({nativeEvent, event}) {
      this.destroyEvent = event
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
>>> .v-calendar-daily__interval-text {
  font-size: 15px;
  padding-top: 2.5em;
}
>>> .v-event-timed {
  margin-left: 5px;
  line-height: 75px;
  text-align: center;
}
>>> .v-event-summary {
  font-size: 20px;
}
</style>
