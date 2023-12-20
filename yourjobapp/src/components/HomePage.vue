<template>
  <v-container>
      <!-- <v-app-bar
        app
        color="#64320C"
        dark
        class="appBar"
      >
        <v-spacer></v-spacer>

        <v-btn icon class="btnAppBar"  @click.prevent="logOut">
          <v-icon small>mdi-logout</v-icon>
            Logout
        </v-btn>
      </v-app-bar> -->
      <v-row>
        <!-- <v-col cols="12" md="1"> </v-col> -->
        <v-col cols="12" md="4" class="d-flex align-center justify-center">
          <v-card class="align-center justify-center pa-3" id="container-info">
            <v-img src="../assets/skills (1).png" />
            <h2 class="mt-10">Identify your career potential</h2>
            <p>You only need to choose the answer that suits your skills. Your skills will help you to find the job that fit you.</p>
          </v-card>
        </v-col>
        <!-- <v-col cols="12" md="1"> </v-col> -->
        <v-col cols="12" md="4" class="d-flex align-center justify-center">
          <v-card class="align-center justify-center pa-3" id="container-info">
            <v-img src="../assets/analysis.png" />
            <h2 class="mt-10">Scientific Method</h2>
            <p>This test is developed using logistic regression method, so that the recommendation can be trusted.</p>
          </v-card>
        </v-col>
        <!-- <v-col cols="12" md="1"> </v-col> -->
        <v-col cols="12" md="4" class="d-flex align-center justify-center">
          <v-card class="align-center justify-center pa-3" id="container-info">
            <v-img src="../assets/booking.png" />
            <h2 class="mt-10">Easy to use</h2>
            <p>This test feature is very easy to use, only need internet access, and can be done anywhere.</p>
          </v-card>
        </v-col>
        <!-- <v-col cols="12" md="1"> </v-col> -->
      </v-row>
      <v-row class="container-button">
        <v-col cols="12" md="12" class="d-flex align-center justify-center">
          <v-btn :to="{name:'main',params: { name: name }}" style="color:white;background-color: rgb(49, 43, 43); border-radius: 15px;" class="mx-3 mb-3 pa-6">
            Take the test !
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
  

  export default {
    name: 'HomePage',
    props:['name'],
    mounted(){
    },
    data: () => ({
    }),
    methods:{
      
    }
  }
</script>
<style scoped>
h2, p {
    text-align: center;
}
#container-info{
  max-width: 25vw;
  /* min-height: 90vh; */
  border-radius: 15px 15px 15px 15px;
}
.container-button{
  margin-top: 100px;
  margin-bottom: 100px;
}
@media screen and (max-width : 600px) {
  #container-info{
    max-width: 100vw;
    min-height: 10vh;
  }
}
</style>
