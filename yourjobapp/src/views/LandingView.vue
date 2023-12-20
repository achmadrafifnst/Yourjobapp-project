<template>
    <div class="landing-container" style="height: 100vh; font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
        <v-card style="height:100%; background-color: rgba(0,0,0,0);" class="pa-3">
            <v-row class="d-flex align-center justify-center text-center" style="height: 100%;">
                <div class="container-title">
                    <h1>Welcome!</h1>
                    <h3>Find your job with us and get your financial freedom</h3>
                    <v-btn :to="{name:'login'}" style="color:white;background-color: rgb(49, 43, 43); border-radius: 15px;" class="mx-6 mb-3 mt-6 pa-6">
                        Sign In
                    </v-btn>
                    <v-btn :to="{name:'register'}" style="color:white;background-color: rgb(49, 43, 43); border-radius: 15px;" class="mx-3 mb-3 pa-6">
                        Sign Up
                    </v-btn>
                </div>
            </v-row>
        </v-card>
    </div>
</template>
<style scoped>
.landing-container{
    background: url('../assets/bg_landing_page.jpg') center center fixed;
    background-size: cover;
}
h1{
    font-size: 400%; 
    margin-top: -100px; 
    color:rgb(212, 210, 210); 
    text-shadow:0px 3px 3px rgb(46, 40, 40);
}
h3{
    font-size: 170%; 
    color:rgb(212, 210, 210); 
    text-shadow:0px 3px 3px rgb(46, 40, 40);
}
.container-title{
    display: flex; 
    flex-direction: column; 
    align-items: center; 
    max-width: 40%;
}
@media screen and (max-width:600px){
    .container-title{
        max-width: 70%;
    }
}
</style>