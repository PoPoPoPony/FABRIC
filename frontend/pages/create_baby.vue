<script>
// import capoo_1 from '@/assets/babyinfo/capoo_1.png'
import { Plus } from '@element-plus/icons-vue'
import { ZoomIn } from '@element-plus/icons-vue'
import { Download } from '@element-plus/icons-vue'
import { Delete } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { api_base_url } from '@/apis/api_base_url'
// import structuredClone from '@ungap/structured-clone';
import { v4 as uuidv4 } from 'uuid';
import { useUserStore } from "@/stores/user"
// import { ElLoading } from 'element-plus'
import { APIUpdateBabyInfo } from "@/apis/baby"

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
    mounted() {
        // let file = {
        //     url: "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg"
        // }
        // this.handleChange("", [file])
        // console.log(typeof(file))
        // console.log(file)
    },
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
            baby_avatar_reupload: false,
            backend_info: {
                'url': api_base_url+'/baby/create',
                'header': {
                    'Authorization': `Bearer ${useCookie("access_token").value}`
                }
            },
            upload_key: 0,
            baby_name: '',
            baby_avatar_backup: '',
            input_cls: "text-black focus:text-blue-700 focus:border-blue-700",
            label_cls: "peer-focus:before:border-blue-700 peer-focus:text-blue-700 peer-focus:after:border-blue-700",
            baby_birth: "",
            baby_sex: "",
            sex_options: [{
                "value": "Male",
                "label": "Male"
            }, {
                "value": "Female",
                "label": "Female"
            }],
            baby_diseases: "",
            disease_options: [{
                "value": "0",
                "label": "高血壓",
            }, {
                "value": "1",
                "label": "糖尿病",
            }, {
                "value": "2",
                "label": "心臟疾病",
            }, {
                "value": "3",
                "label": "氣喘",
            }, {
                "value": "4",
                "label": "唐氏症",
            }, {
                "value": "5",
                "label": "高血脂症",
            }, {
                "value": "6",
                "label": "胃癌",
            }, {
                "value": "7",
                "label": "乳癌",
            }, {
                "value": "8",
                "label": "白化症",
            }, {
                "value": "9",
                "label": "色盲",
            }, ],

            // 整合id、name、sex、... etc的物件(avatar由el-upload上傳)
            baby_data: {},
            upload_key: 0,
            baby_id: uuidv4(),
        }
    },
    methods: {
        on_error(file, files) {
            ElMessage({
                message: "Error!",
                type: 'error',
            })
            this.upload_key+=1
        },

        handleRemove(file) {
            this.$refs.upload.handleRemove(file)
            this.files = []
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

        handleChange(file, files) {
            if (file.status == 'ready') {
                if (this.files.length == 0) {
                    this.files.push(file)
                } else if (this.files.length == 1) {
                    this.files[0] = file
                }
            }
            

            this.hideUpload = this.files.length >= 1
        },
        date_picker_change(date_str) {
            this.baby_birth = date_str
        },
        disease_change(vals) {
            console.log(vals)
        },
        show_error(message) {
            ElMessage({
                message: message,
                type: 'error',
            })
        },
        check_baby_data() {
            let status = ''
            let message=''
            if (this.files.length == 0) {
                status = false
                message = "Please upload baby's picture!"

                return {
                    'status': status,
                    'message': message
                }
            } 
            if (!this.baby_name) {
                status = false
                message = "Please enter baby's name!"

                return {
                    'status': status,
                    'message': message
                }
            } 

            if (!this.baby_sex) {
                status = false
                message = "Please select baby's biological sex!"

                return {
                    'status': status,
                    'message': message
                }
            }

            if (!this.baby_birth) {
                status = false
                message = "Please select baby's birth date!"

                return {
                    'status': status,
                    'message': message
                }
            }

            return {
                'status': true,
                'message': ''
            }

            
        },
        
        async store_click() {
            console.log("store click")
            // let checked = this.check_baby_data()
            // if (checked['status']) {
            //     this.send_backend()
            // } else {
            //     this.show_error(checked['message'])
            // }

            // console.log(typeof(this.files[0]))
            // console.log(this.files[0])

            // console.log(this.files)
            // console.log(this.baby_sex)
            // console.log(this.baby_name)
            // console.log(this.baby_diseases)
            // console.log(this.baby_birth)

            // submit the baby avatar

            // const userStore = useUserStore()

            // this.baby_data = {
            //     'baby_id': uuidv4(),
            //     'baby_name': this.baby_name,
            //     'baby_birth': this.baby_birth,
            //     'baby_sex': this.baby_sex,
            //     'baby_diseases': this.baby_diseases.join(','),
            //     'user_role': userStore.user_role
            // }

            // await this.$refs.upload.submit()

            await APIUpdateBabyInfo(
                this.baby_id,
                this.files[0].raw,
                this.baby_name,
                this.baby_birth,
                this.baby_sex,
                this.baby_diseases.join(','),
            )

            // this.upload_key+=1

        },

        before_baby_avatar_upload (file) {
            if (file.type !== 'image/jpeg' && file.type !== 'image/jpg' && file.type !== 'image/png') {
                ElMessage.error('Avatar picture must be JPG/JPEG/PNG format!')
                return false
            } else {
                console.log(this.files[0])
                let new_file = new File([this.files[0]['raw']], this.files[0]['raw']['name'])

            }
        },

        baby_avatar_upload_error() {
            console.log("error")
        },

        baby_avatar_upload_success() {
            ElMessage({
                message: "Success!",
                type: "success",
            })

            navigateTo("baby_detail_list")
        },

        go_back () {
            navigateTo("/baby_detail_list")
        },

        send_backend() {

        },
        temp() {
            // console.log(this.baby_diseases.join(','))
        }
    }
}

