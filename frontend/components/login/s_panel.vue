<template>
    <div>
        <!-- <el-input v-model="input2" class="w-8 p-10 rounded" placeholder="Account" style="border:none"> -->
            <!-- <template #prepend style='background-color: white ;'> -->
                <!-- <el-icon size='20' ><User/></el-icon> -->
            <!-- </template> -->
        <!-- </el-input> -->
        <div class="mt-12 mx-5">
            <login-input input_type="text" label="Email" @input_change="email_change"/>
        </div>

        <div class="mt-3 mx-5">
            <login-input input_type="password" label="Password" @input_change="pwd_change"/>
        </div>
        <div class="mt-3 mx-5">
            <client-only>
                <login-select @select_change="role_change"/>
            </client-only>
        </div>
        <div class="mt-3 mx-5">
            <button class="w-full middle none center rounded-lg bg-blue-700 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md border-2 border-blue-700 shadow-blue-700/20 transition-all hover:shadow-lg hover:shadow-blue-700/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" data-ripple-light="true" @click="create_click" :disabled="!user_email || !user_pwd || user_roles.length==0">
                Create!
            </button>
        </div>
        <div class="mt-3 mx-5">
            <button class="w-full middle none center rounded-lg bg-white py-3 px-6 font-sans text-xs font-bold uppercase text-black border-2 border-blue-700 transition-all hover:bg-blue-700 hover:text-white hover:shadow-lg hover:shadow-blue-700/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" data-ripple-light="true" @click="cancle_click">
                Cancle
            </button>
        </div>
    </div>
</template>


<script>
import { ElLoading } from 'element-plus'
import { ElMessage } from 'element-plus'
import { APICreateUser } from '@/apis/user'

export default {
    created() {

    },
    mounted() {

    },
    data() {
        return {
            user_email: "",
            user_pwd: "",
            user_roles: []
        }
    },
    methods: {
        async create_click() {
            // const loading = ElLoading.service({
            //     lock: true,
            //     text: 'Loading',
            //     background: 'rgba(0, 0, 0, 0.7)',
            // })
            let p = await APICreateUser(
                this.user_email,
                this.user_pwd,
                "Local",  // account_type is set to be local,
                this.user_roles
            )



            // Promise.all(create_user_promise).then(() => {
            //     loading.close()
            //     ElMessage({
            //         message: 'Create account success!',
            //         type: 'success',
            //     })
            //     this.$emit("create_account_success")
            // }).catch(()=>{
            //     loading.close()
            //     ElMessage({
            //         message: 'Create account failed!',
            //         type: 'error',
            //     })
            // })
        }, 
        cancle_click() {
            this.$emit("signup_cancel_click")
        },
        email_change(email) {
            this.user_email = email
        },
        pwd_change(pwd) {
            this.user_pwd = pwd
        },
        role_change(roles) {
            this.user_roles = roles
        }
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