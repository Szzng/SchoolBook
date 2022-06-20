<template>
  <div>
    <v-dialog v-model="dialog.login" max-width="1200" persistent>
      <v-card class="px-3 pb-8">
        <v-row justify="end">
          <v-btn text @click="close" class="mt-5 pr-2">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-row>

        <v-row justify="center" align="center">
          <v-col sm="12" md="6">
            <v-card outlined min-height="350">
              <v-card-title class="success--text font-weight-bold pb-0">
                <v-icon class="mr-1" color="success" large>
                  mdi-human-greeting
                </v-icon>
                새로 오셨나요?
                <v-card-subtitle class="pb-0 pt-2">
                  안전한 사이트 이용을 위해
                  <strong>회원 가입 시 학교 IP 주소가 자동으로 등록</strong
                  >됩니다.<br />
                  이미 등록된 IP 주소는 변경 불가하니,
                  <strong>학교 컴퓨터를 이용하여 가입해주세요!</strong>
                </v-card-subtitle>
              </v-card-title>

              <v-form ref="registerform" lazy-validation>
                <v-card-text class="pt-1">
                  <v-checkbox
                    v-model="ipCheck1"
                    label="학교 컴퓨터를 이용하여 가입하고 있습니다."
                    class="mycheckbox ml-1 mb-2"
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
                    우리 학교 등록
                    <v-icon class="ml-3">mdi-bank-check</v-icon>
                  </v-btn>
                </v-card-text>
              </v-form>
            </v-card>
          </v-col>

          <v-col sm="12" md="6">
            <v-card outlined min-height="350">
              <v-card-title class="accent--text font-weight-bold pb-0">
                <v-icon class="mr-1" color="accent" large
                  >mdi-account-search</v-icon
                >
                이미 가입된 학교인가요?
                <v-card-subtitle class="pb-0 pt-2">
                  안전한 사이트 이용을 위해
                  <strong>회원 가입 시 등록된 학교 IP 주소와 일치</strong>해야
                  합니다.<br />
                  <strong>학교 컴퓨터를 이용하여 로그인해주세요!</strong>
                </v-card-subtitle>
              </v-card-title>

              <v-form ref="loginform" lazy-validation>
                <v-card-text class="pt-1">
                  <v-checkbox
                    v-model="ipCheck2"
                    label="학교 컴퓨터를 이용하여 로그인하고 있습니다."
                    class="mycheckbox ml-1 mb-2"
                    color="secondary"
                    :rules="ipRule"
                  >
                  </v-checkbox>
                  <v-text-field
                    v-model="loginName"
                    label="가입된 학교 이름을 입력하세요."
                    required
                    outlined
                    color="primary"
                    :rules="nameRule"
                  ></v-text-field>
                  <v-btn
                    color="accent"
                    x-large
                    block
                    class="font-weight-bold white--text"
                    style="font-size: 23px"
                    @click="login"
                  >
                    우리 학교로 이동
                    <v-icon class="ml-3">mdi-airplane-takeoff</v-icon>
                  </v-btn>
                </v-card-text>
              </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
    <SuccessDialog />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import SuccessDialog from '@/components/General/SuccessDialog.vue'
import api from '@/api/modules/accounts'

export default {
  components: { SuccessDialog },
  data: () => ({
    registerName: '',
    loginName: '',
    ipCheck1: false,
    ipCheck2: false,
    ipRule: [(v) => !!v || 'IP 주소를 위한 확인이 필요합니다.'],
    nameRule: [
      (v) => !!v || '학교 이름을 입력하세요.',
      (v) =>
        !/[~!@#$%^&*()_+|<>?:{}/]/.test(v) || '특수문자를 사용할 수 없습니다.',
      (v) => (v && v.length >= 3) || '학교 이름은 3글자 이상으로 지정해주세요.'
    ]
  }),

  computed: {
    ...mapState('generalStore', ['dialog'])
  },

  methods: {
    close () {
      this.dialog.login = false
      this.$refs.registerform.reset()
      this.$refs.loginform.reset()
      this.$refs.registerform.resetValidation()
      this.$refs.loginform.resetValidation()
    },

    register () {
      if (this.$refs.registerform.validate()) {
        api.register({ name: this.registerName })
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
>>> .mycheckbox .v-label {
  font-size: 16px;
  color: black;
  font-weight: bold;
}
</style>
