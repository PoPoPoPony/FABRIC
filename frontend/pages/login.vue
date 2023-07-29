<script>
import bg_screen from '~/assets/login/bg.jpg'
import bg_smart_phone from '~/assets/login/smart_phone_bg.jpg'



export default {
    created () {
        const { isMobile } = useDevice()
        if(isMobile) {
            this.bg = bg_smart_phone
        } else {
            this.bg = bg_screen
        }
        
    },
    data() {
        return { 
            bg: 0,
            loginclicked: false
        }
    },
    methods: {
        onLoginClick() {
            this.loginclicked = true
            setTimeout(()=>{
                navigateTo("/babyinfo")
            }, 2000)
        }
    }
}
</script>

<template>
    <div class="bg-no-repeat bg-cover w-full h-screen" :style="{ backgroundImage: `url(${bg})`}">
        <div class="absolute inset-x-0 bottom-0 h-60 bg-white rounded-t-3xl drop-shadow-2xl" >
            <login-button-with-icon class="mt-3 mr-2 ml-3 w-80 items-center" icon_name="Apple"/>
            <login-button-with-icon class="mt-2 mr-2 ml-3 w-80 items-center" icon_name="Google"/>
            <!-- <button v-if="!loginclicked" class="rounded-3xl p-2 self-center bg-orange-400 mt-2 mr-2 ml-3 w-80 items-center text-white" @click="onLoginClick"> -->
                <!-- <NuxtLink to="/home"> -->
                    <!-- 登入 -->
                <!-- </NuxtLink> -->
            <!-- </button> -->
            <button  class="rounded-3xl p-2  bg-orange-400 mt-2 mr-2 ml-3 w-80  text-white flex items-center justify-center" @click="onLoginClick" :disabled="loginclicked">
                <svg v-if="loginclicked" class="animate-spin mr-3 w-6 h-6" viewBox="0 0 40 40">
                    <path opacity="0.3" fill="#ffffff" d="M20.201,5.169c-8.254,0-14.946,6.692-14.946,14.946c0,8.255,6.692,14.946,14.946,14.946
                    s14.946-6.691,14.946-14.946C35.146,11.861,28.455,5.169,20.201,5.169z M20.201,31.749c-6.425,0-11.634-5.208-11.634-11.634
                    c0-6.425,5.209-11.634,11.634-11.634c6.425,0,11.633,5.209,11.633,11.634C31.834,26.541,26.626,31.749,20.201,31.749z"/>
                    <path fill="#ffffff" opacity="1" d="M26.013,10.047l1.654-2.866c-2.198-1.272-4.743-2.012-7.466-2.012h0v3.312h0
    C22.32,8.481,24.301,9.057,26.013,10.047z"/>
                </svg>
                <text v-if="!loginclicked">
                    登入
                </text>
            </button>
            <div class="mt-3 mr-2 ml-3 w-80 text-center text-sm">沒有帳號? 立即<span class="text-amber-600">註冊</span></div>
        </div>
    </div>
    
</template>