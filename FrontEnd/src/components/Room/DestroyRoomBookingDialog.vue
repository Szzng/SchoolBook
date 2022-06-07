<template>
  <div>
    <v-dialog
      v-if="booking"
      v-model="dialog.destroyRoomBooking"
      max-width="400"
      persistent
    >
      <v-card>
        <v-row align="center" justify="center">
          <v-btn
            color="red darken-1"
            width="100"
            height="40"
            class="font-weight-bold white--text mt-10"
            style="font-size: 16px"
          >
            <v-icon class="mr-1">mdi-close-circle-outline</v-icon>
            {{ booking.booker }}
          </v-btn>
        </v-row>
        <v-row
          align="center"
          justify="center"
          class="mt-8 mb-6"
          :style="{ fontSize: '18px' }"
        >
          정말 예약을 취소하시겠어요?
        </v-row>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" class="white--text" @click="destroyBooking"
            >예약 취소하기</v-btn
          >
          <v-btn @click="dialog.destroyRoomBooking = false">아니요</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/room'

export default {
  props: {
    booking: Object
  },

  computed: {
    ...mapState('roomStore', ['dialog', 'focusRoom', 'focusDate'])
  },

  methods: {
    destroyBooking () {
      api.DestroyRoomBooking(this.booking.id, this.focusRoom, this.focusDate)
      this.dialog.destroyRoomBooking = false
    }
  }
}
</script>
