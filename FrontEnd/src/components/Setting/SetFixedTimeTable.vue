<template>
  <div class="mt-5 mx-16">
    <v-form ref="form" lazy-validation>
      <v-card outlined class="mb-3">
        <v-card-title>
          1. 시간표를 설정할 교실(장소)를 선택하세요.
        </v-card-title>
        <v-card-text>
          <v-row justify="start" align="center" class="">
            <v-col
              cols="3"
              class="py-1 mb-3"
              v-for="item in places"
              :key="item"
            >
              <v-checkbox
                v-model="place"
                :label="item"
                :value="item"
                hide-details
              >
              </v-checkbox>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>

      <v-card outlined class="mb-10">
        <v-card-title>
          2. 선택한 장소의 고정 시간표를 입력하세요.
        </v-card-title>

        <v-divider></v-divider>
        <v-row align="center" justify="center" class="py-3 mx-0">
          <v-col cols="1"></v-col>
          <v-col
            cols="2"
            v-for="weekday in weekdays"
            :key="weekday"
            class="text-center"
          >
            {{ weekday }}요일
          </v-col>
        </v-row>
        <v-divider></v-divider>

        <v-row
          align="center"
          justify="center"
          v-for="period in periods"
          :key="period"
          class="my-1 mx-0"
        >
          <v-col cols="1" class="text-center py-1"> {{ period }}교시 </v-col>
          <v-col
            cols="2"
            v-for="(weekday, idx) in weekdays"
            :key="idx"
            class="text-center py-1"
          >
            <v-text-field
              v-model="fixedTimeTable[idx][period - 1]"
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
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: () => ({
    place: '',
    places: ['강당', '컴퓨터1실', '컴퓨터2실'],
    weekdays: ['월', '화', '수', '목', '금'],
    fixedTimeTable: {
      0: ['', '', '', '', '', ''],
      1: ['', '', '', '', '', ''],
      2: ['', '', '', '', '', ''],
      3: ['', '', '', '', '', ''],
      4: ['', '', '', '', '', '']
    }
  }),

  computed: {
    ...mapState('classroomStore', ['periods'])
  }
}
</script>

<style scoped>
.v-card__title {
  font-size: 18px;
  color: indigo;
  font-weight: bolder;
}
</style>
