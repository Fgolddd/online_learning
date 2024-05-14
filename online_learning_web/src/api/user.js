
import http from './request.js'

export default {
    login(form) {
        return http.post('user/login/', form)
    },
    register(form) {
        return http.post('user/register/', form)
    },
    getUserInfo(id) {
        return http.get(`user/info/${id}`, {}, true)
    },

}