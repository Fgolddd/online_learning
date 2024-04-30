import axios from "axios";

const namespaced = true;

const state = () => ({
    cart: [],
});

const getters = {
    getCart: (state) => state.cart,
    // 在Vuex store的getters对象中定义
    getCourseById: (state) => (id) => state.cart.find((course) => course.id === id),
};

const actions = {
    async fetchCart({ commit }) {
        // 使用实际的API URL替换此处的占位符
        const response = await axios.get('cart/', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
            },
        })
        commit('setCart', response.data);

    },
};

const mutations = {
    setCart(state, cart) {
        state.cart = cart;
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};