<template>
  <div class="mt-4">
    <v-sheet class="mx-16">
      <v-row align="start" justify="center">
        <v-col sm="12" md="6">
          <v-card class="mt-1 mb-5">
            <v-card-title>등록된 교실 · 장소 수정</v-card-title>
            <v-card-text class="mt-3">
              <v-card
                v-for="place in rooms"
                :key="place.name"
                outlined
                class="py-2 mb-3"
              >
                <v-row align="center" justify="start">
                  <v-col sm="12" md="4" class="pl-7">
                    <span style="font-size: 18px; font-weight: bolder">
                      {{ place.name }}</span
                    >
                  </v-col>

                  <v-col sm="12" md="8" class="text-right pr-6">
                    <v-btn
                      class="mr-2"
                      width="120"
                      height="45"
                      outlined
                      color="indigo"
                      elevation="2"
                      @click="updateTimetable(place.name)"
                      >기본 시간표
                      <v-icon>mdi-timetable</v-icon>
                    </v-btn>
                    <v-btn
                      width="70"
                      height="45"
                      outlined
                      color="secondary"
                      elevation="2"
                      @click="destroyRoom(place.name)"
                      >삭제
                      <v-icon>mdi-delete-alert-outline</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
              </v-card>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col sm="12" md="6">
          <v-card class="mt-1 mb-5">
            <v-card-title>교실 · 장소 추가 등록</v-card-title>
            <v-card-title>
              <v-row align="center" justify="start">
                <v-col sm="6" md="12">
                  <v-form ref="form" lazy-validation>
                    <v-text-field
                      v-model="newRoom"
                      outlined
                      label="교실 · 장소 이름을 입력하세요. (특수 문자 불가)"
                      :rules="placeNameRule"
                    ></v-text-field>
                  </v-form>
                </v-col>
                <v-col sm="6" md="12">
                  <v-btn
                    :disabled="disabled"
                    outlined
                    x-large
                    block
                    color="indigo"
                    elevation="3"
                    @click="createTimetable"
                    >기본 시간표 등록
                    <v-icon class="ml-1">mdi-timetable</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-sheet>
    <UpdateTimetableDialog :room="room" />
    <DestroyRoomDialog :room="room" />

    <CreateTimetableDialog :room="propsRoom" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/setting'
import DestroyRoomDialog from '@/components/Setting/DestroyRoomDialog.vue'
import UpdateTimetableDialog from '@/components/Setting/UpdateTimetableDialog.vue'

import CreateTimetableDialog from '@/components/Setting/CreateTimetableDialog.vue'

export default {
  components: {
    DestroyRoomDialog,
    UpdateTimetableDialog,
    CreateTimetableDialog
  },

  data: () => ({
    room: '',
    newRoom: '',
    propsRoom: '',
    disabled: true,
    placeNameRule: [
      (v) => !!v || '이름을 입력하세요.',
      (v) =>
        !/[~!@#$%^&*()_+|<>?:{}/]/.test(v) || '특수문자는 사용할 수 없습니다.'
    ]
  }),

  watch: {
    newRoom () {
      if (this.$refs.form.validate()) {
        this.disabled = false
      } else {
        this.disabled = true
      }
    }
  },

  computed: {
    ...mapState('roomStore', ['dialog', 'periods', 'rooms'])
  },

  methods: {
    updateTimetable (room) {
      this.room = room
      api.getTimetable(this.room)
    },

    destroyRoom (room) {
      this.room = room
      this.dialog.destroyRoom = true
    },

    createTimetable () {
      this.propsRoom = this.newRoom
      this.dialog.createTimetable = true
      this.$refs.form.reset()
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
