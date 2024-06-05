import axios from "axios";
import { useRouter } from "vue-router";
import { toast } from "bulma-toast";


const router = useRouter();

const http = {
    // 请求方法
    request(config) {
        // 调用请求拦截器
        config = beforeRequest(config);

        // 创建axios实例并发送请求
        if (config.method == "GET") {
            return axios.get(config.url, {
                params: config.data,
                headers: config.headers
            }).then(response => {
                // 调用响应拦截器
                const resp = beforeResponse(response);
                return resp;
            }).catch(error => {
                // 调用异常处理的方法
                errorHandle(error);
                throw error; // 重新抛出错误以便外部处理
            });
        } else if (config.method == "POST") {
            return axios.post(config.url, config.data, {
                headers: config.headers
            }).then(response => {
                // 调用响应拦截器
                const resp = beforeResponse(response);
                return resp;
            }).catch(error => {
                // 调用异常处理的方法
                errorHandle(error);
                throw error; // 重新抛出错误以便外部处理
            });
        } else if (config.method == "PUT") {
            return axios.put(config.url, config.data, {
                headers: config.headers
            }).then(response => {
                // 调用响应拦截器
                const resp = beforeResponse(response);
                return resp;
            }).catch(error => {
                // 调用异常处理的方法
                errorHandle(error);
                throw error; // 重新抛出错误以便外部处理
            });
        } else if (config.method == "DELETE") {
            return axios.delete(config.url, {
                params: config.data,
                headers: config.headers
            }).then(response => {
                // 调用响应拦截器
                const resp = beforeResponse(response);
                return resp;
            }).catch(error => {
                // 调用异常处理的方法
                errorHandle(error);
                throw error; // 重新抛出错误以便外部处理
            });
        } else if (config.method == "PATCH") {
            return axios.patch(config.url, config.data, {
                headers: config.headers
            }).then(response => {
                // 调用响应拦截器
                const resp = beforeResponse(response);
                return resp;
            }).catch(error => {
                // 调用异常处理的方法
                errorHandle(error);
                throw error; // 重新抛出错误以便外部处理
            });
        } else {
            console.log("请求方法错误");
        }

    },
    get(url, data, auth) {
        /*
        url：接口地址
        data: 查询参数
        auth：请求是否需要携带tokne进行认证(true or false)
        */
        return this.request({
            url: url,
            data: data,
            auth: auth,
            method: "GET"
        })
    },
    post(url, data, auth) {
        /*
        url：接口地址
        data: 请求体参数
        auth：请求是否需要携带tokne进行认证(true or false)
        */
        return this.request({
            url: url,
            data: data,
            auth: auth,
            method: 'POST'
        })
    },
    delete(url, auth) {
        /*
        url：接口地址
        auth：请求是否需要携带tokne进行认证(true or false)
        */
        return this.request({
            url: url,
            auth: auth,
            method: 'DELETE'
        })
    },
    put(url, data, auth) {
        /*
        url：接口地址
        data: 请求体参数
        auth：请求是否需要携带tokne进行认证(true or false)
        */
        return this.request({
            url: url,
            data: data,
            auth: auth,
            method: 'PUT'
        })
    },
    patch(url, data, auth) {
        /*
        url：接口地址
        data: 请求体参数
        auth：请求是否需要携带tokne进行认证(true or false)
        */
        return this.request({
            url: url,
            data: data,
            auth: auth,
            method: 'PATCH'
        })
    }
}
// 请求拦截器
const beforeRequest = (config) => {
    // 请求之前的做的操作
    console.log('请求拦截器：', config);
    config.headers = {}; // 注意这里应该是headers，不是header
    if (config.auth) {
        const token = localStorage.getItem('token'); // 使用localStorage获取token
        if (token) {
            // 在请求头中添加token
            config.headers.Authorization = `Bearer ${token}`;
        } else {
            // 没有登录，无访问权限，使用Vue Router进行重定向
            router.push('/login');
        }
    }
    return config;
};

// 响应拦截器
const beforeResponse = (response) => {
    console.log('响应拦截器：', response);
    if (response.status !== 200 && response.status !== 201 && response.status !== 204) {
        // 给出对应的提示
        if (response.data.error) {
            toast({
                message: response.data.error.toString(),
                type: 'is-primary',
                position: 'top-center',
                duration: 2000,
            })
        }
    }
    return response;
};

//异常处理器
const errorHandle = (err) => {
    console.log('网络异常，请求失败!', err)

}


export default http