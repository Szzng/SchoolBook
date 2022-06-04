<template>
  <div class="mt-4">
    <v-sheet class="mx-16">
      <span style="font-size: 18px" class="black--text font-weight-bold">
        1. 등록된 교실 · 장소 수정
      </span>
      <v-card outlined class="mt-1 mb-5">
        <v-card-text>
          <v-btn
            v-for="place in places"
            :key="place.name"
            color="primary"
            outlined
            x-large
            elevation="3"
            class="mx-1 my-1 white--text font-weight-bold"
            @click="fixRoom(place.name)"
          >
            {{ place.name }}
            <v-icon class="ml-1">mdi-comment-edit-outline</v-icon>
          </v-btn>
        </v-card-text>
      </v-card>

      <span style="font-size: 18px" class="black--text font-weight-bold">
        2. 추가 등록
      </span>
      <v-card outlined class="mt-1 mb-5">
        <v-card-text>
          <v-form ref="form" lazy-validation>
            <v-card>
              <v-card-title>
                추가로 등록할 교실 · 장소는 모두 몇 개인가요?
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

            <v-row align="end" justify="start" class="my-5">
              <v-col cols="3" v-for="i in range" :key="i">
                <v-card>
                  <v-card-subtitle>
                    교실(장소){{ i + 1 }}의 이름을 입력하세요.
                  </v-card-subtitle>
                  <v-card-text>
                    <v-text-field
                      v-model="placesNames[i]"
                      :label="`${i + 1}번째`"
                      outlined
                      hide-details
                      :rules="placesNameRule"
                    ></v-text-field>
                  </v-card-text>
                </v-card>
              </v-col>
              <v-col class="text-right">
                <v-btn
                  :disabled="disabled"
                  @click="save"
                  class="primary"
                  x-large
                  >등록</v-btn
                >
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>
      </v-card>
    </v-sheet>

    <FixRoomDialog :roomToFix="roomToFix" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/setting'
import FixRoomDialog from '@/components/Setting/FixRoomDialog.vue'

export default {
  components: { FixRoomDialog },

  data: () => ({
    roomToFix: '',
    placesCount: 0,
    placesNames: [],
    placesCountRule: [
      (v) => !!v || '교실(장소)의 개수를 적어주세요.',
      (v) => (v && v >= 0) || '0보다 큰 수를 입력해주세요.'
    ],
    placesNameRule: [(v) => !!v || '교실(장소)의 이름을 입력하세요.']
  }),

  computed: {
    ...mapState('roomStore', ['dialog', 'periods', 'places']),
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
        const postData = {
          places: this.placesNames
        }
        api.setRoomPlaces(postData)
        this.$refs.form.reset()
      }
    },

    fixRoom (room) {
      this.roomToFix = room
      this.dialog.fixRoom = true
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
