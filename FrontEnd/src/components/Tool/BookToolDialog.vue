<template>
  <div>
    <v-dialog
      v-model="dialog.bookTool"
      max-width="50vw"
      content-class="book-dialog"
      persistent
    >
      <v-card class="pa-6">
        <v-row justify="end">
          <v-btn text @click="close">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-row>
        <v-row justify="center" class="mt-0">
          <v-card-title>{{ formatSelectedDate }}</v-card-title>
        </v-row>

        <v-form v-if="left" ref="form" lazy-validation>
          <v-row justify="center" class="mt-5">
            <v-col cols="3" class="py-3" v-for="item in periods" :key="item">
              <v-checkbox
                v-model="period"
                :label="`${item}교시 (${left[item - 1]}대)`"
                :disabled="!left[item - 1]"
                :color="colors[item - 1]"
                :value="item"
                hide-details
              >
              </v-checkbox>
            </v-col>
          </v-row>

          <v-text-field
            v-model="booker"
            label="학년-반"
            required
            :rules="bookerRule"
            outlined
            color="primary"
            class="mt-12 pt-2 px-3"
          ></v-text-field>
          <v-text-field
            v-model="quantity"
            label="대여 수량"
            required
            :rules="quantityRule"
            type="number"
            outlined
            color="primary"
            class="mt-3 px-3"
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="예약 취소용 비밀번호 (숫자 4자리)"
            required
            :rules="passwordRule"
            type="number"
            outlined
            color="primary"
            class="mt-3 px-3"
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
import api from '@/api/modules/tool'

export default {
  data: () => ({
    period: [],
    booker: '',
    quantity: 0,
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
    ...mapState('toolStore', [
      'dialog',
      'periods',
      'left',
      'focusDate',
      'focusTool',
      'colors'
    ]),
    formatSelectedDate () {
      const date = this.focusDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    },

    fetchMinLeft () {
      var leftArrayByPlace = this.left
      var min = Math.max(...leftArrayByPlace)
      this.period.forEach(function (i) {
        min = Math.min(min, leftArrayByPlace[i - 1])
      })
      return min
    },

    quantityRule () {
      const rules = [
        (v) => !!v || '몇 개를 빌리시나요?',
        (v) => (v && v >= 1) || '0보다 큰 수를 입력해주세요.'
      ]

      if (this.fetchMinLeft) {
        const rule = (v) =>
          (v || '') <= this.fetchMinLeft ||
          `${this.fetchMinLeft} 이하의 수를 입력해주세요`

        rules.push(rule)
      }
      return rules
    }
  },

  methods: {
    close () {
      this.dialog.bookTool = false
      this.$refs.form.reset()
      this.$refs.form.resetValidation()
    },

    save () {
      if (!this.period.length) {
        alert('몇 교시에 사용하실지 선택해주세요!')
      }
      if (this.period.length && this.$refs.form.validate()) {
        const postData = {
          tool: this.focusTool,
          date: this.focusDate,
          period: this.period,
          booker: this.booker,
          quantity: this.quantity,
          password: this.password
        }
        api.BookTool(this, postData)
        this.$refs.form.reset()
      }
    }
  }
}
</script>
