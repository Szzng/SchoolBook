<template>
  <div class="mt-4 mx-16">
    <v-card class="mx-10 mt-5" flat>
      <v-row justify="center" align="center">
        <v-card-title style="font-size: 22px" class="accent--text">
          <v-icon class="mr-2" large color="accent">mdi-tablet-cellphone</v-icon>
          물품 · 교구 등록 및 관리
          <v-icon class="ml-2" large color="accent"
            >mdi-tablet-cellphone</v-icon
          >
        </v-card-title>
      </v-row>
    </v-card>

    <v-card class="my-10" outlined>
      <v-card-title class="">
        <v-row align="center" justify="center" class="ml-0 mr-7">
          <v-col sm="6" md="11" class="pb-0">
            <v-form ref="form" lazy-validation>
              <v-row align="center" justify="start" class="ma-0">
                <v-col sm="4" md="4" class="py-0">
                  <v-text-field
                    v-model="newTool.name"
                    outlined
                    label=" 1. 이름을 입력하세요. (특수 문자 불가)"
                    :rules="nameRule"
                  ></v-text-field>
                </v-col>
                <v-col sm="4" md="4" class="py-0">
                  <v-text-field
                    v-model="newTool.quantity"
                    outlined
                    label="2. 총 수량을 입력하세요."
                    type="number"
                    :rules="quantityRule"
                  ></v-text-field>
                </v-col>
                <v-col sm="4" md="4" class="py-0">
                  <v-text-field
                    v-model="newTool.place"
                    outlined
                    label="3. 보관하는 장소를 입력하세요."
                    :rules="placeRule"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-form>
          </v-col>
          <v-col sm="1" md="1" class="pl-0 pb-7">
            <v-btn
              :disabled="disabled"
              outlined
              x-large
              block
              color="success"
              elevation="3"
              height="56"
              @click="createTool"
              >등록
              <v-icon class="ml-1">mdi-hammer-wrench</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card-title>
    </v-card>

    <v-card class="my-10" flat>
      <v-row>
        <v-col v-for="tool in tools" :key="tool.name" class="py-2 mb-3">
          <v-card outlined class="py-3 px-2">
            <v-row justify="center" align="center">
              <v-card-title style="font-size: 20px; font-weight: bolder">
                <v-icon class="mx-0 mr-2" size="30" color="accent"
                  >mdi-desktop-mac</v-icon
                >

                {{ tool.name }}</v-card-title
              >
            </v-row>
            <v-row justify="center" align="center" class="mb-3 mt-5">
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
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-card>

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
      (v) => (v && v.length <= 5) || '이름은 5글자 이하로 적어주세요.',
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
