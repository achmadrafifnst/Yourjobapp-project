<template>
  <!-- <div :style="{ background: 'url(' + require('@/assets/bg-coklat.png') + ')', 'background-size':'cover' }"> -->
    <div>
    <v-app-bar
      app
      style="background-color:rgba(100, 49, 15, 0.8); color:white;"
      dark
      fixed
      class="appBar"
    >

      <h3> Hai, {{ this.name }}</h3>

      <v-spacer></v-spacer>

      <v-btn
        text
        class="hidden-sm-and-down"
        :to="{name:'home'}"
      >
        <span class="ma-0">Home</span>
      </v-btn>
      
      <v-btn
        href="https://achmadrafifnasution.vercel.app/contact"
        text
        class="hidden-sm-and-down"
      >
        <span class="ma-0">Contact Me</span>
      </v-btn>

      <v-btn icon class="hidden-sm-and-down"  @click.prevent="logOut">
        <v-icon>mdi-logout</v-icon>
      </v-btn>

      <v-menu offset-y v-if="isMobileView">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="white"
            dark
            v-bind="attrs"
            v-on="on"
            text
          >
            <v-icon>mdi-menu</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="(item, index) in items"
            :key="index"
            :href="item.href"
            :to="item.to"
            @click="item.click"
          >
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

    </v-app-bar>
    <v-main>
      <HomePage :name="name"/>
      <v-row style="min-height: 5px; background-color: black;"></v-row>
      <v-row style="min-height: 50px; background-color: white;">
        <v-col cols="12" md="12" class="d-flex align-center justify-center" id="footer">
          Develop By <a href="https://achmadrafifnasution.vercel.app" class="link"> Achmad Rafif Nasution</a>
        </v-col>
      </v-row>
    </v-main>
  </div>
</template>

<script>
  import HomePage from '../components/HomePage'
  import HomeServices from '@/services/home-service'

  export default {
    name: 'HomeView',
    mounted(){
      if(this.name==''){
        this.afterLogin();
      }
      // this.afterLogin();
      this.ResponsiveAppbar();
      window.addEventListener('resize', this.ResponsiveAppbar);
    },
    components: {
      HomePage,
    },
    data(){
      return{
        name:'',
        isMobileView :false,
        items: [
          { title: 'Home',href:'',to:{name:'home'},click:this.Home },
          { title: 'Contact Me',href:'https://achmadrafifnasution.vercel.app/contact',to:'',click:this.Home },
          { title: 'Logout',href:'',to:'',click:this.logOut}
        ],
      }
    },
    methods:{
      Home(){
        console.log('anda berada di home page')
      },
      ResponsiveAppbar(){
        const isMobile = window.matchMedia('(max-width: 959px)').matches;
        this.isMobileView = isMobile;
      },
      logOut(){
        this.$store.dispatch('auth/logout');
        this.$router.push('/');
      },
      afterLogin(){
        HomeServices.getHome().then(
          response => {
            console.log(response.data.msg)
            this.name = response.data.name
          },
          error => {
              if(error.response.status==401){
                this.$store.dispatch('auth/logout');
                this.$router.push('/login');
              }
              else if (error.response.status === 500) {
                console.error('Error 500. Refreshing page...');
                window.location.reload(true);
              }
          }
        )
      }
    }
  }
</script>
<style scoped>
/* .appBar{
        padding-right: 40px;
    } */
#footer{
  font-family: 'Times New Roman';
}

#footer .link{
  color: black;
  margin-left:5px;
}

.appBar h3{
  margin-right:20px;
}
</style>