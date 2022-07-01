const generalStore = {
  namespaced: true,
  state: {
    dialog: {
      success: false,
      error: false,
      registerSuccess: false,
      register: false,
      logout: false
    },
    successMsg: '',
    errorMsg: '',
    access: {token: '', exp: ''},
    school: { name: 'Guest' },
    code: ' '
  },

  mutations: {
    successMsgSetter (state, msg) {
      state.successMsg = msg
    }
  }
}

export default generalStore
