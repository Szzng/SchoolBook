<template>
  <div>
    <v-dialog
      v-model="dialog.bookRoom"
      max-width="500"
      content-class="book-dialog"
      persistent
    >
      <v-card class="pa-6">
        <v-row justify="end">
          <v-btn text @click="close">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-row>
        <v-row align="center" justify="center" class="mt-0">
          <v-card-title class="pb-0"
            >{{ formatSelectedDate }} {{ eventBooking.name }}교시
          <v-card-subtitle class="purple--text pl-1 pb-3">{{focusRoom}}</v-card-subtitle>
          </v-card-title>
        </v-row>

        <v-form ref="form" lazy-validation>
          <v-text-field
            v-model="booker"
            label="학년-반"
            required
            outlined
            color="primary"
            class="mt-12 pt-2 px-3"
            :rules="bookerRule"
          ></v-text-field>
          <v-card-actions>
            <v-btn
              block
              color="primary"
              class="white--text pr-0 mr-0"
              x-large
              @click="save"
            >
              예약하기
            </v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/room'

export default {
  props: {
    eventBooking: Object
  },
  data: () => ({
    booker: '',
    bookerRule: [
      (v) => !!v || '예약자를 적어주세요.',
      (v) => (v && v.length <= 10) || '예약자는 10글자 이하로 적어주세요.'
    ]
  }),

  computed: {
    ...mapState('roomStore', ['dialog', 'periods', 'focusDate', 'focusRoom']),
    formatSelectedDate () {
      if (this.eventBooking.start) {
        const date = this.eventBooking.start.split('-')
        return date[1] + '월  ' + date[2] + '일 '
      }
    }
  },

  methods: {
    close () {
      this.dialog.bookRoom = false
      this.$refs.form.reset()
      this.$refs.form.resetValidation()
    },

    save () {
      if (this.$refs.form.validate()) {
        const postData = {
          'date': this.eventBooking.start,
          'period': this.eventBooking.name,
          'room': this.focusRoom,
          'booker': this.booker
        }
        api.BookRoom(this, postData)
        this.$refs.form.reset()
      }
    }
  }
}
</script>
