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
    mounted() {

    },
    data() {
        return { 
            bg: 0,
            panel_show: 'login'
        }
    },
    methods: {
        return_click() {
            navigateTo("/welcome")
        },
        signup_click() {
            this.panel_show = 'signup'
        },
        signup_cancel_click() {
            this.panel_show = 'login'
        },
        create_account_success() {
            this.panel_show = 'login'
        }
    }
}
</script>

<template>
    <div class="bg-no-repeat bg-cover w-full h-screen -z-20" :style="{ backgroundImage: `url(${bg})`}">
        <!--  justify-self-center align-items-center -->
        <div class='background' />
        <div class="grid grid-cols-3 gap-1 pt-10">
            <button class="col-start-1 col-span-1 justify-self-start ml-4 z-10" @click="return_click">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="w-7 h-7 font-bold text-white">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                </svg>
            </button>
        </div>
        <div class="fixed bottom-0 w-full h-96">

        </div>
        <div class="fixed bottom-0 w-full h-96">
            <div class="h-16 w-full absolute t-0 wave_animation bg-slate-50"/>
            <transition name="slide_left">
                <!-- 跟folder重名好像會出問題 (login-login-panel不行) -->
                <login-l-panel v-if="panel_show=='login'" class="absolute w-full h-80 bottom-0 bg-slate-50" @signup_click="signup_click" />
            </transition>
            <transition name="slide_right">
                <login-s-panel v-if="panel_show=='signup'" class="absolute w-full h-80 bottom-0 bg-slate-50" @signup_cancel_click="signup_cancel_click" @create_account_success="create_account_success"/>
                <!-- signup_click -->
            </transition>
        </div>
    </div>
</template>

<style lang='scss' scoped>
.slide_right-leave-active, .slide_right-enter-active, .slide_left-leave-active, .slide_left-enter-active {
    transition: all 0.9s ease;
}

.slide_right-enter-from {
    transform: translateX(100%);
}

.slide_right-enter-to {
    transform: translateX(0%);
}


.slide_right-leave-from {
    transform: translateX(0%);
}

.slide_right-leave-to {
    transform: translateX(100%);
}


.slide_left-enter-from {
    transform: translateX(-100%);
}

.slide_left-enter-to {
    transform: translateX(0%);
}


.slide_left-leave-from {
    transform: translateX(0%);
}

.slide_left-leave-to {
    transform: translateX(-100%);
}


.background {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.3);
}


.wave_animation {
    animation-name: wave_ani;
    animation-duration: 3s;
    animation-iteration-count: infinite;
    animation-direction: normal;
    animation-timing-function: ease-in-out;
}


@keyframes wave_ani {
    0%, 100% {
clip-path: polygon(100% 100%, 0% 100% , 0.00% 100.00%, 1.67% 99.53%, 3.33% 98.12%, 5.00% 95.82%, 6.67% 92.68%, 8.33% 88.77%, 10.00% 84.20%, 11.67% 79.07%, 13.33% 73.51%, 15.00% 67.66%, 16.67% 61.67%, 18.33% 55.67%, 20.00% 49.82%, 21.67% 44.26%, 23.33% 39.13%, 25.00% 34.56%, 26.67% 30.65%, 28.33% 27.51%, 30.00% 25.21%, 31.67% 23.81%, 33.33% 23.33%, 35.00% 23.81%, 36.67% 25.21%, 38.33% 27.51%, 40.00% 30.65%, 41.67% 34.56%, 43.33% 39.13%, 45.00% 44.26%, 46.67% 49.82%, 48.33% 55.67%, 50.00% 61.67%, 51.67% 67.66%, 53.33% 73.51%, 55.00% 79.07%, 56.67% 84.20%, 58.33% 88.77%, 60.00% 92.68%, 61.67% 95.82%, 63.33% 98.12%, 65.00% 99.53%, 66.67% 100.00%, 68.33% 99.53%, 70.00% 98.12%, 71.67% 95.82%, 73.33% 92.68%, 75.00% 88.77%, 76.67% 84.20%, 78.33% 79.07%, 80.00% 73.51%, 81.67% 67.66%, 83.33% 61.67%, 85.00% 55.67%, 86.67% 49.82%, 88.33% 44.26%, 90.00% 39.13%, 91.67% 34.56%, 93.33% 30.65%, 95.00% 27.51%, 96.67% 25.21%, 98.33% 23.81%, 100.00% 23.33%);

    }
    50% {
clip-path: polygon(100% 100%, 0% 100% , 0.00% 23.33%, 1.67% 23.81%, 3.33% 25.21%, 5.00% 27.51%, 6.67% 30.65%, 8.33% 34.56%, 10.00% 39.13%, 11.67% 44.26%, 13.33% 49.82%, 15.00% 55.67%, 16.67% 61.67%, 18.33% 67.66%, 20.00% 73.51%, 21.67% 79.07%, 23.33% 84.20%, 25.00% 88.77%, 26.67% 92.68%, 28.33% 95.82%, 30.00% 98.12%, 31.67% 99.53%, 33.33% 100.00%, 35.00% 99.53%, 36.67% 98.12%, 38.33% 95.82%, 40.00% 92.68%, 41.67% 88.77%, 43.33% 84.20%, 45.00% 79.07%, 46.67% 73.51%, 48.33% 67.66%, 50.00% 61.67%, 51.67% 55.67%, 53.33% 49.82%, 55.00% 44.26%, 56.67% 39.13%, 58.33% 34.56%, 60.00% 30.65%, 61.67% 27.51%, 63.33% 25.21%, 65.00% 23.81%, 66.67% 23.33%, 68.33% 23.81%, 70.00% 25.21%, 71.67% 27.51%, 73.33% 30.65%, 75.00% 34.56%, 76.67% 39.13%, 78.33% 44.26%, 80.00% 49.82%, 81.67% 55.67%, 83.33% 61.67%, 85.00% 67.66%, 86.67% 73.51%, 88.33% 79.07%, 90.00% 84.20%, 91.67% 88.77%, 93.33% 92.68%, 95.00% 95.82%, 96.67% 98.12%, 98.33% 99.53%, 100.00% 100.00%);
    transform: scaleX(150%);
    }
}


</style>