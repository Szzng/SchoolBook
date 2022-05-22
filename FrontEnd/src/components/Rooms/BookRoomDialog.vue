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
        <v-row justify="center" class="mt-0">
          <v-card-title>{{ formatSelectedDate }}</v-card-title>
        </v-row>

        <v-form ref="form" lazy-validation>
         <v-row justify="center" class="ml-8 mt-5">
            <v-col cols="4" class="py-0" v-for="item in periods" :key="item">
              <v-checkbox
                v-model="period"
                :label="`${item}교시`"
                :color="colors[item - 1]"
                :value="item"
                :disabled="false"
                :rules="periodRule"
                hide-details
              >
              </v-checkbox>
            </v-col>
          </v-row>
          <v-text-field
          v-model="borrower"
            label="학년-반"
            required
            outlined
            color="primary"
            class="mt-12 pt-2 px-3"
            :rules="borrowerRule"
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
    selectedDate: String
  },
  data: () => ({
    period: '',
    place: '컴퓨터실1',
    borrower: '',
    colors: ['red', 'indigo', 'deep-purple', 'pink', 'orange', 'green'],
    periodRule: [(v) => !!v || '몇 교시에 예약하시나요?'],
    borrowerRule: [
      (v) => !!v || '예약자 적어주세요.',
      (v) => (v && v.length <= 10) || '예약자는 10글자 이하로 적어주세요.'
    ]
  }),

  computed: {
    ...mapState('roomStore', ['dialog', 'periods']),
    formatSelectedDate () {
      const date = this.selectedDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
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
          'time.date': this.selectedDate,
          'time.period': this.period,
          'place.name': this.place,
          borrower: this.borrower
        }
        api.BookRoom(this, postData)
        this.$refs.form.reset()
      }
    }
  }
}
</script>
