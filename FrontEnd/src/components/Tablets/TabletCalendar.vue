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
            @click:date="bookTablets"
          ></v-calendar>
        </v-sheet>

      </v-col>
    </v-row>
    <checkTabletsBookingDialog :selectedDate="focus" />
  </div>
</template>

<script>
import checkTabletsBookingDialog from '@/components/Tablets/CheckTabletsBookingDialog.vue'
import { mapState } from 'vuex'

export default {
  components: { checkTabletsBookingDialog },

  data: () => ({
    focus: '',
    weekday: [1, 2, 3, 4, 5, 6, 0]
  }),

  computed: {
    ...mapState('bookStore', ['dialog'])
  },
  methods: {
    bookTablets ({ date }) {
      this.focus = date
      this.dialog.checkTabletsBooking = true
    },
    setToday () {
      this.focus = ''
    }
  }
}
</script>
