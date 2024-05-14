
import http from './request.js'

export default {
    getOrderList() {
        return http.get('order/', {}, true)
    },
    createOrder() {
        return http.post('order/', {}, true)
    },
    removeOrder(orderId) {
        return http.delete(`order/${orderId}`, true)
    }

}