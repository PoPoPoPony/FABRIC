<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <!-- absolute inset-x-0  -->
        <div class=" bg-neutral-50 grid grid-cols-1 grid-rows-2">
            <p class="text-center text-lg font-bold font-sans pt-10 row-start-1 row-span-2  col-start-1 col-span-1">帳戶</p> 
        </div>
        <div class=" my-8 mx-4">
            <p class="text-start text-xl font-bold font-sans ">用戶</p>
            <div class="rounded-lg bg-neutral-50 w-full divide-y">
                <account-settings-banner-basic label="Email" :user_label="user_email"/>
                <account-settings-banner-basic label="更改密碼" />
            </div>
        </div>
        <div class=" my-8 mx-4">
            <p class="text-start text-xl font-bold font-sans ">裝置與角色</p>
            <div class="rounded-lg bg-neutral-50 w-full divide-y">
                <account-settings-banner-basic label="裝置" user_label="尚未配對"/>
                <account-settings-banner-basic label="靈敏度" user_label="中" />
                <account-settings-banner-basic label="角色" user_label="媽媽" />
                <account-settings-banner-basic label="寶貝" user_label="" />
            </div>
        </div>
        <div class="my-8 mx-4">
            <p class="text-start text-xl font-bold font-sans ">通知</p>
            <div class="rounded-lg bg-neutral-50 w-full divide-y">
                <account-settings-banner-switch label="更換尿布" :user_label="true"/>
                <account-settings-banner-switch label="睡覺 " :user_label="false"/>
            </div>
        </div>
        <div class="my-8 mx-4">
            <button id="logout_btn" class="hover:text-neutral-50 py-2 rounded-lg bg-neutral-50 hover:bg-red-600 w-full px-4 text-red-600 font-bold text-center" @click="logout_click"> 
                登出
            </button>
        </div>
        <div class="fixed bottom-0 pt-2 w-full h-12 bg-neutral-50">
            <footer-banner :page_type="page_type" class=""/>
        </div>
    </div>
</template>


<script>
import { useUserStore } from '@/stores/user'

export default {
    created() {
        const userStore = useUserStore()
        this.user_email = userStore.user_email
    },
    data () {
        return {
            page_type: "account",
            user_email: '',
        }
    },

    computed () {
        
    },

    methods: {
        logout_click() {
            navigateTo("/login")
        },
    },
}
</script>
<style lang="scss">
#logout_btn {
    cursor: pointer;
}
</style>