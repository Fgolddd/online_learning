import { createStore } from 'vuex';
import user from './modules/user';
import post from './modules/post';
import course from './modules/course';
import userInfo from './modules/userInfo';
import cart from './modules/cart';
import order from './modules/order'
export default createStore({
    modules: {
        user,
        post,
        course,
        userInfo,
        cart,
        order,
    },
});