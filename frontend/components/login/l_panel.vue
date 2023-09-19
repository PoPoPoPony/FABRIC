<template>
    <div>
        <!-- <el-input v-model="input2" class="w-8 p-10 rounded" placeholder="Account" style="border:none"> -->
            <!-- <template #prepend style='background-color: white ;'> -->
                <!-- <el-icon size='20' ><User/></el-icon> -->
            <!-- </template> -->
        <!-- </el-input> -->
        <div class="mt-12 mx-5">
            <!-- <login-account-input/> -->
            <login-input input_type="text" label="Email" @input_change="email_change" ref="email_input"/>
        </div>

        <div class="mt-3 mx-5">
            <login-input input_type="password" label="Password" @input_change="pwd_change" ref="pwd_input"/>
        </div>
        <div class="mt-5 mx-5">
            <button class="w-full middle none center rounded-lg bg-blue-700 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md border-2 border-blue-700 shadow-blue-700/20 transition-all hover:shadow-lg hover:shadow-blue-700/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" data-ripple-light="true" @click="login_click" :disabled="!user_email || !user_pwd" >
                Login
            </button>
        </div>
        <div class="mt-3 mx-5">
            <div class="text-divider">or</div>
        </div>
        <div class="mt-3 mx-5">
            <button class="w-full middle none center rounded-lg bg-white py-3 px-6 font-sans text-xs font-bold uppercase text-black border-2 border-blue-700 transition-all hover:bg-blue-700 hover:text-white hover:shadow-lg hover:shadow-blue-700/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" data-ripple-light="true" @click="signup_click">
                Sign up
            </button>
        </div>
    </div>
</template>


<script>
import { ElMessage } from 'element-plus'
import { ElLoading } from 'element-plus'
import { APIUserLogin, APIGetUserRole } from '@/apis/user'
import { useUserStore } from '@/stores/user'


export default {
    created() {

    },
    mounted() {

    },
    data() {
        return {
            user_email: "",
            user_pwd: "",
        }
    },
    methods: {
        async login_click() {
            const loading = ElLoading.service({
                lock: true,
                text: 'Loading',
                background: 'rgba(0, 0, 0, 0.7)',
            })

            let retv = await APIUserLogin(this.user_email, this.user_pwd)
            

            if (retv['status_code'] == 200) {
                ElMessage({
                    message: 'Login success!',
                    type: 'success',
                })

                // store access token in the cookie
                const cookie_access_token = useCookie("access_token", {
                    httpOnly: false,
                })
                cookie_access_token.value = retv['data']['access_token']

                const userStore = useUserStore()
                // console.log(this.user_email)
                userStore.set_user_email(this.user_email)
                
                // 存cookie可能比較慢，這邊先直接傳access_token進去
                let retv_role = await APIGetUserRole(retv['data']['access_token'])
                
                if (retv_role['status_code'] == 200) {
                    userStore.set_user_role(retv_role['data'][0]['user_role'])
                    navigateTo("/babyinfo")
                } else {
                    ElMessage({
                        message: `Role Error! \n ${retv['message']}`,
                        type: 'error',
                    })
                }


                
                // console.log(userStore.user_email)

                

                // navigateTo("/babyinfo")
                
                // pinia example
                // const authStore = useAuthStore()

                // console.log(authStore.access_token)
                // console.log(authStore.token_type)
            } else if (retv['status_code'] == 403) {
                ElMessage({
                    message: retv['message'],
                    type: 'error',
                })
                this.$refs.email_input.input_invalid_styling()
                this.$refs.pwd_input.input_invalid_styling()
            } else {
                console.log(retv['status_code'])
            }
            loading.close()
        },
        signup_click() {
            this.$emit("signup_click")
        },
        email_change(email) {
            this.user_email = email
        },
        pwd_change(pwd) {
            this.user_pwd = pwd
        },
    }
}



</script>


<style lang='scss' scoped>

.text-divider {
    display: flex;
    align-items: center;
    --text-divider-gap: 1rem; // set a customizable gap between label and lines
}

.text-divider::before, .text-divider::after {
    content: '';
    height: 1px;
    background-color: silver;
    flex-grow: 1;
}

.text-divider::before {
    margin-right: var(--text-divider-gap);
}

.text-divider::after {
    margin-left: var(--text-divider-gap);
}
</style>