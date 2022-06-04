const toolStore = {
  namespaced: true,
  state: {
    dialog: {
      checkToolBooking: false,
      bookTool: false,
      destroyToolBooking: false,
      destroyTool: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    rooms: [{ name: '전산실' }, { name: '준비물실' }],
    focusDate: '',
    focusRoom: '',
    bookedToolLists: [],
    left: [],
    colors: ['red', 'indigo', 'deep-purple', 'pink', 'orange', 'green']
  },
  mutations: {
    focusDateSetter (state, date) {
      state.focusDate = date
    },
    focusPlaceSetter (state, place) {
      state.focusRoom = place
    }
  },
  actions: {
  }
}

export default toolStore
