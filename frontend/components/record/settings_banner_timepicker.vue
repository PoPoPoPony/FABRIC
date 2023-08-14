<template>
    <div class="w-full h-10 py-1 grid grid-cols-10">
        <div class="col-span-3 font-bold py-1 pl-4"> {{ label }}</div>
        <div class="col-start-6 col-span-5 mr-4">
            <client-only>
                <record-datepicker v-if="time_type == 'date'" :default_date="user_time"/>
                <record-timepicker v-if="time_type == 'time'" :default_time="user_time"/>
            </client-only>
        </div>
    </div>
</template>
<script>
export default {
    // time_type -> 'time' or 'date'
    props: ["label", "user_time", 'time_type'],
    mounted() {
        
    },
    data() {
        return {

        }
    }
}
</script>
<style lang="scss">
    
</style>