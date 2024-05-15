
import http from './request.js'

export default {
    getCouponList() {
        return http.get('/coupon/', {}, true)
    },
}