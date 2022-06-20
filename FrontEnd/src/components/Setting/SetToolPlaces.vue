<template>
  <div class="mt-4">
    <v-sheet class="mx-16">
      <v-row align="start" justify="center">
        <v-col sm="12" md="6">
          <v-card class="mt-1 mb-5">
            <v-card-title>등록된 물품 · 교구 수정</v-card-title>
            <v-card-text class="mt-3">
              <v-card
                v-for="tool in tools"
                :key="tool.name"
                outlined
                class="py-2 mb-3"
              >
                <v-row align="center" justify="start">
                  <v-col sm="12" md="4" class="pl-7">
                    <span style="font-size: 18px; font-weight: bolder">
                      {{ tool.name }}</span
                    >
                  </v-col>

                  <v-col sm="12" md="8" class="text-right pr-6">
                    <v-btn
                      class="mr-2"
                      width="70"
                      height="45"
                      outlined
                      color="success"
                      elevation="2"
                      @click="updateTool(tool.name)"
                      >수정
                      <v-icon>mdi-cog-sync-outline</v-icon>
                    </v-btn>
                    <v-btn
                      width="70"
                      height="45"
                      outlined
                      color="secondary"
                      elevation="2"
                      @click="destroyTool(tool.name)"
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
            <v-card-title class="mb-3">물품 · 교구 추가 등록</v-card-title>
            <v-card-title>
              <v-form ref="form" lazy-validation>
                <v-row align="center" justify="start">
                  <v-col sm="4" md="12" class="py-0">
                    <v-text-field
                      v-model="newTool.name"
                      outlined
                      label=" 1. 이름을 입력하세요. (특수 문자 불가)"
                      :rules="nameRule"
                    ></v-text-field>
                  </v-col>
                  <v-col sm="4" md="12" class="py-0">
                    <v-text-field
                      v-model="newTool.quantity"
                      outlined
                      label="2. 총 수량을 입력하세요."
                      type="number"
                      :rules="quantityRule"
                    ></v-text-field>
                  </v-col>
                  <v-col sm="4" md="12" class="py-0">
                    <v-text-field
                      v-model="newTool.place"
                      outlined
                      label="3. 보관하는 장소를 입력하세요."
                      :rules="placeRule"
                    ></v-text-field>
                  </v-col>
                  <v-col sm="12" md="12">
                    <v-btn
                      :disabled="disabled"
                      outlined
                      x-large
                      block
                      color="success"
                      elevation="3"
                      height="56"
                      class="mb-3"
                      @click="createTool"
                      >등록
                      <v-icon class="ml-1">mdi-hammer-wrench</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
              </v-form>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-sheet>
    <DestroyToolDialog :tool="tool" />
    <UpdateToolDialog :tool="tool" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/setting'
import DestroyToolDialog from '@/components/Setting/DestroyToolDialog.vue'
import UpdateToolDialog from '@/components/Setting/UpdateToolDialog.vue'

export default {
  components: {
    DestroyToolDialog,
    UpdateToolDialog
  },

  data: () => ({
    tool: {},
    newTool: { name: '', quantity: '', place: '' },
    disabled: true,
    nameRule: [
      (v) => !!v || '이름을 입력하세요.',
      (v) =>
        !/[~!@#$%^&*()_+|<>?:{}/]/.test(v) || '특수문자를 사용할 수 없습니다.'
    ],
    quantityRule: [
      (v) => !!v || '수량을 입력하세요.',
      (v) => (v && v >= 0) || '0보다 큰 수를 입력해주세요.'
    ],
    placeRule: [
      (v) => !!v || '보관 장소를 입력하세요.',
      (v) =>
        !/[~!@#$%^&*()_+|<>?:{}/]/.test(v) || '특수문자를 사용할 수 없습니다.'
    ]
  }),

  watch: {
    newTool: {
      deep: true,
      handler () {
        if (this.$refs.form.validate()) {
          this.disabled = false
        } else {
          this.disabled = true
        }
      }
    }
  },

  computed: {
    ...mapState('toolStore', ['dialog', 'periods', 'tools'])
  },

  methods: {
    updateTool (tool) {
      api.getTool(this, tool)
    },

    destroyTool (tool) {
      this.tool.name = tool
      this.dialog.destroyTool = true
    },

    createTool () {
      api.createTool(this.newTool)
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
