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
    places: [{ name: '전산실' }, { name: '준비물실' }],
    focusDate: '',
    focusPlace: '',
    bookedToolLists: [],
    left: [],
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

export default toolStore
