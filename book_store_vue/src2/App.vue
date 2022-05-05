<template>
<!-- 
  https://codesandbox.io/s/o4yy06?file=/src/App.vue:2649-3365
-->
  <div id="app">
    <ReactiveBase
      app="test_index"
      url="http://localhost:9200/"  
    >
    
    <div class="navbar">
        <h2><span class="logo">Bs</span>BookSearch</h2>
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
    <div class="focus-shortcut" slot="addonAfter">/</div>
    </DataSearch>
    </div>

      <button class="toggle" @click="switchContainer">
        {{ showBooks ? "Show Filters 💣" : "Show Books 📚" }}
      </button>

      <div class="container">
        <div class="filters-container" :class="{ full: !showBooks }">
          <MultiList
      componentId="Category"
      dataField="category.keyword"
      class="filter"
      title="Select Cateogory"
      :react="{ and: ['Title', 'Ratings'] }"
          />
          <!--
          <SingleRange
            componentId="Ratings"
            dataField="average_rating"
            :data="[
              { start: 0, end: 3, label: 'Rating < 3' },
              { start: 3, end: 4, label: 'Rating 3 to 4' },
              { start: 4, end: 5, label: 'Rating > 4' },
            ]"
            title="Book Ratings"
            class="filter"
          />
          -->
        </div>
        <div :class="{ 'result-list-container': true, full: showBooks }">
          <SelectedFilters />
          <ReactiveList
            componentId="SearchResult"
            dataField="title"
            :pagination="true"
            :from="0"
            :size="8"
            :showResultStats="true"
            :react="{ and: ['Ratings', 'Category', 'Title'] }"
            :innerClass="{ list: 'books-container', poweredBy: 'appbase' }"
          >
            <div slot="renderItem" class="book-content" slot-scope="{ item }">

              <a
                key="item._id"
                target="_blank"
                :href="
                  'https://www.google.com/search?q=' +
                  item.title.replace(' ', '+')
                "
              >
                <div class="image">
                  <img :src="item.image" alt="Book Cover" class="book-image" />
                  <div class="rating">
                    {{ 1 }} ⭐️
                  </div>
                  <div class="details">
                    <h4 class="book-header">{{ item.title }}</h4>
                    <p>By {{ item.category }}</p>
                  </div>
                </div>
              </a>

              <!--
               <p class="book-header">{{ item.title }} - {{item.category}}</p> 
                  <div class="details">
                    <h4 class="book-header">{{ item.title }}</h4>
                    <p>By {{ item.category }}</p>
                  </div>
              -->

            </div>
          </ReactiveList>
        </div>
      </div>
    </ReactiveBase>
  </div>
</template>

<script>
import "./styles.css";
export default {
  name: "app",
  data: function () {
    return {
      showBooks: window.innerWidth <= 768 ? true : false,
    };
  },
  methods: {
    switchContainer: function () {
      return (this.showBooks = !this.showBooks);
    },
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
