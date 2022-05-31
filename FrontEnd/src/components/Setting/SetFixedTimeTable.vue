<template>
  <div class="mt-4 mx-16">
    <v-form ref="form" lazy-validation>
      <v-row align="start" justify="center">
        <v-col sm="12" md="4">
          <v-card class="mb-3" height="530">
            <v-card-title>
              1. 시간표를 설정할 교실(장소)를 선택하세요.
            </v-card-title>
            <v-divider class="mb-3"></v-divider>
            <v-card-text>
              <v-row
                justify="start"
                align="center"
                class="ml-3 pb-1"
                v-for="item in places"
                :key="item"
              >
                <v-checkbox
                  v-model="place"
                  :label="item"
                  :value="item"
                  hide-details
                  color="secondary"
                >
                  <template v-slot:label>
                    <span id="checkboxLabel">{{ item }}</span>
                  </template>
                </v-checkbox>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col v-show="place" sm="12" md="8">
          <v-card class="mt-3" height="530">
            <v-row align="center">
              <v-col class="pt-0">
                <v-card-title>
                  2. 정해진 시간표를 입력하세요.
                  <v-card-subtitle
                    class="indigo--text font-weight-bold pa-0 ma-0 pl-1 mt-1"
                    >(빈 시간은 빈칸으로 두세요.)</v-card-subtitle
                  >
                </v-card-title>
              </v-col>
              <v-col cols="2" class="text-right pt-0 mr-2">
                <v-btn class="primary" large> 완료 </v-btn>
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
                {{ period }}교시
              </v-col>
              <v-col v-for="(weekday, idx) in weekdays" :key="idx" class="py-1">
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
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: () => ({
    place: '',
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
    ...mapState('classroomStore', ['periods', 'places'])
  }
}
</script>

<style scoped>
#checkboxLabel {
  color: indigo;
  font-size: 17px;
  font-weight: bold;
}

.v-card__title {
  font-size: 19px;
  font-weight: bolder;
}

.v-btn {
  font-size: 16px;
  font-weight: bolder;
}
</style>
