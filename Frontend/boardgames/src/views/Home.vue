<template>
  <div class="home">    
    <div class="row container">
      <el-input
        placeholder="Buscar juego"
        prefix-icon="el-icon-search"
        v-model="searchGameName.name">
        <el-button slot="append" icon="el-icon-search" @click="searchGame"></el-button>
      </el-input>      
    </div>    
    <!-- <div class="row" v-for="category in categories" v-if="!searchGameName.search">
      <div class="container">
        <div class="row">
          <div class="col-sm-2">
            <h5>{{ category }}</h5>        
          </div>  
          <div class="col-sm-10"></div>    
        </div>        
        <div class="row" v-if="games.find(x => x.category === category)">
          <div 
            class="col-sm-3 mr-1 mt-1 game-box" 
            v-loading="loading"
            @click="toGameDetail(specific_game)"
            v-for="specific_game in games.find(x => x.category === category).games_getted">
            {{ specific_game.name }}
          </div>
        </div>
        <div class="row mt-0 mb-0">
          <div class="col-sm-12">
            <hr style="border-top: 1px solid #a6c8ea">    
          </div>          
        </div>        
      </div>
    </div>  -->
    <div 
      class="row" 
      v-if="!searchGameName.search"
      v-for="category in categories"
      :key="category">
      <div class="container">
        <div class="row">
          <h5>{{ category }}</h5>        
        </div>
        <div class="row" v-if="games.find(x => x.category === category)">
          <div 
            class="col-sm mr-1 mt-1">
            <ul id="hexGrid">
              <li class="hex" 
                v-for="specific_game in games.find(x => x.category === category).games_getted"
                :key="specific_game.name"
                @click="toGameDetail(specific_game)">
                <a class="hexIn">
                  <img src="https://farm8.staticflickr.com/7187/6895047173_d4b1a0d798.jpg"/>
                  <h1>{{ specific_game.name }}</h1>
                  <p>{{ specific_game.description }}</p>
                </a>
              </li>
            </ul>
          </div>          
        </div>
      </div>      
    </div>
    <div class="row" v-else>
      <div class="container">
        <div 
          class="row game-box" 
          v-for="game in searchGameName.gamesFetched"
          :key="game.name"
          @click="toGameDetail(game)">
          <p>{{ game.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import mongoDB from "@/services/mongoDB.js";

export default {
  name: 'Home',
  data () {
    return {
      loading: true,
      games: [],
      categories: [],
      limit: 100,
      searchGameName: {search: false, name: "", gamesFetched: []}
    }
  },
  created() {
    mongoDB
      .getCategories(6) // Se trae 6 categorias de juegos.
      .then(response => {
        this.categories = response
        mongoDB
        .getGamesByCategories(this.limit, response) // Se trae 'limit' juegos por categoria.
        .then(gamesGetted => {
          this.games = gamesGetted
        })        
      })            
  },
  methods: {
    searchGame() {
      mongoDB
      .getGamesByName(this.limit, this.searchGameName.name)
      .then(gamesGetted => {
        console.log(gamesGetted)
        this.searchGameName.search = true
        this.searchGameName.gamesFetched = gamesGetted
      })
    },
    toGameDetail(game) {
      this.$router.push({name: "GameDetail", params: {game: game}})
    }
  }
};
</script>
