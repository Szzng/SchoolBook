<template>
  <div>
    <v-dialog v-model="dialog.logout" max-width="460" persistent>
      <v-card class="px-3 py-5" min-height="200">
        <v-row justify="end">
          <v-btn text @click="dialog.logout = false" class="mt-3 pr-5">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-row>

        <v-row justify="center" class="mb-3">
          <v-card-title class="font-weight-bold error--text">
            <v-icon class="mr-1" color="error" large>
              mdi-human-greeting
            </v-icon>
            로그아웃 하시겠어요?
          </v-card-title>
        </v-row>
        <v-card-actions class="py-3">
          <v-btn
            block
            color="error"
            class="white--text"
            x-large
            @click="logout"
          >
            로그아웃
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/modules/accounts'

export default {
  computed: {
    ...mapState('generalStore', ['dialog'])
  },

  methods: {
    logout () {
      api.logout()
    }
  }
}
</script>
