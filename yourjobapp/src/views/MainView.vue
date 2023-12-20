<template>
  <div :style="{ background: 'url(' + require('@/assets/bg-coklat.png') + ')' }">
    <v-app-bar
      app
      color="#64320C"
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
      <MainPage />
      <v-row style="min-height: 5px; background-color: black;"></v-row>
      <v-row style="min-height: 50px; background-color: white;">
        <v-col cols="12" md="12" class="d-flex align-center justify-center" id="footer">
          Developed By <a href="https://achmadrafifnasution.vercel.app" class="link"> Achmad Rafif Nasution</a>
        </v-col>
      </v-row>
    </v-main>
  </div>
</template>
<script>
import MainPage from '@/components/MainPage.vue'

export default{
    name:'MainView',
    components:{
        MainPage
    },
    mounted(){
        this.ResponsiveAppbar();
        window.addEventListener('resize', this.ResponsiveAppbar);
        this.name = this.$route.params.name
    },
    data(){
        return{
            name:'',
            isMobileView:false,
            items: [
                { title: 'Home',href:'',to:{name:'home'},click:this.Home },
                { title: 'Contact Me',href:'https://achmadrafifnasution.vercel.app/contact',to:'',click:this.Home },
                { title: 'Logout',href:'',to:'',click:this.logOut}
            ],
        }
    },
    methods:{
        ResponsiveAppbar(){
            const isMobile = window.matchMedia('(max-width: 959px)').matches;
            this.isMobileView = isMobile;
        },
        Home(){
            console.log('anda berada di home page')
        },
        logOut(){
            this.$store.dispatch('auth/logout');
            this.$router.push('/');
        },
    }
}
</script>
<style scoped>
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