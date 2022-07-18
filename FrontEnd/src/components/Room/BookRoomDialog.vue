<template>
  <div>
    <v-dialog
      :retain-focus="false"
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
            >{{ formatSelectedDate }} {{ booking.name }}교시
            <v-card-subtitle class="accent--text pl-1 pb-3">{{
              focusRoom
            }}</v-card-subtitle>
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
          <v-text-field
            v-model="password"
            label="예약 취소용 비밀번호 (숫자 4자리)"
            required
            :rules="passwordRule"
            type="number"
            outlined
            color="primary"
            class="px-3"
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
  props: {},
  data: () => ({
    booker: '',
    password: '',
    bookerRule: [
      (v) => !!v || '예약자를 적어주세요.',
      (v) => (v && v.length <= 4) || '예약자는 4글자 이하로 적어주세요.'
    ],
    passwordRule: [
      (v) => !!v || '예약 취소 시 사용할 비밀번호를 적어주세요.',
      (v) => (v && v.length === 4) || '비밀번호는 숫자 4자리로 적어주세요.'
    ]
  }),

  computed: {
    ...mapState('roomStore', [
      'dialog',
      'periods',
      'focusDate',
      'focusRoom',
      'booking'
    ]),
    formatSelectedDate () {
      if (this.booking.start) {
        const date = this.booking.start.split('-')
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
          date: this.booking.start,
          period: this.booking.name,
          room: this.focusRoom,
          booker: this.booker,
          password: this.password
        }
        api.BookRoom(this, postData)
        this.$refs.form.reset()
      }
    }
  }
}
</script>
