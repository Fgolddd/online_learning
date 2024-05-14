import axios from "axios";

const namespaced = true;

const state = () => ({
    posts: [],
});

const getters = {
    getPosts: (state) => state.posts,
    getPostById: (state) => (id) => state.posts.find((post) => post.id === id),
};

const actions = {
    async fetchPosts({ commit }) {
        // 使用实际的API URL替换此处的占位符
        const response = await axios.get('post/')
        commit('setPosts', response.data);
    },
};

const mutations = {
    setPosts(state, posts) {
        state.posts = posts;
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};