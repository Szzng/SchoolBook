<template>
  <div>
    <v-dialog
      v-model="dialog.bookTablets"
      max-width="500"
      content-class="book-dialog"
    >
      <v-card class="pa-6">

        <v-row justify="center">
          <v-card-title>{{ formatSelectedDate }}</v-card-title>
        </v-row>

        <v-row justify="space-between" class="mx-12">
          <v-checkbox
            v-for="(item, i) in places"
            :key="i"
            v-model="place"
            :label="item"
            :color="colors[i]"
            :value="item"
            hide-details
          ></v-checkbox>
        </v-row>

        <v-row justify="center">
          <v-col cols="4" class="pt-0" v-for="item in periods" :key="item">
            <v-checkbox
              v-model="period"
              :label="`${item}교시`"
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
          outlined
          color="primary"
        ></v-text-field>
        <v-text-field
          v-model="quantity"
          label="대여 수량"
          outlined
          color="primary"
        ></v-text-field>
        <v-card-actions>
          <v-btn
            block
            color="blue darken-1"
            class="pr-0 mr-0"
            text
            x-large
            @click="save"
          >
            예약하기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/tablets'

export default {
  props: { selectedDate: String },
  data: () => ({
    place: '',
    period: [],
    borrower: '',
    quantity: 0,
    places: ['전산실', '준비물실'],
    periods: [1, 2, 3, 4, 5, 6],
    colors: ['red', 'indigo', 'deep-purple', 'pink', 'orange', 'green']
  }),

  computed: {
    ...mapState('bookStore', ['dialog']),
    formatSelectedDate () {
      const date = this.selectedDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {
    save () {
      console.log('save()...')
      const postData = {
        'time.date': this.selectedDate,
        'time.period': this.period,
        'place.name': this.place,
        'borrower': this.borrower,
        'quantity': this.quantity
      }
      api.BookTablets(this, postData)
      console.log(postData)
    }
  }
}
</script>
