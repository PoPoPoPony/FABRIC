import { v4 as uuidv4 } from 'uuid';
import { api_base_url } from '../apis/api_base_url'
// import { useUserStore } from '@/stores/user'

// 這些暫時都還沒用到

export const APIUploadBabyAvatar = async (user_email, pwd) => {
    let status_code = ''
    let message = ''
    let data = ''
    // const authStore = useAuthStore()

    let req_form = new FormData()
    req_form.append("grant_type", "password")
    req_form.append("username", user_email)
    req_form.append("password", sha512(pwd))

    const retv = await useFetch("/auth/token", {
        onRequest({ request, options }) {
            options.baseURL = api_base_url
            options.method = 'post'
            options.retry = 3
            options.body = req_form
        },
        onRequestError({ request, options, error }) {
            // Handle the request errors
        },
        onResponse({ request, response, options }) {
            // Process the response data
            status_code = response.status
            message = 'success'
            data = response._data

            // authStore.set_access_token(data['access_token'])
            // authStore.set_token_type(data['token_type'])

        },
        onResponseError({ request, response, options }) {
            // Handle the response errors
            status_code = response.status
            message = response._data['detail']
            data = null
        }
    })

    return {
        'status_code': status_code,
        'message': message,
        'data': data
    }




}


export const get_role = async () => {
    const retv = await useFetch("/user/role", {
        onRequest({ request, options }) {
            options.baseURL = api_base_url
            options.method = 'get'
            options.retry = 3
            options.headers = {
                'Authorization': `Bearer ${useCookie("access_token").value}`
            }
        },
        onRequestError({ request, options, error }) {
            // Handle the request errors
        },
        onResponse({ request, response, options }) {
            // Process the response data

            console.log(response)
            // authStore.set_access_token(data['access_token'])
            // authStore.set_token_type(data['token_type'])

        },
        onResponseError({ request, response, options }) {
            // Handle the response errors
            console.log(response)

        }
    })

}