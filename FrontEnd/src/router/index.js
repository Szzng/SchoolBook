import Vue from 'vue'
import Router from 'vue-router'

import SettingTabs from '@/components/Setting/SettingTabs.vue'
import SetRoomPlaces from '@/components/Setting/SetRoomPlaces.vue'
import SetToolPlaces from '@/components/Setting/SetToolPlaces.vue'

import ToolPlaceTabs from '@/components/Tool/ToolPlaceTabs.vue'
import ToolCalendar from '@/components/Tool/ToolCalendar.vue'

import RoomCalendar from '@/components/Room/RoomCalendar.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/setting',
      component: SettingTabs,
      props: true,
      children: [
        { path: 'tool', component: SetToolPlaces },
        { path: 'room', component: SetRoomPlaces }
      ]
    },

    {
      path: '/room/:place',
      component: RoomCalendar,
      props: true
    },
    {
      path: '/tool',
      component: ToolPlaceTabs,
      props: true,
      children: [
        { path: ':place', component: ToolCalendar, props: true }
      ]
    }
  ]
})
