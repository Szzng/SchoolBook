<template>
  <div>
    <v-dialog v-model="dialog.fixRoom" max-width="530" persistent>
      <v-card>
        <v-row justify="end" class="pt-5 mr-1">
          <v-btn text @click="dialog.fixRoom = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-row>
        <v-card-title>
          <v-row align="center" justify="center">
            <v-btn
              color="primary"
              outlined
              x-large
              class="mx-1 mt-3 white--text font-weight-bold"
            >
              {{ roomToFix }}
              <v-icon class="ml-1">mdi-comment-question-outline</v-icon>
            </v-btn>
          </v-row>
        </v-card-title>

        <v-card-actions class="pb-10 mt-12">
          <v-row justify="center" align="center">
            <v-btn
              class="mx-3"
              outlined
              large
              color="indigo"
              elevation="3"
              @click="fixTimetable"
              >기본 시간표 수정
              <v-icon class="ml-1">mdi-timetable</v-icon>
            </v-btn>
            <v-btn
              class="mx-3"
              outlined
              large
              color="indigo"
              elevation="3"
              @click="dialog.destroyRoom = true"
              >삭제
              <v-icon class="ml-1">mdi-delete-alert-outline</v-icon>
            </v-btn>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <DestroyRoomDialog :room="roomToFix" />
    <FixTimetableDialog :room="roomToFix" :fixedTimetable="fixedTimetable" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/setting'
import DestroyRoomDialog from '@/components/Setting/DestroyRoomDialog.vue'
import FixTimetableDialog from '@/components/Setting/FixTimetableDialog.vue'

export default {
  components: { DestroyRoomDialog, FixTimetableDialog },

  props: {
    roomToFix: String
  },

  data: () => ({
    fixedTimetable: {
      0: ['', '', '', '', '', ''],
      1: ['', '', '', '', '', ''],
      2: ['', '', '', '', '', ''],
      3: ['', '', '', '', '', ''],
      4: ['', '', '', '', '', '']
    }
  }),

  computed: {
    ...mapState('roomStore', ['dialog'])
  },

  methods: {
    fixTimetable () {
      api.getFixedTimeTable(this, this.roomToFix)
    }
  }
}
</script>
