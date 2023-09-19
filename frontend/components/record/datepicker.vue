<template>
      <div
      class="relative"
      v-show="datepicker_show"
      ref="date_picker"
      >

      <input
        type="text"
        class="block w-full rounded  bg-transparent px-3 py-1 data-[te-input-state-active] font-bold" :value="default_date"
        style="background-color: #EEEEEF; color: black;" />
    </div>
  </template>

<script>
  import { Datepicker, Input, initTE } from "tw-elements";

  export default {
    props:["default_date"],
    created() {
      initTE({ Datepicker, Input })
    },
    mounted() {
      new Datepicker(
        this.$refs.date_picker, {
          format: "yyyy/mm/dd",
          startDate: this.date,
          // inline: true
          disableFuture: true,
          disableInput: false
        }, {
          datepickerToggleButton: 'flex items-center justify-content-center [&>svg]:w-5 [&>svg]:h-5 absolute outline-none border-none bg-transparent right-0.5 top-1/2 -translate-x-1/2 -translate-y-1/2 text-black dark:text-black',
          datepickerCell: 'text-center data-[te-datepicker-cell-disabled]:text-neutral-300 data-[te-datepicker-cell-disabled]:cursor-default data-[te-datepicker-cell-disabled]:pointer-events-none data-[te-datepicker-cell-disabled]:hover:cursor-default hover:cursor-pointer group data-[te-datepicker-cell-focused]:border-black border-black data-[te-datepicker-cell-disabled]:border-black',
          datepickerDropdownContainer: 'w-[328px] h-[380px] bg-white rounded-lg shadow-[0px_2px_15px_-3px_rgba(0,0,0,.07),_0px_10px_20px_-2px_rgba(0,0,0,.04)] z-[1066] dark:bg-zinc-700'
        }
      );

      this.$refs.date_picker.addEventListener(
        "dateChange.te.datepicker", 
        (event) => this.date_picker_change(event)
      );

      this.datepicker_show = true
    },
    data() {
      return {
        date: this.default_date,
        datepicker_show: false,
      }
    },
    methods: {
      date_picker_change(event) {
        let date_str = this.get_date_str(event)
        this.$emit("date_picker_change", date_str)
      },



      get_date_str(event) {
        let year = event.date.getFullYear() // 西元年
        let month = event.date.getMonth()+1 // 月的indx (+1後才是真正的月份)
        let date = event.date.getDate() // 日
        // console.log(event.date.getDay()); 星期幾

        if (month<10) {
          month = '0'+String(month)
        } else {
          month = String(month)
        }

        if (date<10) {
          date = '0'+String(date)
        } else {
          date = String(date)
        }

        let date_str = String(year)+'-'+month+'-'+date
        this.date = date_str
        return date_str
      }
    },
  }
</script>
