<template>
  <div>
    <v-row class="fill-height">
      <v-col sm="12" md="4">
        <v-sheet height="10vh">
          <v-toolbar flat>
            <v-spacer></v-spacer><v-spacer></v-spacer><v-spacer></v-spacer>

            <v-btn fab text small color="grey darken-2" @click="prev"
              ><v-icon small> mdi-chevron-left </v-icon>
            </v-btn>

            <v-toolbar-title v-if="$refs.calendar">
              {{ $refs.calendar.title }}
            </v-toolbar-title>
            <v-toolbar-title v-else>
              {{ initCalendarTitle }}
            </v-toolbar-title>

            <v-btn fab text small color="grey darken-2" @click="next"
              ><v-icon small> mdi-chevron-right </v-icon>
            </v-btn>

            <v-spacer></v-spacer>

            <v-btn outlined color="grey darken-2" @click="setToday">
              Today
            </v-btn>
          </v-toolbar>
        </v-sheet>

        <v-sheet height="68vh" class="ml-2">
          <v-calendar
            ref="calendar"
            v-model="$store.state.toolStore.focusDate"
            :weekdays="weekday"
            color="primary"
            type="month"
            @click:date="checkToolBooking"
          ></v-calendar>
        </v-sheet>
      </v-col>

      <v-col sm="12" md="8">
        <CheckToolBookingDialog />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import CheckToolBookingDialog from '@/components/Tool/CheckToolBookingDialog.vue'
import { mapState } from 'vuex'
import api from '@/api/modules/tool'

export default {
  components: { CheckToolBookingDialog },

  data: () => ({
    initCalendarTitle: '',
    weekday: [1, 2, 3, 4, 5]
  }),

  computed: {
    ...mapState('toolStore', ['dialog', 'focusDate', 'focusTool'])
  },

  async created () {
    await this.$nextTick()
    this.initCalendarTitle = this.$refs.calendar.title
  },

  methods: {
    checkToolBooking () {
      api.getToolBookingsByDate(this.focusTool, this.focusDate)
    },
    prev () {
      this.$refs.calendar.prev()
      this.checkToolBooking()
    },
    next () {
      this.$refs.calendar.next()
      this.checkToolBooking()
    },
    setToday () {
      this.$store.commit(
        'toolStore/focusDateSetter',
        this.$refs.calendar.$data.times.today.date
      )
      this.checkToolBooking()
    }
  }
}
</script>
