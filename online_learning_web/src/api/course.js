import http from './request.js'

export default {
    getCourseList() {
        return http.get('course/')
    },
    getCourse(courseId) {
        return http.get(`course/${courseId}/`)
    },
    getVedio(vedioId) {
        return http.get(`course/video/${vedioId}/`, {}, true)
    }
}