import http from './request.js'

export default {
    getPostList() {
        return http.get('post/')
    },
    getPost(postId) {
        return http.get(`post/${postId}/`, {}, true)
    },
    createPost(params) {
        return http.post('post/', params, true)
    },
    deletePost(postId) {
        return http.delete(`post/${postId}/`, {}, true)
    },
    addComment(params) {
        return http.post('comment/', params, true)
    }
}