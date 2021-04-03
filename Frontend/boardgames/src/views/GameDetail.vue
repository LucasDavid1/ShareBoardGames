<template>
    <div class="container">
        <h4>{{ game.name }}</h4>
        <p>Rating: {{ game.average.toFixed(2) }}</p>
        <p>{{ game.description }}</p>
    </div>
</template>

<script>
//import mongoDB from '@services/mongoDB.js'

export default {
    data() {
        return {
            game: ""
        }
    },
    created() {
        console.log(this.$route.params.game)
        this.game = this.$route.params.game
    }
}
</script>
