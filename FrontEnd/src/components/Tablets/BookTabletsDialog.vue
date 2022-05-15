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
        <v-toolbar cards flat class="my-2">
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
        </v-toolbar>

        <v-row justify="center" class="ml-10">
          <v-col cols="4" class="pt-0" v-for="item in periods" :key="item">
            <v-checkbox
              v-model="period"
              :label="`${item}교시`"
              :color="colors[item-1]"
              :value="item"
              hide-details
            >
            </v-checkbox>
          </v-col>
        </v-row>

        <v-form id="book-tablets-form" ref="bookTabletsForm" class="pa-3 pt-10">
          <v-text-field
            name="class"
            label="학년-반"
            outlined
            color="primary"
          ></v-text-field>
          <v-text-field
            name="quantity"
            label="대여 수량"
            outlined
            color="primary"
          ></v-text-field>
        </v-form>
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

export default {
  props: { selectedDate: String },
  data: () => ({
    place: '',
    period: [],
    places: ['전산실', '학습 준비물실'],
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
    // ...mapActions('bookStore', ['login']),
    save () {
      console.log('save()...')
      // const postData = new FormData(document.getElementById('book-tablets-form'))
      // this.login(postData)
      this.$refs.bookTabletsForm.reset()
    }
  }
}
</script>
