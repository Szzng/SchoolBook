const DjangoBase = 'http://127.0.0.1:8000/'

export default {
  Django_API: `${DjangoBase}api/`,

  /* Book Tablets */
  tabletsAll: 'tablets/',
  tabletsByDate: (date) => {
    return `tablets/${date}/`
  },
  tabletDestroy: (tabletId) => {
    return `tablets/destroy/${tabletId}/`
  },
  tabletLeft: (date) => {
    return `tablets/left/${date}`
  }
}
