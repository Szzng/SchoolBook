<template>
  <div>
    <v-dialog v-model="dialog.destroyTool" max-width="500" persistent>
      <v-card>
        <v-card-title>
          <v-row align="center" justify="center">
            <v-btn
              color="primary"
              outlined
              x-large
              class="mx-1 mt-5 white--text font-weight-bold"
            >
              {{ tool }}
              <v-icon class="ml-1">mdi-progress-close</v-icon>
            </v-btn>
          </v-row>
        </v-card-title>
        <v-card-text>
          <v-row
            align="center"
            justify="center"
            class="mt-10 mb-3 black--text text-center font-weight-bold"
            style="font-size: 18px"
          >
            관련된 모든 예약 정보가 삭제됩니다. <br />
            정말 삭제하시겠어요?
          </v-row>
        </v-card-text>
        <v-card-actions class="pb-6">
          <v-spacer></v-spacer>
          <v-btn color="error" class="white--text" @click="destroyPlace"
            >삭제</v-btn
          >
          <v-btn @click="dialog.destroyTool = false">취소</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/setting'

export default {
  props: {
    tool: String
  },

  data: () => ({
    destroy: false
  }),

  computed: {
    ...mapState('toolStore', ['dialog'])
  },

  methods: {
    destroyPlace () {
      api.destroyTool(this.tool)
      this.dialog.destroyTool = false
    }
  }
}
</script>
