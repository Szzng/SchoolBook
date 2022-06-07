<template>
  <div>
    <v-row class="fill-height ml-5">
      <v-col sm="12" md="5">
        <v-sheet height="80" class="pr-3">
          <v-toolbar flat>
            <v-btn outlined color="grey darken-1" @click="setToday">
              Today
            </v-btn>
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

            <v-btn disabled text x-large class="pa-0">
              {{ focusTool }}
            </v-btn>
          </v-toolbar>
        </v-sheet>

        <v-sheet height="520" class="pr-8 ml-2">
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

      <v-col sm="12" md="7">
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
    ...mapState('toolStore', ['dialog', 'focusTool'])
  },

  async created () {
    await this.$nextTick()
    this.initCalendarTitle = this.$refs.calendar.title
  },

  methods: {
    checkToolBooking ({ date }) {
      this.$store.commit('toolStore/focusDateSetter', date)
      api.getToolBookingsByDate(this.focusTool, date)
    },
    setToday () {
      this.$store.commit('toolStore/focusDateSetter', '')
      this.dialog.checkToolBooking = false
    }
  }
}
</script>
