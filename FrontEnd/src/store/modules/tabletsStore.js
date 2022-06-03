const tabletsStore = {
  namespaced: true,
  state: {
    dialog: {
      checkTabletsBooking: false,
      bookTablets: false,
      destroyTablet: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    places: [{ name: '전산실' }, { name: '준비물실' }],
    focusDate: '',
    focusPlace: '',
    bookedTabletsLists: [],
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

export default tabletsStore
