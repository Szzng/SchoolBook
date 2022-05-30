const classroomStore = {
  namespaced: true,
  state: {
    dialog: {
      checkRoomBooking: false,
      bookRoom: false,
      destroyRoomBooking: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    places: ['강당', '컴퓨터1실', '컴퓨터2실'],
    focusDate: '',
    focusPlace: '',
    bookedRoomLists: [],
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
