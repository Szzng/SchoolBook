<template>
  <div class="mx-10 mt-16 pt-1">
    <v-carousel
      cycle
      height="350"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item v-for="(slide, i) in slides" :key="i">
        <v-sheet :color="colors[i]" height="100%">
          <v-row class="fill-height" align="center" justify="center">
            <div class="text-h2">
              {{ slide }}
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>

    <v-sheet height="300" color="black" class="white--text">
      1. 회원 가입/ 로그인 2. 기본 설정 3. 예약
    </v-sheet>
  </div>
</template>

<script>
export default {
  data: () => ({
    colors: [
      'indigo',
      'warning',
      'pink darken-2',
      'red lighten-1',
      'deep-purple accent-4'
    ],
    slides: [
      '학교의 모든 예약, 스쿨북 School Book',
      '학교의 모든 예약, 스쿨북 School Book',
      '학교의 모든 예약, 스쿨북 School Book',
      '학교의 모든 예약, 스쿨북 School Book',
      '학교의 모든 예약, 스쿨북 School Book'
    ]
  })
}
</script>
