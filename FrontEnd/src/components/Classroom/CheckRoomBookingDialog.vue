<template>
  <div class="mt-2 mr-10">
    <v-sheet v-show="dialog.checkRoomBooking" height="581" outlined class="mt-5">
      <v-card class="pl-5" flat>
        <v-card-actions class="mb-5">
          <v-spacer></v-spacer>
           <v-card-title class="pl-0 pt-1"
            >{{ formatSelectedDate }}
            <v-card-subtitle class="purple--text ma-0 pa-0 pl-1 pt-2">
              {{ focusPlace }}</v-card-subtitle
            >
          </v-card-title>
          <v-spacer></v-spacer>
          <v-btn color="primary" class="pr-0 mr-1">
            예약
            <v-icon left class="ml-0"> mdi-clock-plus-outline </v-icon>
          </v-btn>
        </v-card-actions>

        <v-card v-for="period in periods" :key="period" flat class="my-0 py-0">
          <v-row align="center" justify="center">
            <v-col sm="12" md="5">
              <v-card-subtitle class="pb-3 black--text">
                {{ period }}교시
              </v-card-subtitle>
            </v-col>

             <v-col class="pa-0">
              <v-card-text>
                  <v-chip
                    v-if="[2, 3, 4].includes(period)"
                    color="primary"
                    outlined
                    large
                  >
                    <v-avatar left>
                      <v-icon>mdi-checkbox-marked-circle</v-icon>
                    </v-avatar>
                    예약자
                  </v-chip>
              </v-card-text>
            </v-col>

          </v-row>
          <v-divider class="my-3 ml-3 mr-7"></v-divider>
        </v-card>
      </v-card>
    </v-sheet>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  components: {},

  data: () => ({
    colors: ['orange', 'pink', 'deep-purple', 'cyan', 'green', 'indigo']
  }),

  computed: {
    ...mapState('classroomStore', ['dialog', 'periods', 'focusDate', 'focusPlace']),

    formatSelectedDate () {
      const date = this.focusDate.split('-')
      return date[1] + '월  ' + date[2] + '일'
    }
  },

  methods: {}
}
</script>
