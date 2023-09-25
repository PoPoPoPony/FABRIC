
import { APIGetUserBabys } from 'apis/user';
<template>
    <div>
        <button @click="baby_click">
        <div class="w-full grid grid-cols-10 py-4">
            <div class="content-center col-start-1 col-span-2 self-center">
                <el-image :src="`${api_base_url}/baby/avatar/${baby_avatar}`" fit="contain" class="object-contain justify-self-center rounded-full border-2 border-black"/>
            </div>
            <div class="content-center col-start-3 col-span-3 self-center text-xl font-bold">
                {{ baby_name }}
            </div>
            <div class="content-center col-start-7 col-span-3 self-center text-m justify-self-end">
                {{ get_baby_age() }}
            </div>
        </div>
        </button>
    </div>


    <!-- <div class="w-full h-10 py-1 pl-3 grid grid-cols-10">
        <div class="col-span-1 rounded-full">
            <img :src="img_src" class="object-contain justify-self-center rounded-full">
        </div>
        <div class="col-start-2 col-span-3 place-self-center">
            {{ name }}
        </div>
        <div class="col-start-6 col-span-5 pr-4 place-self-end">
            <input
                class="relative -ml-[1.5rem] mr-[6px] mt-[0.15rem] h-[1.5rem] w-[1.5rem] appearance-none rounded-full border-[0.125rem] border-solid border-neutral-300 outline-none before:pointer-events-none before:absolute before:h-[1.2rem] before:w-[1.2rem] before:scale-0 before:rounded-full before:bg-transparent before:opacity-0 before:shadow-[0px_0px_0px_13px_transparent] before:content-[''] checked:border-orange-500 checked:bg-orange-500 checked:before:opacity-[0.16] checked:after:absolute checked:after:mt-[0.14rem] checked:after:ml-[0.42rem] checked:after:block checked:after:h-[0.8125rem] checked:after:w-[0.375rem] checked:after:rotate-45 checked:after:border-[0.125rem] checked:after:border-l-0 checked:after:border-t-0 checked:after:border-solid checked:after:border-white checked:after:bg-transparent checked:after:content-[''] hover:cursor-pointer hover:before:opacity-[0.04] hover:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:shadow-none focus:transition-[border-color_0.2s] focus:before:scale-100 focus:before:opacity-[0.12] focus:before:shadow-[0px_0px_0px_13px_rgba(0,0,0,0.6)] focus:before:transition-[box-shadow_0.2s,transform_0.2s] focus:after:absolute focus:after:z-[1] focus:after:block focus:after:h-[0.875rem] focus:after:w-[0.875rem] focus:after:rounded-[0.125rem] focus:after:content-[''] checked:focus:before:scale-100 checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca] checked:focus:before:transition-[box-shadow_0.2s,transform_0.2s] checked:focus:after:mt-[0.14rem] checked:focus:after:ml-[0.42rem] checked:focus:after:h-[0.8125rem] checked:focus:after:w-[0.375rem] checked:focus:after:rotate-45 checked:focus:after:rounded-none checked:focus:after:border-[0.125rem] checked:focus:after:border-l-0 checked:focus:after:border-t-0 checked:focus:after:border-solid checked:focus:after:border-white checked:focus:after:bg-transparent dark:border-neutral-600 dark:checked:border-orange-500 dark:checked:bg-orange-500 dark:focus:before:shadow-[0px_0px_0px_13px_rgba(255,255,255,0.4)] dark:checked:focus:before:shadow-[0px_0px_0px_13px_#3b71ca]"
                type="checkbox" v-model="cbox_selected" ref="cbox" />
        </div>
    </div> -->
</template>



<script>
// import { APIGetAvatar } from "@/apis/baby"
import { api_base_url } from '@/apis/api_base_url'


export default {
    props: ["idx", "baby_id", "baby_name", "baby_avatar", "baby_birth", "baby_sex", "baby_diseases"],
    mounted() {

    },
    data() {
        return {
            api_base_url: api_base_url
        }
    },
    methods: {
        get_baby_age() {
            const date_birth = new Date(this.baby_birth)
            const date_now = new Date()
            let td = date_now.getTime() - date_birth.getTime()
            td = parseInt(td / (1000 * 3600 * 24) / 30)

            return `${parseInt(td/12)}歲${td%12}個月`
        },
        baby_click() {
            navigateTo({
                path: "/create_baby",
                query: {
                    idx: this.idx // pinia中的baby_id index
                }
            })
        },
        // async get_baby_avatar() {
        //     // let retv = await APIGetAvatar(this.baby_avatar)
        //     // console.log(retv['data'])

        //     // return URL.createObjectURL(retv['data'])
        //     return ``
        // }
    }
}


</script>