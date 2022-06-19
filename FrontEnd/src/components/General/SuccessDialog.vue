<template>
  <div>
    <v-dialog
      :retain-focus="false"
      v-model="dialog.success"
      max-width="460"
      persistent
    >
      <v-card class="px-3 py-5" min-height="200">
          <v-card-title class="font-weight-bold accent--text">
            환영합니다!
            <v-icon class="ml-1" color="purple darken-2" large> mdi-human-greeting </v-icon>
            <v-card-subtitle class="px-0 py-5 black--text" style="font-size:16px; font-weight:bold;">{{ successMsg }}</v-card-subtitle>
          </v-card-title>
        <v-card-actions class="pb-3">
          <v-btn
            block
            color="purple darken-2"
            class="white--text"
            x-large
            @click="dialog.success = false"
          >
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState('generalStore', ['dialog', 'successMsg'])
  }
}
</script>
