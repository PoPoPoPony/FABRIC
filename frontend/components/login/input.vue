<template>
  <div class="relative h-10 w-full" :class="container_cls" :key="container_key">
    <div class="absolute top-2/4 right-3 grid h-5 w-5 -translate-y-2/4 place-items-center text-black">
      <el-icon size='20' class="" :style="icon_style" style='font-weight:bold;' >
        <User v-if="label=='Email'"/>
        <Key v-if="label=='Password'"/>
      </el-icon>
    </div>
    <input :type='input_type' class="peer h-full w-full rounded-[7px] border border-gray-200 border-t-transparent bg-transparent px-3 py-2.5 !pr-9 font-sans text-sm font-normal outline outline-0 transition-all placeholder-shown:border placeholder-shown:  placeholder-shown:border-t-gray-200 focus:border-2 focus:border-t-transparent focus:outline-0 disabled:border-0 disabled:bg-gray-50" :class="input_cls" placeholder=" " @focus='f_f' @blur='f_b' v-model="input_val" @change="input_change"/>

    <label class="before:content[' '] after:content[' '] pointer-events-none absolute left-0 -top-1.5 flex h-full w-full select-none text-[11px] font-normal leading-tight text-black transition-all before:pointer-events-none before:mt-[6.5px] before:mr-1 before:box-border before:block before:h-1.5 before:w-2.5 before:rounded-tl-md before:border-t before:border-l before:border-gray-200 before:transition-all after:pointer-events-none after:mt-[6.5px] after:ml-1 after:box-border after:block after:h-1.5 after:w-2.5 after:flex-grow after:rounded-tr-md after:border-t after:border-r after:border-gray-200 after:transition-all peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[3.75] peer-placeholder-shown:text-gray-500 peer-placeholder-shown:before:border-transparent peer-placeholder-shown:after:border-transparent peer-focus:text-[11px] peer-focus:leading-tight peer-focus:before:border-t-2 peer-focus:before:border-l-2 peer-focus:after:border-t-2 peer-focus:after:border-r-2 peer-disabled:text-transparent peer-disabled:before:border-transparent peer-disabled:after:border-transparent peer-disabled:peer-placeholder-shown:text-blue-500" :class="label_cls">
      {{ label }}
    </label>
  </div>
</template>


<script>
import { User } from '@element-plus/icons-vue'
import { Key } from '@element-plus/icons-vue'

export default {
    props: ["input_type", "label"],
    components: {
      User,
      Key
    },
    created () {
    },
    mounted() {
        
    },
    data() {
        return { 
            icon_style: '',
            input_val: '',
            is_invalid: false,
            input_cls: "text-black focus:text-blue-700 focus:border-blue-700",
            label_cls: "peer-focus:before:border-blue-700 peer-focus:text-blue-700 peer-focus:after:border-blue-700",
            container_cls: '',
            container_key: 0,
        }
    },
    methods: {
        f_f() {
          if (!this.is_invalid) {
            this.icon_style = 'color: #1d4ed8'
          }
        },
        f_b() {
          if (!this.is_invalid || this.input_val == '') {
            this.icon_style = ''
          }
        },
        input_change () {
          if (this.label == "Email") {
            let result = this.varify_email(this.input_val)
            if (result || this.input_val.length==0) {
              // styling
              this.input_valid_styling()

              // pushing data
              this.$emit("input_change", this.input_val)
            } else {
              // stying 
              this.input_invalid_styling()

              // pushing data
              this.$emit("input_change", "")
            }
          } else if (this.label == 'Password') {
            if (this.input_val.length==0) {  // 之後這邊可以替換成需要高強度密碼才 $emit
              this.input_valid_styling()
              this.$emit("input_change", "")
            } else {
              this.input_valid_styling()
              this.$emit("input_change", this.input_val)
            }
          }
        },

        varify_email(email) {
            var regex = /^([a-zA-Z0-9_.\-+])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            return regex.test(email)
        },

        input_invalid_styling() {
          this.is_invalid = true
          this.input_cls = "text-red-600 focus:border-red-600 border-red-600 border-2"
          this.label_cls = "peer-focus:before:border-red-600 peer-focus:text-red-600 peer-focus:after:border-red-600 before:border-red-600 text-red-600 after:border-red-600 after:border-t-2 before:border-t-2"
          this.icon_style = 'color: #dc2626'
          this.container_cls = "animate__animated animate__shakeX"
          this.container_key+=1
        },

        input_valid_styling() {
          this.is_invalid = false
          this.icon_style = ''
          this.input_cls = "text-black focus:text-blue-700 focus:border-blue-700"
          this.label_cls = "peer-focus:before:border-blue-700 peer-focus:text-blue-700 peer-focus:after:border-blue-700"
          this.container_cls=''
        },
    }
}
</script>