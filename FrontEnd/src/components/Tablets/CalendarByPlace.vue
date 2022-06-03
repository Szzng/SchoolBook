<template>
  <div>
    <v-row class="fill-height ml-5">
      <v-col sm="12" md="6">
        <v-sheet height="80" class="pr-10">
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

        <v-sheet height="530" class="pr-10">
          <v-calendar
            ref="calendar"
            v-model="$store.state.tabletsStore.focusDate"
            :weekdays="weekday"
            color="primary"
            type="month"
            @click:date="checkTabletsBooking"
          ></v-calendar>
        </v-sheet>
      </v-col>

      <v-col sm="12" md="6">
        <CheckTabletsBookingDialog />
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
    weekday: [1, 2, 3, 4, 5]
  }),

  computed: {
    ...mapState('tabletsStore', ['dialog', 'focusPlace'])
  },

  async created () {
    await this.$nextTick()
    this.initCalendarTitle = this.$refs.calendar.title
  },

  methods: {
    checkTabletsBooking ({ date }) {
      this.$store.commit('tabletsStore/focusDateSetter', date)
      api.getBookedTabletsListByDate(this.focusPlace, date)
      api.getLeftTabletsCounts(this.focusPlace, date)
      this.dialog.checkTabletsBooking = true
    },
    setToday () {
      this.$store.commit('tabletsStore/focusDateSetter', '')
      this.dialog.checkTabletsBooking = false
    }
  }
}
</script>
