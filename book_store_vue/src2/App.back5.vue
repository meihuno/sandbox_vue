
<template>
  <div id="app">
  <reactive-base app="test_index" url="http://localhost:9200/"  :enableAppbase="true" >
    <h5>検索お試しランチャー</h5>
  <div class="navbar">
     <DataSearch
      componentId="Title"
      iconPosition="right"
      :dataField="[
      'title',
      'text'
      ]"
      className="data-search"
      :showClear="false"
      placeholder="Search for book"
    >
    </DataSearch>
  </div>

     <button class="toggle" @click="switchContainer">
        {{ showBooks ? "Show Filters 💣" : "Show Books 📚" }}
      </button>

  <div class="container">
    <div class="filters-container" :class="{ full: !showBooks }">
    <multi-list
      componentId="Category"
      dataField="category.keyword"
      class="filter"
      title="Select Cateogory"
      aggregationSize=5
      :react="{ and: ['Title', 'Ratings'] }"
    />

    <single-range
      componentId="Ratings"
      dataField="rating"
      :data="[
      { 'start': 0, 'end': 3, 'label': 'Rating < 3' },
      { 'start': 3, 'end': 4, 'label': 'Rating 3 to 4' },
      { 'start': 4, 'end': 5, 'label': 'Rating > 4' }
      ]"
      title="Book Ratings"
      class="filter"
      />
   </div>

    <div :class="{ 'result-list-container': true, full: showBooks }">
    <SelectedFilters />
    <ReactiveList
      componentId="SearchResult"
      dataField="title"
      :pagination="true"
      :from="0"
      :size="8"
      :showResultStats="false"
      className="result-list-container"
      :react="{ and: ['Title', 'Category'] }"
      :innerClass="{ list: 'books-container', poweredBy: 'appbase' }"
>
      <div slot="renderItem" class="book-content" slot-scope="{ item }">
      <p class="book-header">{{ item.title }} - {{item.category}}</p> 
      </div>
    </ReactiveList>
    </div>
  </div>
  </reactive-base> 
  </div>
</template>

<script>
import "./styles.css";
// import text from "raw-loader!./foobar.txt";
//import book from './test.json'

export default {
  // components: {Body, Test}, 
  name: "App",
  data: function() {
    return {
      showBooks: window.innerWidth <= 768 ? true : false
    };
  },

  methods:{  
    switchContainer: function () {
      return (this.showBooks = !this.showBooks);
    },
  },
  computed: {}
}
</script>

<style>

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.data-search{ width: 800px; }

</style>
