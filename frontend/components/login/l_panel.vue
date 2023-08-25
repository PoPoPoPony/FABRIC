<template>
    <div>
        <!-- <el-input v-model="input2" class="w-8 p-10 rounded" placeholder="Account" style="border:none"> -->
            <!-- <template #prepend style='background-color: white ;'> -->
                <!-- <el-icon size='20' ><User/></el-icon> -->
            <!-- </template> -->
        <!-- </el-input> -->
        <div class="mt-12 mx-5">
            <!-- <login-account-input/> -->
            <login-input input_type="text" label="Email"/>
        </div>

        <div class="mt-3 mx-5">
            <login-input input_type="password" label="Password"/>
        </div>
        <div class="mt-5 mx-5">
            <button class="w-full middle none center rounded-lg bg-blue-700 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md border-2 border-blue-700 shadow-blue-700/20 transition-all hover:shadow-lg hover:shadow-blue-700/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none" data-ripple-light="true" @click="login_click">
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


export default {
    created() {

    },
    mounted() {

    },
    data() {
        return {}
    },
    methods: {
        login_click() {
            navigateTo("/babyinfo")
        },
        signup_click() {
            this.$emit("signup_click")
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