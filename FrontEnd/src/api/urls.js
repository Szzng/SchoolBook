const DjangoBase = 'http://127.0.0.1:8000/'

export default {
  Django_API: `${DjangoBase}api/`,

  /* Tablets */
  allBookedTablets: 'tablets/',
  bookedTabletsByDate: (date) => {
    return `tablets/${date}/`
  }
}
