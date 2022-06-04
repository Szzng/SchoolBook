const DjangoBase = 'http://127.0.0.1:8000/'

export default {
  Django_API: `${DjangoBase}api/`,

  /* Setting_Tool */
  setting_toolPlaces: 'tools/setting/place/',
  setting_DestroytoolPlace: (placeName) => {
    return `tools/setting/place/${placeName}/`
  },

  /* Setting_Room */
  setting_Room: 'rooms/setting/',
  setting_DestroyRoom: 'rooms/setting/destroy/',
  setting_UpdateTimetable: 'rooms/setting/timetable/',
  setting_TimetableByRoom: (room) => {
    return `rooms/setting/timetable/${room}/`
  },

  /* Tool */
  tool_All: 'tools/',
  tool_ByDate: (place, date) => {
    return `tools/${place}/${date}/`
  },
  tool_Destroy: (toolId) => {
    return `tools/${toolId}/`
  },
  tool_Left: (place, date) => {
    return `tools/left/${place}/${date}/`
  },

  /* Room */
  room_All: 'rooms/',
  room_ByDate: (date) => {
    return `rooms/${date}`
  },
  room_Destroy: (roomId) => {
    return `rooms/destroy/${roomId}/`
  },
  room_AvailableEvents: (room, date) => {
    return `rooms/events/${room}/${date}/`
  },
  room_BookingByDate: (room, date) => {
    return `rooms/${room}/${date}/`
  }
}
