<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <!-- absolute inset-x-0  -->
        <div class=" bg-neutral-50 grid grid-cols-1 grid-rows-2">
            <p class="text-center text-lg font-bold font-sans pt-10 row-start-1 row-span-2  col-start-1 col-span-1">帳戶</p> 
        </div>
        <div class=" my-8 mx-4">
            <p class="text-start text-xl font-bold font-sans ">用戶</p>
            <div class="rounded-lg bg-neutral-50 w-full divide-y">
                <account-settings-banner-basic label="Email" user_label="test@gmail.com"/>
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
                <account-settings-banner-switch label="裝置" :switch_value="true"/>
                <account-settings-banner-switch label="靈敏度" :switch_value="false"/>
            </div>
        </div>
        <div class="my-8 mx-4">
            <button id="logout_btn" class="hover:text-neutral-50 py-2 rounded-lg bg-neutral-50 hover:bg-red-600 w-full px-4 text-red-600 font-bold text-center" @click="onClick"> 
                登出
            </button>
        </div>
    </div>
</template>


<script>
export default {
    methods: {
        onClick() {
            console.log("123")
        },
    },
}
</script>
<style lang="scss">
#logout_btn {
    cursor: pointer;
}
</style>