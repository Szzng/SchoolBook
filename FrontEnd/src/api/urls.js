const DjangoBase = 'http://127.0.0.1:8000/'

export default {
  Django_API: `${DjangoBase}api/`,

  /* Setting */
  setting_toolPlaces: 'tool/setting/place/',
  setting_DestroytoolPlace: (placeName) => {
    return `tool/setting/place/${placeName}/`
  },
  setting_RoomPlaces: 'rooms/setting/place/',
  setting_DestroyRoomPlace: 'rooms/setting/place/destroy/',
  setting_FixedTimeTable: 'rooms/setting/fixedtimetable/',
  setting_ByPlaceFixedTimeTable: (placeName) => {
    return `rooms/setting/fixedtimetable/${placeName}/`
  },

  /* Tool */
  tool_All: 'tool/',
  tool_ByDate: (place, date) => {
    return `tool/${place}/${date}/`
  },
  tool_Destroy: (toolId) => {
    return `tool/${toolId}/`
  },
  tool_Left: (place, date) => {
    return `tool/left/${place}/${date}/`
  },

  /* Room */
  room_All: 'rooms/',
  room_ByDate: (date) => {
    return `rooms/${date}`
  },
  room_Destroy: (roomId) => {
    return `rooms/destroy/${roomId}/`
  },
  room_AvailableBookingEvents: (place, date) => {
    return `rooms/events/${place}/${date}/`
  },
  room_BookingByDate: (place, date) => {
    return `rooms/${place}/${date}/`
  }
}
