<template>
  <div>
    <v-dialog
      v-model="dialog.checkRoomBooking"
      max-width="700"
      content-class="check-booking-dialog"
    >
      <v-card class="pl-2">
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-card-title class="pl-0">{{ formatSelectedDate }}</v-card-title>
          <v-spacer></v-spacer>

          <v-btn color="primary" class="pr-0 mr-0">
            예약
            <v-icon left class="ml-0"> mdi-clock-plus-outline </v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  components: { },

  props: {
    selectedDate: String
  },

  data: () => ({
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green', 'indigo']
  }),

  computed: {
    ...mapState('roomStore', ['dialog']),

    formatSelectedDate () {
      const date = this.selectedDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {
  }
}
</script>

<style scoped>
>>> .check-booking-dialog {
  position: absolute;
  left: 0;
}
</style>
