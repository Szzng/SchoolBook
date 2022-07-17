<template>
  <div>
    <v-dialog v-model="dialog.destroyToolBooking" max-width="450" persistent>
      <v-card class="px-5 py-5">
        <v-row align="center" justify="center">
          <v-chip color="error" large class="white--text mt-10">
            <v-avatar left>
              <v-icon>mdi-close-circle-outline</v-icon>
            </v-avatar>
            {{ booking.booker }} ({{ booking.quantity }}대)
          </v-chip>
        </v-row>

        <v-row
          align="center"
          justify="center"
          class="mx-5 mt-8"
          :style="{ fontSize: '17px' }"
        >
          정말 예약을 취소하시겠어요?<br />
          예약 시 저장한 비밀번호를 입력하세요.
        </v-row>
        <v-form ref="password">
          <v-row class="mx-10 mt-8">
            <v-text-field
              v-model="password"
              label="예약 취소용 비밀번호"
              required
              :rules="passwordRule"
              type="number"
              outlined
              color="primary"
              class="mb-1 px-3"
            ></v-text-field>
          </v-row>
        </v-form>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" large class="white--text" @click="destroyBooking"
            >예약 취소</v-btn
          >
          <v-btn large @click="close">닫기</v-btn>
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

  data: () => ({
    password: '',
    passwordRule: [
      (v) => !!v || '예약 시 저장한 비밀번호를 입력하세요.',
      (v) => (v && v.length === 4) || '비밀번호는 숫자 4자리로 적어주세요.'
    ]
  }),

  computed: {
    ...mapState('toolStore', ['dialog', 'focusTool', 'focusDate'])
  },

  methods: {
    close () {
      this.dialog.destroyToolBooking = false
      this.$refs.password.reset()
      this.$refs.password.resetValidation()
    },

    destroyBooking () {
      if (this.$refs.password.validate()) {
        api.DestroyToolBooking(this.booking.id, this.password, this.focusTool, this.focusDate)
        this.dialog.destroyToolBooking = false
      }
    }
  }
}
</script>
