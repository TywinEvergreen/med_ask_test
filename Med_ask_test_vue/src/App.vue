<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<script>
    export default {
        name: 'App'
    }
</script>

<style>
    a {
        cursor: pointer;
        color: #000;
    }
    .md-autocomplete, .md-field {
        box-shadow: 0.5px 1px 3px;
        border-radius: 10px;
    }

    .md-content {
        width: 80px;
        height: 60px;
        margin: 24px;
        box-shadow: 0 0 5px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        margin: 20%;
        padding: 3%;
        box-shadow: 2px 1px 30px;
        border-radius: 10px;
        text-align: center;
        color: #2c3e50;
    }
</style>
