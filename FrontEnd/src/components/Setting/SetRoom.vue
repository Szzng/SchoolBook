<template>
  <div class="mt-4 mx-16">
    <v-card class="mx-10 mt-5" flat>
      <v-row justify="center" align="center">
        <v-card-title style="font-size: 22px" class="accent--text">
          <v-icon class="mr-2" large color="accent"
            >mdi-google-classroom</v-icon
          >
          교실 · 장소 등록 및 관리
          <v-icon class="ml-2" large color="accent"
            >mdi-google-classroom</v-icon
          >
        </v-card-title>
      </v-row>
    </v-card>

    <v-card class="my-10" outlined>
      <v-card-title>
        <v-row align="center" justify="start">
          <v-col sm="6" md="9" class="pb-0">
            <v-form ref="form" lazy-validation>
              <v-text-field
                v-model="newRoom"
                outlined
                label="교실 · 장소 이름을 입력하세요. (특수 문자 불가)"
                :rules="placeNameRule"
              ></v-text-field>
            </v-form>
          </v-col>
          <v-col sm="6" md="3" class="pl-0 pb-7">
            <v-btn
              :disabled="disabled"
              outlined
              x-large
              block
              color="success"
              elevation="3"
              @click="createTimetable"
              >기본 시간표 등록
              <v-icon class="ml-1">mdi-timetable</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card-title>
    </v-card>

    <v-card class="my-10" flat>
      <v-row>
        <v-col
          sm="6"
          md="4"
          v-for="place in rooms"
          :key="place.name"
          class="my-3"
        >
          <v-card outlined class="py-3 px-2">
            <v-row justify="center" align="center">
              <v-card-title style="font-size: 20px; font-weight: bolder">
                <v-icon class="mx-0 mb-1" large color="accent"
                  >mdi-cradle</v-icon
                >

                {{ place.name }}</v-card-title
              >
            </v-row>
            <v-row justify="center" align="center" class="mb-3 mt-5">
              <v-btn
                class="mr-2"
                width="120"
                height="45"
                outlined
                color="success"
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
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-card>

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
      (v) => (v && v.length <= 5) || '이름은 5글자 이하로 적어주세요.',
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
  color: success;
  font-weight: bolder;
}
</style>
