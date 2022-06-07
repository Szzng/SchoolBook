const DjangoBase = 'http://127.0.0.1:8000/'

export default {
  Django_API: `${DjangoBase}api/`,

  /* Setting_Tool */
  setting_Tool: 'tools/setting/',
  setting_DestroyTool: 'tools/setting/destroy/',

  /* Setting_Room */
  setting_Room: 'rooms/setting/',
  setting_DestroyRoom: 'rooms/setting/destroy/',
  setting_UpdateTimetable: 'rooms/setting/timetable/',
  setting_TimetableByRoom: (room) => {
    return `rooms/setting/timetable/${room}/`
  },

  /* Tool */
  tool_All: 'tools/',
  tool_BookingByDate: (tool, date) => {
    return `tools/${tool}/${date}/`
  },
  tool_DestroyBooking: (bookingId) => {
    return `tools/${bookingId}/`
  },
  tool_Left: (tool, date) => {
    return `tools/left/${tool}/${date}/`
  },

  /* Room */
  room_All: 'rooms/',
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
