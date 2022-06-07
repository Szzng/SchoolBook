const toolStore = {
  namespaced: true,
  state: {
    dialog: {
      checkToolBooking: false,
      bookTool: false,
      destroyToolBooking: false,
      updateTool: false,
      destroyTool: false
    },
    periods: [1, 2, 3, 4, 5, 6],
    tools: [],
    focusDate: '',
    focusTool: '',
    toolBookingLists: {},
    left: [],
    colors: ['red', 'indigo', 'deep-purple', 'pink', 'orange', 'green']
  },
  mutations: {
    focusDateSetter (state, date) {
      state.focusDate = date
    },
    focusToolSetter (state, tool) {
      state.focusTool = tool
    }
  },
  actions: {
  }
}

export default toolStore
