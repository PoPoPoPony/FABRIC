<template>
    <div>
        <!-- <el-input v-model="input2" class="w-8 p-10 rounded" placeholder="Account" style="border:none"> -->
            <!-- <template #prepend style='background-color: white ;'> -->
                <!-- <el-icon size='20' ><User/></el-icon> -->
            <!-- </template> -->
        <!-- </el-input> -->
        <div class="mt-12 mx-5">
            <login-input input_type="text" label="Email"/>
        </div>

        <div class="mt-3 mx-5">
            <login-input input_type="password" label="Password"/>
        </div>
        <div class="mt-3 mx-5">
            <client-only>
                <login-select/>
            </client-only>
        </div>
        <div class="mt-3 mx-5">
            <button class="w-full middle none center rounded-lg bg-blue-700 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md border-2 border-blue-700 shadow-blue-700/20 transition-all hover:shadow-lg hover:shadow-blue-700/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" data-ripple-light="true" @click="create_click">
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

export default {
    created() {

    },
    mounted() {

    },
    data() {
        return {}
    },
    methods: {
        create_click() {
            const loading = ElLoading.service({
                lock: true,
                text: 'Loading',
                background: 'rgba(0, 0, 0, 0.7)',
            })
            setTimeout(() => {
                loading.close()
                ElMessage({
                    message: 'Create account success!',
                    type: 'success',
                })
                this.$emit("create_account_success")
            }, 3000)
        }, 
        cancle_click() {
            this.$emit("signup_cancel_click")
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