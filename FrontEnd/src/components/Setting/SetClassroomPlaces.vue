<template>
  <div class="mt-4">
    <v-sheet class="mx-16">
      <v-form ref="form" lazy-validation>
        <v-row justify="center">
          <v-col cols="6">
            <v-card>
              <v-card-title>
                Q. 예약 시스템을 사용할 교실(장소)은 모두 몇 개인가요?
              </v-card-title>
              <v-card-text>
                <v-text-field
                  v-model="placesCount"
                  label="0 이상의 정수를 입력해주세요."
                  filled
                  dense
                  hide-details
                  :rules="placesCountRule"
                ></v-text-field>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row align="end" justify="start" class="my-5">
          <v-col cols="3" v-for="i in range" :key="i">
            <v-card>
              <v-card-subtitle>
                교실(장소){{ i + 1 }}의 이름을 입력하세요.
              </v-card-subtitle>
              <v-card-text>
                <v-text-field
                  v-model="placesName[i]"
                  :label="`${i + 1}번째`"
                  outlined
                  hide-details
                  :rules="placesNameRule"
                ></v-text-field>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col class="text-right">
            <v-btn :disabled="disabled" @click="save" class="primary" x-large
              >완료</v-btn
            >
          </v-col>
        </v-row>
      </v-form>
    </v-sheet>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data: () => ({
    placesCount: 0,
    placesName: [],
    placesCountRule: [
      (v) => !!v || '교실(장소)의 개수를 적어주세요.',
      (v) => (v && v >= 0) || '0보다 큰 수를 입력해주세요.'
    ],
    placesNameRule: [(v) => !!v || '교실(장소)의 이름을 입력하세요.']
  }),

  computed: {
    ...mapState('classroomStore', ['periods']),
    range () {
      return [...Array(Number(this.placesCount)).keys()]
    },

    disabled () {
      if (this.placesCount > 0) {
        return false
      } else {
        return true
      }
    }
  },

  methods: {
    save () {
      if (this.$refs.form.validate()) {
        // const postData = {
        //   placesName: this.placesName
        // }
        // api.BookTablets(this, postData)
        this.$refs.form.reset()
      }
    }
  }
}
</script>

<style scoped>
.v-card__title {
  font-size: 19px;
  color: indigo;
  font-weight: bolder;
}
</style>
