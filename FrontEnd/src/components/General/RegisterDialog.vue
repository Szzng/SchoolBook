<template>
  <div>
    <v-dialog v-model="dialog.register" max-width="1000" persistent>
      <v-card class="px-4 pb-8">
        <v-row justify="end">
          <v-btn text @click="close" class="mt-5 pr-2">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-row>

        <v-row justify="center" align="center" class="mt-0">
          <v-col cols="11">
            <v-card outlined min-height="380">
              <v-card-title
                class="success--text font-weight-bold pb-0 mt-2"
                style="font-size: 26px"
              >
                <v-icon class="mr-1" color="success" x-large>
                  mdi-human-greeting
                </v-icon>
                새로 오셨나요?
              </v-card-title>
              <v-card-subtitle
                class="success--text mt-3 ml-6"
                style="font-size: 20px"
              >
                안전한 사이트 이용을 위해
                <strong>회원 가입 시 학교별로 고유한 링크가 주어집니다.</strong>
                <v-icon class="ml-0" color="success" large>
                  mdi-link-variant
                </v-icon>
                <br />링크는 다시 확인할 수 없으니,
                <strong>링크를 복사하여 저장해주세요</strong>
                <v-icon class="ml-0" color="success" large>
                  mdi-content-save-alert-outline
                </v-icon>
              </v-card-subtitle>

              <v-form ref="registerform" lazy-validation>
                <v-card-text class="pt-0">
                  <v-checkbox
                    v-model="urlCheck"
                    label="발급되는 링크를 복사 후 즐겨찾기, 북마크, 메모 등등에 저장해놓겠습니다."
                    class="mycheckbox ml-6 mb-1 mt-0"
                    color="secondary"
                    :rules="ipRule"
                  >
                  </v-checkbox>
                  <v-text-field
                    v-model="registerName"
                    label="학교 이름을 입력하세요."
                    required
                    outlined
                    color="success"
                    class="mx-6"
                    :rules="nameRule"
                  ></v-text-field>
                  <v-btn
                    color="success"
                    x-large
                    block
                    class="font-weight-bold white--text"
                    style="font-size: 23px"
                    @click="register"
                  >
                    우리 학교 링크 발급
                    <v-icon class="ml-3">mdi-airplane-takeoff</v-icon>
                  </v-btn>
                </v-card-text>
              </v-form>
            </v-card>
          </v-col>
        </v-row>

        <v-row justify="center" align="center">
          <v-col cols="11">
            <v-card outlined min-height="190">
              <v-card-title
                class="accent--text font-weight-bold pb-0 mt-3"
                style="font-size: 26px"
              >
                <v-icon class="mr-1" color="accent" x-large>
                  mdi-account-search
                </v-icon>
                이미 가입한 학교인가요?
              </v-card-title>
              <v-card-subtitle
                class="accent--text mt-4 ml-6"
                style="font-size: 20px"
              >
                <strong>가입할 때 받으신 학교 링크</strong>로 접속해주세요.
                <v-icon class="ml-0" color="accent" large>
                  mdi-link-variant
                </v-icon>
                <br />
                <strong
                  >그 누구도 학교 링크를 저장해두지 않았다면, 다시 회원 가입해야
                  합니다.</strong
                ><v-icon class="ml-1 mb-1" color="accent" large>
                  mdi-emoticon-sad-outline
                </v-icon>
              </v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
    <RegisterSuccessDialog :name="name" :code="code" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import RegisterSuccessDialog from '@/components/General/RegisterSuccessDialog.vue'
import api from '@/api/modules/accounts'

export default {
  components: { RegisterSuccessDialog },
  data: () => ({
    registerName: '',
    loginName: '',
    urlCheck: false,
    ipRule: [(v) => !!v || 'IP 주소를 위한 확인이 필요합니다.'],
    nameRule: [
      (v) => !!v || '학교 이름을 입력하세요.',
      (v) =>
        !/[~!@#$%^&*()_+|<>?:{}/]/.test(v) || '특수문자를 사용할 수 없습니다.',
      (v) => (v && v.length >= 3) || '학교 이름은 3글자 이상으로 지정해주세요.'
    ],
    name: '',
    code: ''
  }),

  computed: {
    ...mapState('generalStore', ['dialog'])
  },

  methods: {
    close () {
      this.dialog.register = false
      this.$refs.registerform.reset()
      this.$refs.loginform.reset()
      this.$refs.registerform.resetValidation()
      this.$refs.loginform.resetValidation()
    },

    register () {
      if (this.$refs.registerform.validate()) {
        api.register({ name: this.registerName }, this)
        this.$refs.registerform.reset()
      }
    },

    login () {
      if (this.$refs.loginform.validate()) {
        api.login({ name: this.loginName })
        this.$refs.loginform.reset()
      }
    }
  }
}
</script>

<style scoped>
.v-card {
  border-width: 3px;
}

.mycheckbox >>> .v-label {
  font-size: 18px;
  color: black;
  font-weight: bold;
}
</style>