</script>



<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <div class="bg-neutral-50 h-20">
            <div class="grid grid-cols-3 gap-1 pt-10">
                <div class="col-start-1 col-span-1 ml-2 justify-self-start">
                    <el-button text @click="go_back">
                        <svg xmlns="http://www.w3.org/2000/svg" style="display: inline;" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="font-bold text-orange-400 w-5 h-5 place-self-center">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 19.5L8.25 12l7.5-7.5" />
                        </svg>
                        <span class="text-orange-400 font-bold">返回</span>
                    </el-button>
                </div>
                <p class="col-start-2 col-span-1 text-center text-lg font-sans font-bold">編輯寶貝資訊</p>
                <div class="col-start-3 col-span-1 mr-2 justify-self-end">
                    <!-- :disabled="!baby_name || !baby_sex || !baby_birth" -->
                    <el-button text class="justify-self-end" @click="store_click">
                        <span class="text-orange-400 font-bold ">儲存</span>
                    </el-button>
                </div>
            </div>

        </div>
        <div class="grid h-80 pt-8 w-full place-items-center">
            <el-upload :key="upload_key" :on-error="baby_avatar_upload_error" :on-success="baby_avatar_upload_success" :before-upload="before_baby_avatar_upload" accept="image/jpg,image/png,image/jpeg" class="place-items-center" ref="upload" :file-list="files" :class="{hide:hideUpload}" :action="backend_info['url']" :on-change="handleChange" list-type="picture-card" :limit="1" :auto-upload="false" :headers="backend_info['header']" :data="baby_data" name="baby_avatar">
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
                            @click="handleDownload(baby_avatar)"
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
                <img class="w-full" :src="dialogImageUrl" alt="Preview Image" />
            </el-dialog>
        </client-only>

        <!-- <div class="fixed bottom-0 pt-2 w-full h-12 bg-neutral-50">
            <footer_banner :page_type="page_type" class="" />
        </div> -->
        <div class="bg-white rounded-xl mx-8 px-3 divide-y">
            <div class="w-full grid grid-cols-10 py-4 ">
                <span class="self-center col-start-1 col-span-2">寶貝 : </span>
                <div class="relative content-center col-start-3 col-span-8 self-center">
                    <input type='text' class="peer h-full w-full rounded-[7px] border border-gray-200 border-t-transparent bg-transparent px-3 py-2.5 !pr-9 font-sans text-sm font-normal outline outline-0 transition-all placeholder-shown:border placeholder-shown:  placeholder-shown:border-t-gray-200 focus:border-2 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-gray-50" :class="input_cls" placeholder=" " v-model="baby_name"/>
                    <label class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-black transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-500" :class="label_cls">
                        姓名
                    </label>
                </div>
            </div>
            <div class="w-full grid grid-cols-10 py-4">
                <span class="self-center col-start-1 col-span-2 ">性別 : </span>
                <client-only>
                    <el-select-v2
                        v-model="baby_sex"
                        :options="sex_options"
                        placeholder="Please select"
                        class="self-center col-start-3 col-span-8"
                        clearable
                    />
                </client-only>
            </div>
            <div class="w-full grid grid-cols-10 py-4">
                <span class="self-center col-start-1 col-span-3">出生日期 : </span>
                <div class="col-start-4 col-span-7">
                    <client-only>
                        <record-datepicker default_date="" @date_picker_change="date_picker_change"/>
                    </client-only>
                </div>
            </div>
            <div class="w-full grid grid-cols-10 py-4">
                <span class="self-center col-start-1 col-span-3 ">
                    家族疾病 :
                    <span class="text-xs">
                        (無則不需填)
                    </span>
                </span>
                <client-only>
                    <el-select-v2
                        v-model="baby_diseases"
                        :options="disease_options"
                        placeholder=""
                        class="self-center col-start-4 col-span-7"
                        multiple
                        clearable
                        collapse-tags
                        collapse-tags-tooltip
                    />
                </client-only>
            </div>
        </div>
        <el-button @click="temp">123</el-button>


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