<script>
import bg_screen from '~/assets/welcome/bg.jpg'
import bg_smart_phone from '~/assets/welcome/smart_phone_bg.jpg'



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
                navigateTo("/login")
            }, 0)
            // 2000
        }
    }
}
</script>

<template>
    <div class="bg-no-repeat bg-cover w-full h-screen" :style="{ backgroundImage: `url(${bg})`}">
        <!-- new responsive test -->
        <div class="fixed h-56 bottom-0 w-full px-2 bg-white rounded-t-3xl drop-shadow-2xl justify-center" >
            <welcome-button-with-icon class="mt-3 px-4" icon_name="Apple"/>
            <welcome-button-with-icon class="mt-2 px-4" icon_name="Google"/>
            <div class="w-full mt-2 px-4">
                <button  class="rounded-3xl py-2 bg-orange-400 w-full text-white flex items-center justify-center" @click="onLoginClick" :disabled="loginclicked">
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
            </div>
            <div class="mt-3 mr-2 ml-3 text-center text-sm">沒有帳號? 立即<span class="text-amber-600">註冊</span></div>
        </div>
    </div>
    
</template>