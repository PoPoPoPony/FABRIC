<template>
    <div class="w-full h-10 py-1 grid grid-cols-10">
        <div class="col-span-3 font-bold py-1 pl-4"> {{ label }}</div>
        <div class="col-start-9 col-span-2">
            <el-switch
                v-model="switch_value"
                class="scale-y-125 scale-x-125 transform-gpu"
                inline-prompt
                style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
                active-text=""
                inactive-text=""
                v-if="switch_show"
            />
        </div>
    </div>
</template>
<script>
export default {
    props: ["label", "user_label"],
    mounted() {
        this.switch_show = true
    },
    data() {
        return {
            switch_value: this.user_label,
            switch_show: false,
        }
    }
}
</script>
<style lang="scss">
    
</style>