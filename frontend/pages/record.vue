<script>
export default {
    props:[]
}


</script>


<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="grid grid-cols-8 gap-1 pt-10">
            <div class="col-start-1 col-span-2 justify-self-start pl-3 text-orange-400 font-bold">
                取消
            </div>
            <div class="col-start-3 col-span-4 text-center text-lg font-sans font-bold">新增紀錄</div>
            <div class="col-start-7 col-span-2 justify-self-end pr-3 text-orange-400 font-bold">
                完成
            </div>
        </div>
        <div class=" my-8 mx-4">
            <div class="rounded-lg bg-neutral-50 w-full divide-y">
                <record-settings-banner-timepicker label="日期" user_time="2023/02/01" time_type="date"/>
                <record-settings-banner-timepicker label="時間" user_time="08:42" time_type="time"/>
            </div>
        </div>
        <!-- <client-only>
            <datepicker></datepicker>
        </client-only> -->
    </div>
</template>