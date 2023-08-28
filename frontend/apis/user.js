import sha512 from 'js-sha512';
import { v4 as uuidv4 } from 'uuid';
import { api_base_url } from '../apis/api_base_url'

export const create_user = (user_email, pwd, account_type, user_role) => {
    return new Promise((resolve, reject) => {
        const {data:retv} = useFetch(api_base_url+"user/create", {
            method: 'post',
            body: {
                user_id: uuidv4(),
                user_email: user_email,
                frontend_hashed_pwd: sha512(pwd),
                account_type: account_type,
                user_role: user_role
            }
        })
        if (retv) {
            resolve()
        } else {
            reject()
        }
    })
    
}


export const user_login = async (user_email, pwd) => {
    // return new Promise((resolve, reject) => {
    //     const retv = useFetch(api_base_url+"user/login", {
    //         method: 'get',
    //         query: {
    //             user_email: user_email,
    //             frontend_hashed_pwd: sha512(pwd),
    //         }
    //     })

    //     if (retv.data.value) {
    //         resolve()
    //     } else {
    //         let message = retv.error.value['data']['detail']
    //         reject()
    //     }
    // })


    let status_code = ''
    let message = ''
    let data = ''

    const retv = await useFetch("user/login", {
        onRequest({request, options}){
            options.baseURL = api_base_url
            options.method = 'get',
            options.retry = 3
            options.query = {
                user_email: user_email,
                frontend_hashed_pwd: sha512(pwd)
            }
        },
        onRequestError({request, options, error}) {
            // Handle the request errors
        },
        onResponse({ request, response, options }) {
            // Process the response data
            status_code = response.status
            message = 'success'
            data = response._data
            
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