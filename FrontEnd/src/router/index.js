import Vue from 'vue'
import Router from 'vue-router'

import SettingTabs from '@/components/Setting/SettingTabs.vue'
import SetRoomPlaces from '@/components/Setting/SetRoomPlaces.vue'
import SetToolPlaces from '@/components/Setting/SetToolPlaces.vue'

import ToolTabs from '@/components/Tool/ToolTabs.vue'
import ToolCalendar from '@/components/Tool/ToolCalendar.vue'

import RoomTabs from '@/components/Room/RoomTabs.vue'
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
      path: '/tool',
      component: ToolTabs,
      props: true,
      children: [
        { path: ':tool', component: ToolCalendar, props: true }
      ]
    },

    {
      path: '/room',
      component: RoomTabs,
      props: true,
      children: [
        { path: ':room', component: RoomCalendar, props: true }
      ]
    }

  ]
})
