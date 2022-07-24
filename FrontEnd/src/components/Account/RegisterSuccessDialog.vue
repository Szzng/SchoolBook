<template>
  <div>
    <v-dialog
      :retain-focus="false"
      v-model="dialog.registerSuccess"
      max-width="600"
      persistent
    >
      <v-card class="px-3 py-7" min-height="200">
        <v-row justify="center" align="center" class="pt-4">
          <v-icon class="ml-1" color="success" large>mdi-human-handsup </v-icon>
          <span style="font-size: 20px" class="success--text"
            >{{ name }}님, 환영합니다!</span
          >
          <v-icon class="mr-1" color="success" large>mdi-human-handsup </v-icon>
        </v-row>

        <v-row justify="center" align="center" class="pt-0 pb-3">
          <v-card-title class="success--text text-center">
            <strong
              >아래 링크를 복사하여 저장·공유하세요.<br />
              이 링크는 다시는 확인할 수 없습니다.
            </strong>
          </v-card-title>
        </v-row>

        <v-card-title>
          <v-row justify="center" align="center" class="mx-5">
            <v-text-field
              v-model="link"
              outlined
              label="복사하여 어딘가에 저장 · 공유하세요."
              hide-details
              readonly
            ></v-text-field>
            <v-btn icon @click="copy"><v-icon>mdi-content-copy</v-icon></v-btn>
          </v-row>
        </v-card-title>

        <v-card-actions class="mt-3">
          <v-row justify="center" align="center" class="mx-6" dense>
            <v-col sm="12" md="6">
              <v-btn @click="copy" block x-large color="error">학교 링크 복사</v-btn>
            </v-col>
            <v-col sm="12" md="6">
              <v-btn @click="moveToLink" block x-large color="success" >학교 링크로 이동</v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
  props: {
    name: String,
    code: String
  },

  computed: {
    ...mapState('generalStore', ['dialog', 'successMsg']),
    link () {
      return `http://localhost:8080/${this.code}`
    }
  },

  methods: {
    copy () {
      navigator.clipboard
        .writeText(this.link)
        .then(() => {
          const msg = '학교 링크 복사 완료! 어디든지 붙여 넣으세요! (Ctrl + v)'
          this.$store.commit('generalStore/successMsgSetter', msg)
          this.dialog.success = true
        })
        .catch((err) => {
          console.log('Something went wrong', err)
        })
    },

    moveToLink () {
      navigator.clipboard
        .writeText(this.link)
        .then(() => {
          this.dialog.registerSuccess = false
          window.open(this.link, '_parent')
        })
        .catch((err) => {
          console.log('Something went wrong', err)
        })
    }
  }
}
</script>
