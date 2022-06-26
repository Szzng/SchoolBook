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
                <v-card-subtitle class="pb-0 pt-5">
                  <strong
                    >회원 가입 시 학교별로 고유한 링크가 자동으로 발급</strong
                  >됩니다. 한 번 발급된 링크는 다시 확인할 수 없으니,
                  <strong>꼭 발급되는 링크를 복사하여 저장해주세요!</strong>
                </v-card-subtitle>
              </v-card-title>

              <v-form ref="registerform" lazy-validation>
                <v-card-text class="pt-0">
                  <v-checkbox
                    v-model="urlCheck"
                    label="아하! 지금 발급되는 학교 링크를 복사하여 저장해두어야 하는군요?!"
                    class="mycheckbox ml-1 mb-2 mt-2"
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
                    우리 학교 링크 발급
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
                <v-card-subtitle class="pb-0 pt-5">
                  안전한 사이트 이용을 위해
                  <strong>회원 가입 시 발급된 학교 링크</strong>로 접속해주세요.
                  <strong
                    >아무도 학교 링크를 모른다면, 다시 회원 가입하여 설정해야
                    합니다.</strong
                  >
                </v-card-subtitle>
              </v-card-title>

              <v-form ref="loginform" lazy-validation>
                <v-card-text class="pt-16">
                  <v-text-field
                    v-model="loginName"
                    label="회원 가입 시 발급된 학교 링크를 입력하세요."
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
    urlCheck: false,
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
