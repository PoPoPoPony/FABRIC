<script>
// import capoo_1 from '@/assets/babyinfo/capoo_1.png'
import { Plus } from '@element-plus/icons-vue'
import { ZoomIn } from '@element-plus/icons-vue'
import { Download } from '@element-plus/icons-vue'
import { Delete } from '@element-plus/icons-vue'

export default {
    props: [],
    components: {
        Plus,
        ZoomIn,
        Download,
        Delete
    },
    // created() {



    // },
    // mounted() {

    // },
    // computed() {

    // },
    data() {
        return {
            // capoo_1: capoo_1,
            dialogImageUrl: '',
            dialogVisible: false,
            disabled: false,
            hideUpload: false,
            files: [],
            input_val: '',
            input_cls: "text-black focus:text-blue-700 focus:border-blue-700",
            label_cls: "peer-focus:before:border-blue-700 peer-focus:text-blue-700 peer-focus:after:border-blue-700",
            baby_sex: "",
            sex_options: [{
                "value": "Male",
                "label": "Male"
            }, {
                "value": "Female",
                "label": "Female"
            }]
        }
    },
    methods: {
        handleRemove(file) {
            this.$refs.upload.handleRemove(file)
            this.hideUpload = this.files.length >= 1 // 根據現在的數量決定要不要顯示可上傳的介面
        },

        handlePictureCardPreview(file) {
            this.dialogImageUrl = file.url
            this.dialogVisible = true
        },

        // download 先不做
        // handleDownload(file){ 
        //     console.log(file)
        // },


        handleChange(_, files) {
            this.files = files
            console.log(this.files)
            this.hideUpload = this.files.length >= 1
        }

    //     handleExceed (files) {
    //         this.$refs.upload.clearFiles()
    //         let file = files[0]
    //         this.upload_cls = 'hide'
    //     }
    }
}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="bg-neutral-50 h-20">
            <div class="grid grid-cols-3 gap-1 pt-10">
                <div class="col-start-1 col-span-1 ml-4 justify-self-start text-orange-400 font-bold">
                    <button>
                        <svg xmlns="http://www.w3.org/2000/svg" style="display: inline;" fill="none" viewBox="0 0 24 24"
                            stroke-width="1.5" stroke="currentColor" class="w-6 h-6 place-self-center">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                        </svg>
                        <span>返回</span>
                    </button>
                </div>
                <p class="col-start-2 col-span-1 text-center text-lg font-sans font-bold">編輯寶貝資訊</p>
                <div class="col-start-3 col-span-1 mr-4 justify-self-end text-orange-400 font-bold">
                    <button class="justify-self-end">
                        儲存
                    </button>
                </div>
            </div>
        </div>
        <div class="grid h-80 pt-8 w-full place-items-center">
            <!-- :show-file-list="false" :limit="1"  -->
            <el-upload class="place-items-center" ref="upload" :file-list="files" :class="{hide:hideUpload}" action="#" :on-change="handleChange" list-type="picture-card" :limit="1" :auto-upload="false">
                <el-icon size='20' style='font-weight:bold;' >
                    <Plus/>
                </el-icon>
                <template #file="{ file }">
                    <img class="place-items-center el-upload-list__item-thumbnail" :src="file.url" alt="" />
                    <span class="el-upload-list__item-actions">
                        <span
                            class="el-upload-list__item-preview"
                            @click="handlePictureCardPreview(file)"
                        >
                            <el-icon size='20' style='font-weight:bold;' >
                                <ZoomIn />
                            </el-icon>
                        </span>
                        <!-- <span
                            v-if="!disabled"
                            class="el-upload-list__item-delete"
                            @click="handleDownload(file)"
                        >
                            <el-icon size='20' style='font-weight:bold;' >
                                <Download />
                            </el-icon>
                        </span> -->
                        <span
                            v-if="!disabled"
                            class="el-upload-list__item-delete"
                            @click="handleRemove(file)"
                        >
                            <el-icon size='20' style='font-weight:bold;' >
                                <Delete />
                            </el-icon>
                        </span>
                    </span>
                </template>
            </el-upload>


        </div>
        <client-only>
            <el-dialog v-model="dialogVisible">
                <img w-full :src="dialogImageUrl" alt="Preview Image" />
            </el-dialog>
        </client-only>

        <!-- <div class="fixed bottom-0 pt-2 w-full h-12 bg-neutral-50">
            <footer_banner :page_type="page_type" class="" />
        </div> -->
        <div class="w-72 h-72 bg-white rounded-xl ml-9 px-3 divide-y">
            <div class="w-full h-10 grid grid-cols-10 my-4">
                <span class="self-center col-start-1 col-span-2">寶貝 : </span>
                <div class="relative content-center col-start-3 col-span-8 self-center">
                    <input type='text' class="peer h-full w-full rounded-[7px] border border-gray-200 border-t-transparent bg-transparent px-3 py-2.5 !pr-9 font-sans text-sm font-normal outline outline-0 transition-all placeholder-shown:border placeholder-shown:  placeholder-shown:border-t-gray-200 focus:border-2 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-gray-50" :class="input_cls" placeholder=" " v-model="input_val"/>
                    <label class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-black transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-500" :class="label_cls">
                        姓名
                    </label>
                </div>
            </div>
            <div class="w-full h-10 grid grid-cols-10 my-4">
                <span class="self-center col-start-1 col-span-2 ">性別 : </span>
                <client-only>
                    <el-select-v2
                        v-model="baby_sex"
                        :options="sex_options"
                        placeholder="Please select"
                        class="self-center col-start-3 col-span-8"
                    />
                </client-only>
            </div>
            <div class="w-full h-10 grid grid-cols-10 my-4">
                <span class="self-center col-start-1 col-span-3">出生日期 : </span>
                <div class="col-start-5 col-span-6">
                    <client-only>
                        <record-datepicker default_date=""/>
                    </client-only>
                </div>
            </div>
        </div>



    </div>
</template>


<style lang="scss">
.null_scroll_bar::-webkit-scrollbar {
    display: none;
}

// :deep(.hide .el-upload--picture-card) {
//     display:  none;
// }


.hide .el-upload--picture-card {
    display:  none;
}

</style>