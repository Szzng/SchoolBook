<template>
  <div>
    <v-dialog v-model="dialog.destroyToolBooking " max-width="400" persistent>
      <v-card>
        <v-row align="center" justify="center">
          <v-chip color="red darken-1" class="white--text mt-10">
            <v-avatar left>
              <v-icon>mdi-close-circle-outline</v-icon>
            </v-avatar>
            {{ booking.booker }} ({{ booking.quantity }}대)
          </v-chip>
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
          <v-btn @click="dialog.destroyToolBooking = false">아니요</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/tool'

export default {
  props: {
    booking: Object
  },

  computed: {
    ...mapState('toolStore', ['dialog', 'focusTool', 'focusDate'])
  },

  methods: {
    destroyBooking () {
      api.DestroyToolBooking(this.booking.id, this.focusTool, this.focusDate)
      this.dialog.destroyToolBooking = false
    }
  }
}
</script>
