<template>
    <div class="bg-no-repeat bg-cover w-full h-screen bg-neutral-200">
        <!-- absolute inset-x-0  -->
        <div class=" bg-neutral-50 grid grid-cols-1 grid-rows-2">
            <p class="text-center text-lg font-bold font-sans pt-10 row-start-1 row-span-2  col-start-1 col-span-1">帳戶</p> 
        </div>
        <div class=" my-8 mx-4">
            <p class="text-start text-xl font-bold font-sans ">用戶</p>
            <div class="rounded-lg bg-neutral-50 w-full">
                <account-settings-banner-basic></account-settings-banner-basic>
                <account-settings-banner-basic></account-settings-banner-basic>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    
}
</script>
<style lang="scss">
    
</style>