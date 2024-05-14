
import http from './request.js'

export default {
    getCartList() {
        return http.get('cart/', {}, true)
    },
    addItem(id) {
        return http.post('cart/', {
            course: id
        }, true)
    },
    deleteItem(id) {
        return http.delete(`cart/${id}/`, {}, true)
    },

}