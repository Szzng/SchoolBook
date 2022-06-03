const classroomStore = {
  namespaced: true,
  state: {
    dialog: {
      checkRoomBooking: false,
      bookRoom: false,
      destroyRoomBooking: false,
      destroyRoom: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    places: [],
    focusDate: '',
    focusPlace: '',
    bookedRoomLists: [],
    availableBookingEvents: [],
    colors: ['red', 'indigo', 'deep-purple', 'pink', 'orange', 'green']
  },
  mutations: {
    focusDateSetter (state, date) {
      state.focusDate = date
    },
    focusPlaceSetter (state, place) {
      state.focusPlace = place
    }
  },
  actions: {
  }
}

export default classroomStore
