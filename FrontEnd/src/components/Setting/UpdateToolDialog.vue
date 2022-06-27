<template>
  <div>
    <v-dialog v-model="dialog.updateTool" max-width="550" persistent>
      <v-card class="px-3">
        <v-card-title>
          <v-row align="center" justify="center">
            <v-btn
              color="success"
              outlined
              x-large
              class="mx-1 mt-5 white--text font-weight-bold"
            >
              <v-icon class="mr-1">mdi-progress-alert</v-icon>
              {{ tool.name }}
            </v-btn>
            <v-btn
              color="success"
              outlined
              x-large
              class="mx-1 mt-5 white--text font-weight-bold"
            >
              <v-icon class="mr-1">mdi-progress-alert</v-icon>

              {{ tool.quantity }}개
            </v-btn>
            <v-btn
              color="success"
              outlined
              x-large
              class="mx-1 mt-5 white--text font-weight-bold"
            >
              <v-icon class="mr-1">mdi-progress-alert</v-icon>

              {{ tool.place }}
            </v-btn>
          </v-row>
        </v-card-title>

        <v-card-title class="mt-8 pb-0">
          <v-form ref="form" lazy-validation>
            <v-row align="center" justify="center" class="mr-3">
              <v-col sm="4" md="12" class="py-0">
                <v-text-field
                  v-model="toolToUpdate.name"
                  outlined
                  label="이름 수정 불가능"
                  disabled
                ></v-text-field>
              </v-col>
              <v-col sm="4" md="12" class="py-0">
                <v-text-field
                  v-model="toolToUpdate.quantity"
                  outlined
                  label="총수량"
                  :rules="quantityRule"
                ></v-text-field>
              </v-col>
              <v-col sm="4" md="12" class="py-0">
                <v-text-field
                  v-model="toolToUpdate.place"
                  outlined
                  label="보관 장소"
                  :rules="placeRule"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-form>
        </v-card-title>

        <v-card-text>
          <v-row
            align="center"
            justify="center"
            class="mt-4 mb-3 black--text text-center font-weight-bold"
            style="font-size: 18px"
          >
            관련된 모든 예약에 영향을 미칠 수 있습니다. <br />
            정말 수정하시겠어요?
          </v-row>
        </v-card-text>

        <v-card-actions class="pb-6">
          <v-spacer></v-spacer>
          <v-btn
            color="success lighten-1"
            class="white--text"
            @click="updateTool"
            >수정</v-btn
          >
          <v-btn @click="dialog.updateTool = false">취소</v-btn>
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
    tool: Object
  },

  data: () => ({
    toolToUpdate: {},
    disabled: true,
    nameRule: [
      (v) =>
        !/[~!@#$%^&*()_+|<>?:{}/]/.test(v) || '특수문자를 사용할 수 없습니다.'
    ],
    quantityRule: [
      (v) => !!v || '수량을 입력하세요.',
      (v) => v >= 0 || '0보다 큰 수를 입력해주세요.'
    ],
    placeRule: [
      (v) => !!v || '보관 장소를 입력하세요.',
      (v) => (v && v.length <= 5) || '5글자 이하로 적어주세요.',
      (v) =>
        !/[~!@#$%^&*()_+|<>?:{}/]/.test(v) || '특수문자를 사용할 수 없습니다.'
    ]
  }),

  computed: {
    ...mapState('toolStore', ['dialog'])
  },

  watch: {
    tool () {
      this.toolToUpdate = Object.assign({}, this.tool)
    }
  },

  methods: {
    updateTool () {
      api.updateTool(this.toolToUpdate, this.tool.name)
      this.dialog.updateTool = false
    }
  }
}
</script>
