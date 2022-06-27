import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/General/Home.vue'

import SettingTabs from '@/components/Setting/SettingTabs.vue'
import SetRoom from '@/components/Setting/SetRoom.vue'
import SetTool from '@/components/Setting/SetTool.vue'

import ToolTabs from '@/components/Tool/ToolTabs.vue'
import ToolCalendar from '@/components/Tool/ToolCalendar.vue'

import RoomTabs from '@/components/Room/RoomTabs.vue'
import RoomCalendar from '@/components/Room/RoomCalendar.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/',
      component: Home},
    {
      path: '/:code',
      name: 'home',
      component: Home
    },
    {
      path: '/:code/setting',
      name: 'setting',
      component: SettingTabs,
      props: true,
      children: [
        { path: 'tool', name: 'settingTool', component: SetTool },
        { path: 'room', name: 'settingRoom', component: SetRoom }
      ]
    },

    {
      path: '/:code/tool',
      name: 'tool',
      component: ToolTabs,
      props: true,
      children: [
        { path: ':tool', component: ToolCalendar, props: true }
      ]
    },

    {
      path: '/:code/room',
      name: 'room',
      component: RoomTabs,
      props: true,
      children: [
        { path: ':room', component: RoomCalendar, props: true }
      ]
    }

  ]
})
