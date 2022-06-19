<template>
  <div>
    <v-dialog v-model="dialog.updateTimetable" max-width="900" persistent>
      <v-form ref="form" lazy-validation>
        <v-card height="540" class="pa-4">
          <v-row align="center">
            <v-col class="pt-0">
              <v-card-title>
                <span
                  style="font-weight: bolder; font-size: 22px; color: indigo"
                  >{{ room }}</span
                >의 정해진 시간표를 입력하세요.
                <v-card-subtitle
                  class="indigo--text font-weight-bold pa-0 ma-0 pl-1 mt-1"
                  >(빈 시간은 빈칸으로 두세요.)</v-card-subtitle
                >
              </v-card-title>
            </v-col>
            <v-col cols="3" class="text-right pt-0 mr-2">
              <v-btn @click="save" class="primary" large> 완료 </v-btn>
              <v-btn @click="dialog.updateTimetable = false" large outlined> 닫기 </v-btn>
            </v-col>
          </v-row>

          <v-divider></v-divider>
          <v-row align="center" justify="center" class="py-2 mx-0">
            <v-col cols="1"></v-col>
            <v-col
              v-for="weekday in weekdays"
              :key="weekday"
              class="text-center"
            >
              {{ weekday }}요일
            </v-col>
          </v-row>
          <v-divider class="pb-1"></v-divider>

          <v-row
            align="center"
            justify="center"
            v-for="period in periods"
            :key="period"
            class="my-2 mx-0"
          >
            <v-col cols="1" class="text-center py-1">
              {{ period }}
            </v-col>
            <v-col v-for="(weekday, idx) in weekdays" :key="idx" class="py-1">
              <v-text-field
                v-model="timetable[idx][period - 1]"
                :label="`${weekday} ${period}교시`"
                filled
                rounded
                dense
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
        </v-card>
      </v-form>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/setting'

export default {
  props: {
    room: String
  },

  data: () => ({
    weekdays: ['월', '화', '수', '목', '금']
  }),

  computed: {
    ...mapState('roomStore', ['dialog', 'periods', 'rooms', 'timetable'])
  },

  methods: {
    save () {
      const postData = {
        room: this.room,
        timetable: this.timetable
      }
      api.updateTimetable(postData)
      this.dialog.updateTimetable = false
    }
  }
}
</script>
