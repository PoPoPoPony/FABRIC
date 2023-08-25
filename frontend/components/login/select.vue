<template>
    <div class="h-10 w-full">

        <!-- <select multiple ref="select" v-model="val">
            <option value="1">Mom</option>
            <option value="2">Dad</option>
            <option value="3">Nurse</option>
        </select> -->
        <!-- <label data-te-select-label-ref>Role</label> -->



        <el-select :popper-append-to-body="false" class="w-full" v-model="val" multiple filterable allow-create default-first-option :reserve-keyword="false" placeholder="Choose tags for your article" size="large" clearable @change="select_change" >
            <el-option v-for="item in options" :disabled="item.disable" v-model="val" :key="item.value" :label="item.label" :value="item.value" />
        </el-select>
    </div>
</template>


<script>
// import { Select, initTE } from "tw-elements";

export default {
    props: [],
    components: {

    },
    created() {
        // initTE({ Select });
    },
    mounted() {
        // new Select(
        //     this.$refs.select,
        //     {
        //         selectContainer: 'div',
        //         selectAll: false,
        //         selectPlaceholder: 'Role',
        //         // selectLabelRef: this.$refs.label
        //     }, {
        // }
        // )
        // this.$refs.select.addEventListener(
        //     "valueChange.te.select",
        //     (event) => {
        //         this.role_val = event.value
        //         console.log(this.role_val)
        //     }
        // );
    },
    data() {
        return {
            // role_val: []
            val: 0,
            options: [
                {
                    value: '0',
                    label: 'Mom',
                    disable: false
                },
                {
                    value: '1',
                    label: 'Dad',
                    disable: false
                },
                {
                    value: '2',
                    label: 'Nurse',
                    disable: false
                },
            ]
        }
    },
    methods: {
        select_change() {
            if (Object.values(this.val).includes('0')) {
                this.options[1]['disable'] = true
            } else {
                this.options[1]['disable'] = false
            }

            if (Object.values(this.val).includes('1')) {
                this.options[0]['disable'] = true
            } else {
                this.options[0]['disable'] = false
            }
            this.$emit("role_selected", this.val)
        }
    }
}
</script>

<style scoped>


</style>