import axios from "axios";
import { toast } from "bulma-toast";

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
    async deleteItem({ commit }, id) {
        try {
            await axios.delete(`cart/${id}/`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            });
            toast({
                message: '删除成功',
                type: 'is-danger',
                position: 'top-center',
                duration: 3000,
            });
            commit('deleteItem', id);
        } catch (error) {
            console.error(error);
        }


    }
};

const mutations = {
    setCart(state, cart) {
        state.cart = cart;
    },
    deleteItem(state, id) {
        state.cart = state.cart.filter((item) => item.id !== id);
    },
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations,
};