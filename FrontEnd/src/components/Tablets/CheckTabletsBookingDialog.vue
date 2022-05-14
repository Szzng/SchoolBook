<template>
  <div>
    <v-dialog
      v-model="dialog.checkTabletsBooking"
      max-width="600"
      content-class="check-booking-dialog"
    >
      <v-card class="pl-2">
        <v-card-actions>
          <v-card-title class="pl-0">{{ formatSelectedDate }}</v-card-title>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            class="pr-0 mr-0"
            text
            x-large
            @click="book"
          >
            예약
            <v-icon left class="ml-0"> mdi-clock-plus-outline </v-icon>
          </v-btn>
        </v-card-actions>

        <v-card
          v-for="list in bookedLists"
          :key="list.period"
          flat
          class="my-0 py-0"
        >
          <v-card-subtitle class="py-3 black--text">
            {{ list.period }}</v-card-subtitle
          >
          <v-row
            v-for="place in list.place"
            :key="place.name"
            align="center"
            class="ml-2"
          >
            <v-col cols="3" class="ml-2 indigo--text">
              {{ place.name }} + {{ place.left }}대
              </v-col>
            <v-col>
              <v-card-text class="pa-0">
                <v-chip-group column>
                  <v-chip
                    v-for="(item, i) in place.classes"
                    :key="i"
                    :color="colors[i]"
                    outlined
                    class="white--text"
                  >
                    <v-avatar left>
                      <v-icon>mdi-checkbox-marked-circle</v-icon>
                    </v-avatar>
                    {{ item.class }} ({{ item.quantity }}대)
                  </v-chip>
                </v-chip-group>
              </v-card-text>
            </v-col>
          </v-row>
        <v-divider class="my-3"></v-divider>
        </v-card>
      </v-card>
    </v-dialog>

    <BookTabletsDialog :selectedDate="selectedDate" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import BookTabletsDialog from '@/components/Tablets/BookTabletsDialog.vue'

export default {
  components: { BookTabletsDialog },

  props: { selectedDate: String },

  data: () => ({
    place: '',
    period: [],
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green'],
    place1BookedLists: [],
    place2BookedLists: [],
    bookedLists: [
      {
        period: '1교시',
        place: [
          {name: '전산실', left: '0', classes: [{ class: '4-7', quantity: '30' }, { class: '6-4', quantity: '30' }]},
          {name: '준비물실', left: '30', classes: [{ class: '5-7', quantity: '30' }, { class: '6-1', quantity: '30' }, { class: '6-1', quantity: '30' }]}
        ]
      },
      {
        period: '2교시',
        place: [
          {name: '전산실', left: '0', classes: [{ class: '4-7', quantity: '30' }, { class: '6-4', quantity: '30' }]},
          {name: '준비물실', left: '30', classes: [{ class: '5-7', quantity: '30' }, { class: '6-1', quantity: '30' }]}
        ]
      }, {
        period: '3교시',
        place: [
          {name: '전산실', left: '0', classes: [{ class: '4-7', quantity: '30' }, { class: '6-4', quantity: '30' }]},
          {name: '준비물실', left: '30', classes: [{ class: '5-7', quantity: '30' }, { class: '6-1', quantity: '30' }]}
        ]
      }, {
        period: '4교시',
        place: [
          {name: '전산실', left: '0', classes: [{ class: '4-7', quantity: '30' }, { class: '6-4', quantity: '30' }]},
          {name: '준비물실', left: '30', classes: [{ class: '5-7', quantity: '30' }, { class: '6-1', quantity: '30' }]}
        ]
      }, {
        period: '5교시',
        place: [
          {name: '전산실', left: '0', classes: [{ class: '4-7', quantity: '30' }, { class: '6-4', quantity: '30' }]},
          {name: '준비물실', left: '30', classes: [{ class: '5-7', quantity: '30' }, { class: '6-1', quantity: '30' }]}
        ]
      }, {
        period: '6교시',
        place: [
          {name: '전산실', left: '0', classes: [{ class: '4-7', quantity: '30' }, { class: '6-4', quantity: '30' }]},
          {name: '준비물실', left: '30', classes: [{ class: '5-7', quantity: '30' }, { class: '6-1', quantity: '30' }]}
        ]
      } ]
  }),

  computed: {
    ...mapState('bookStore', ['dialog']),
    formatSelectedDate () {
      const date = this.selectedDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {
    book () {
      this.dialog.bookTablets = true
    }
  }
}
</script>

<style scoped>
>>> .check-booking-dialog {
  position: absolute;
  left: 0;
}
</style>
