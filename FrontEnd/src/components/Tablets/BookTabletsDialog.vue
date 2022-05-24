<template>
  <div>
    <v-dialog
      v-model="dialog.bookTablets"
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
        <v-row justify="center" class="mt-0">
          <v-card-title>{{ formatSelectedDate }}</v-card-title>
        </v-row>

        <v-form v-if="left" ref="form" lazy-validation>
          <v-row justify="center" class="mt-5">
            <v-col cols="4" class="py-0" v-for="item in periods" :key="item">
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
            v-model="borrower"
            label="학년-반"
            required
            :rules="borrowerRule"
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
import api from '@/api/modules/tablets'

export default {
  props: {
    focusDate: String,
    focusPlace: String
  },

  data: () => ({
    period: [],
    borrower: '',
    quantity: 0,
    colors: ['red', 'indigo', 'deep-purple', 'pink', 'orange', 'green'],
    borrowerRule: [
      (v) => !!v || '예약자를 적어주세요.',
      (v) => (v && v.length <= 10) || '예약자는 10글자 이하로 적어주세요.'
    ]
  }),

  computed: {
    ...mapState('tabletsStore', [
      'dialog',
      'periods',
      'places',
      'left'
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
      this.dialog.bookTablets = false
      this.$refs.form.reset()
      this.$refs.form.resetValidation()
    },

    save () {
      if (!this.period.length) {
        alert('몇 교시에 사용하실지 선택해주세요!')
      }
      if (this.period.length && this.$refs.form.validate()) {
        const postData = {
          'time.date': this.focusDate,
          'time.period': this.period,
          'place.name': this.focusPlace,
          borrower: this.borrower,
          quantity: this.quantity
        }
        api.BookTablets(this, postData)
        this.$refs.form.reset()
      }
    }
  }
}
</script>
