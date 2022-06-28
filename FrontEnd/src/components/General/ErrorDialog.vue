<template>
  <div>
    <v-dialog
      :retain-focus="false"
      v-model="dialog.error"
      max-width="550"
      persistent
    >
      <v-card class="px-3 py-5" min-height="200">
        <v-row justify="center" align="center" class="pt-4">
          <v-icon class="ml-1" color="error" large>mdi-alert-outline </v-icon>
        </v-row>

        <v-row justify="center" align="center" class="pt-0 pb-3">
        <v-card-title class="error--text text-center">
          {{ errorMsg }}
        </v-card-title>
        </v-row>

        <v-card-actions class="pb-3">
          <v-btn
            block
            color="error"
            class="white--text"
            x-large
            @click="dialog.error = false"
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
    ...mapState('generalStore', ['dialog', 'errorMsg'])
  }
}
</script>
