<script>
import capoo_1 from '~/assets/babyinfo/capoo_1.png'
import capoo_2 from '~/assets/babyinfo/capoo_2.png'
import capoo_3 from '~/assets/babyinfo/capoo_3.png'
import capoo_4 from '~/assets/babyinfo/capoo_4.png'
import capoo_5 from '~/assets/babyinfo/capoo_5.png'
import capoo_6 from '~/assets/babyinfo/capoo_6.png'
import baby_bottle_icon from '~/assets/babyinfo/baby_bottle@3x.png'
import mother_icon from '~/assets/babyinfo/mother@3x.png'
import bread_icon from '~/assets/babyinfo/bread@3x.png'
import happy_icon from '~/assets/babyinfo/happy@3x.png'
import heart_icon from '~/assets/babyinfo/heart@3x.png'
import poop_icon from '~/assets/babyinfo/poop@3x.png'
import sleep_icon from '~/assets/babyinfo/sleep@3x.png'
import water_icon from '~/assets/babyinfo/water@3x.png'

export default {
    props: [],
    created() {
    },
    mounted() {

    },
    data () {
        return {
            record_type: this.$route.query.record_type,
            capoo_pic_lst: [
                capoo_1, capoo_2, capoo_3, capoo_4, capoo_5, capoo_6
            ],
            capoo_name_lst: [
                "capoo_1", "capoo_2", "capoo_3", "capoo_4", "capoo_5", "capoo_6"
            ],
            is_selected_lst: [true, true, false, true, false, true],
            cbox_group_key: 0,
            drawer: false,
            mother_icon: mother_icon,
            baby_bottle_icon: baby_bottle_icon,
            bread_icon: bread_icon,
            happy_icon: happy_icon,
            heart_icon: heart_icon,
            poop_icon: poop_icon,
            sleep_icon: sleep_icon,
            water_icon: water_icon
        }
    },
    methods: {
        cancel_click() {
            navigateTo("/babyinfo");
        },
        confirm_click() {
            navigateTo("/babyinfo")
        },
        cbox_change(idx, status) {
            console.log(idx, status)
        },
        cbox_select_all() {
            this.is_selected_lst = Array(this.is_selected_lst.length).fill(true)
            this.cbox_group_key+=1
        }
    },
}


</script>


<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="grid grid-cols-8 gap-1 pt-10">
            <button class="col-start-1 col-span-2 justify-self-start ml-4 text-orange-400 font-bold" @click="cancel_click">
                取消
            </button>
            <div class="col-start-3 col-span-4 text-center text-lg font-sans font-bold">新增紀錄</div>
            <button class="col-start-7 col-span-2 justify-self-end mr-4 text-orange-400 font-bold" @click="confirm_click">
                完成
            </button>
        </div>
        <div class=" my-8 mx-4">
            <div class="rounded-lg bg-neutral-50 w-full divide-y">
                <record-settings-banner-timepicker label="日期" user_time="2023/02/01" time_type="date"/>
                <record-settings-banner-timepicker label="時間" user_time="08:42 PM" time_type="time"/>
            </div>
        </div>
        <div class=" my-8 mx-4">
            <div class="rounded-lg bg-neutral-50 w-full">
                <account-settings-banner-basic label="類別" :user_label="record_type" @click="drawer = true"/>
            </div>
        </div>
        <div class=" my-8 mx-4">
            <div class="grid grid-cols-8 gap-1">
                <button class="col-start-1 col-span-4 justify-self-start text-black text-xl font-bold">
                    紀錄至
                </button>
                <button class="col-start-7 col-span-2 justify-self-end mr-1 text-orange-400 font-bold" @click="cbox_select_all">
                    全選
                </button>
            </div>
            <div class="rounded-lg bg-neutral-50 w-full divide-y" :key="cbox_group_key">
                <record-baby-checkbox v-for="i in capoo_pic_lst.length" :img_src="capoo_pic_lst[i-1]" :name="capoo_name_lst[i-1]" :idx="i-1" :is_selected="is_selected_lst[i-1]" @cbox_change="cbox_change"/>
            </div>
        </div>




        <client-only>
            <el-drawer v-model="drawer" class="rounded-t-3xl" size="40%" :with-header="false" direction="btt" ref="drawer">
                <div class="bg-no-repeat bg-cover w-full bg-neutral-100 rounded-t-3xl py-3 mt-5 col-span-2">
                    <div class="grid grid-rows-2 grid-cols-4 mt-3 mx-3 justify-evenly gap-4">
                        <babyinfo-record-panel-item class="col-start-1 col-span-1 row-start-1 row-span-1" :img_src="mother_icon" label="母乳" @click="record_type='母乳'; $refs.drawer.handleClose()"/>
                        <babyinfo-record-panel-item class="col-start-2 col-span-1 row-start-1 row-span-1" :img_src="baby_bottle_icon" label="配方奶" @click="record_type='配方奶'; $refs.drawer.handleClose()"/>
                        <babyinfo-record-panel-item class="col-start-3 col-span-1 row-start-1 row-span-1" :img_src="bread_icon" label="點心" @click="record_type='點心'; $refs.drawer.handleClose()"/>
                        <babyinfo-record-panel-item class="col-start-4 col-span-1 row-start-1 row-span-1" :img_src="sleep_icon" label="睡覺" @click="record_type='睡覺'; $refs.drawer.handleClose()"/>
                        <babyinfo-record-panel-item class="col-start-1 col-span-1 row-start-2 row-span-1" :img_src="water_icon" label="尿尿" @click="record_type='尿尿'; $refs.drawer.handleClose()"/>
                        <babyinfo-record-panel-item class="col-start-2 col-span-1 row-start-2 row-span-1" :img_src="poop_icon" label="便便" @click="record_type='便便'; $refs.drawer.handleClose()"/>
                        <babyinfo-record-panel-item class="col-start-3 col-span-1 row-start-2 row-span-1" :img_src="happy_icon" label="散步" @click="record_type='散步'; $refs.drawer.handleClose()"/>
                        <babyinfo-record-panel-item class="col-start-4 col-span-1 row-start-2 row-span-1" :img_src="heart_icon" label="擠奶" @click="record_type='擠奶'; $refs.drawer.handleClose()"/>
                    </div>
                </div>
            </el-drawer>
        </client-only>











        
    </div>
</template>