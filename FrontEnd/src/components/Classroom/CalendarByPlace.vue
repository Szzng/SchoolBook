<template>
  <div>
    <v-row class="fill-height ml-5">
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

        <v-sheet height="500" class="pr-10">
          <v-calendar
            ref="calendar"
            v-model="$store.state.classroomStore.focusDate"
            :weekdays="weekday"
            color="primary"
            type="month"
            :events="notYetBooked"
            event-color="primary"
            :event-more="false"
            @click:date="checkRoomBooking"
            @click:event="bookRoom"
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
import CheckRoomBookingDialog from '@/components/Classroom/CheckRoomBookingDialog.vue'
import BookRoomDialog from '@/components/Classroom/BookRoomDialog.vue'
import DestroyRoomBookingDialog from '@/components/Classroom/DestroyRoomBookingDialog.vue'

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
    weekday: [1, 2, 3, 4, 5],
    notYetBooked: [
      {
        name: '1',
        start: '2022-05-18',
        color: 'white'
      },
      {
        name: '2',
        start: '2022-05-18'
      },
      {
        name: '3',
        start: '2022-05-18'
      },
      {
        name: '4',
        start: '2022-05-18'
      },
      {
        name: '5',
        start: '2022-05-18'
      },
      {
        name: '6',
        start: '2022-05-18'
      }
    ]
  }),

  computed: {
    ...mapState('classroomStore', ['dialog', 'bookedRoomLists'])
  },

  async created () {
    await this.$nextTick()
    this.initCalendarTitle = this.$refs.calendar.title
  },

  methods: {
    checkRoomBooking ({ date }) {
      this.$store.commit('classroomStore/focusDateSetter', date)
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
  max-width: 12%;
  height: 26% !important;
  border-radius: 100%;
  margin-right: 1px;
  margin-left: 4px;
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
