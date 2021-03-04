<template>
    <div id="app">
        <router-view />
    </div>
</template>

<script>
    export default {
        name: 'App',
    }
</script>

<style>
    body {
        margin: 0px;
        padding: 0px;
        height: 100%;
        width: 100vw;
        overflow: hidden;
        padding-right: calc(100vw - 100%);
    }

    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
    }
</style>
