<template>
  <div class="mt-16 pt-4 ml-4">
    <v-row class="fill-height ml-3">
      <v-col sm="12" md="8">
        <v-sheet height="80" class="pr-10 mt-5">
          <v-toolbar flat>
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
              {{ $refs.calendar.title }} {{focusPlace}}
            </v-toolbar-title>
            <v-toolbar-title v-else>
              {{ initCalendarTitle }} {{focusPlace}}
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

        <v-sheet height="550" class="pr-10">
          <v-calendar
            ref="calendar"
            v-model="$store.state.roomStore.focusDate"
            :weekdays="weekday"
            color="primary"
            type="month"
            :events="availableBookingEvents"
            event-color="deep-purple lighten-3"
            :event-more="false"
            @click:date="checkRoomBooking"
            @click:event="bookRoom"
            @change="changed"
          ></v-calendar>
        </v-sheet>
      </v-col>

      <v-col sm="12" md="4">
        <CheckRoomBookingDialog />
      </v-col>

    </v-row>
    <BookRoomDialog :eventBooking="eventBooking" />
    <DestroyRoomBookingDialog :eventDestroying="eventDestroying" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import CheckRoomBookingDialog from '@/components/Room/CheckRoomBookingDialog.vue'
import BookRoomDialog from '@/components/Room/BookRoomDialog.vue'
import DestroyRoomBookingDialog from '@/components/Room/DestroyRoomBookingDialog.vue'
import api from '@/api/modules/room'

export default {
  components: {
    CheckRoomBookingDialog,
    BookRoomDialog,
    DestroyRoomBookingDialog
  },

  data: () => ({
    initCalendarTitle: '',
    focus: '',
    eventBooking: {},
    eventDestroying: {},
    weekday: [1, 2, 3, 4, 5]
  }),

  computed: {
    ...mapState('roomStore', ['dialog', 'bookedRoomLists', 'focusPlace', 'availableBookingEvents'])
  },

  async created () {
    await this.$nextTick()
    this.initCalendarTitle = this.$refs.calendar.title
    api.getAvailableBookingEvents(this, this.focusPlace, this.$refs.calendar.start)
  },

  methods: {
    changed (info) {
      api.getAvailableBookingEvents(this, this.focusPlace, info.start.date)
    },
    checkRoomBooking ({ date }) {
      this.$store.commit('roomStore/focusDateSetter', date)
      api.getRoomBookingsByDate(this.focusPlace, date)
      this.dialog.checkRoomBooking = true
    },

    bookRoom ({ nativeEvent, event }) {
      this.eventBooking = event
      this.dialog.bookRoom = true
    },

    assertDestroyRoomBooking ({ nativeEvent, event }) {
      this.eventDestroying = event
      this.dialog.destroyRoomBooking = true
    },

    setToday () {
      this.$store.commit('roomStore/focusDateSetter', '')
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
  max-width: 12%;
  height: 22% !important;
  border-radius: 100%;
  margin-right: 1px;
  margin-left: 0.4em;
  margin-top:0.9em;
  float: left;
  text-align: center;
  font-size: 15px;
}

/* >>> .pl-1 {
  font-size: 20px;
  padding-left: 0px;
  padding-right: 0px;
  margin-left: 0px;
} */
</style>
