<template>
    <div style="height: 100%; background-color: rgb(226, 221, 221);" class="pa-16 align-center justify-center">
        <v-row align-center class="d-flex align-center justify-center">
            <v-col cols="12" md="12" class="pa-auto">
                <v-card class="pa-3 mx-auto" id="card-container">
                    <v-form @submit.prevent="validate" ref="form" lazy-validation v-model="valid">
                        <v-col>
                            <v-row class="d-flex align-center justify-center mb-10">
                                <h1>Sign In</h1>
                            </v-row>
                            <v-row class="d-flex align-center justify-center">
                                <v-col cols="12" md="10" sm="12">
                                    <v-text-field 
                                        color="primary" 
                                        v-model="userName" 
                                        :rules="userNameRules" 
                                        outlined
                                        label="Enter your username" 
                                        style="border-radius: 15px;"
                                        required 
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="d-flex align-center justify-center">
                                <v-col cols="12" md="10" sm="12">
                                    <v-text-field 
                                        color="primary" 
                                        v-model="password" 
                                        :rules="passwordRules" 
                                        outlined
                                        type="password"
                                        label="Enter your password" 
                                        style="border-radius: 15px;"
                                        required 
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row class="button-row-container d-flex justify-center align-center">
                                <v-col cols="12" md="4">
                                    <v-btn 
                                        elevation="0" 
                                        color="rgb(49, 43, 43)" 
                                        tile 
                                        type="submit" 
                                        class="pa-6"
                                        :style="{
                                                'color':'#ecf0f1',
                                                'border-radius':'15px'
                                                }" 
                                    >
                                        Login
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-form>
                </v-card>
            </v-col>
        </v-row>
        <v-snackbar 
            v-model="snackbar" 
        >
            {{ this.info }}
            <template v-slot:action="{attrs}">
                <v-btn
                    :color="colorInfo"
                    text
                    v-bind="attrs"
                    @click="failCloseSnackbar"
                >
                    Close
                </v-btn>
            </template>
        </v-snackbar>
    </div>
</template>
<script>
// import axios from 'axios';
// import useVuelidate from '@vuelidate/core';
// import {required} from '@vuelidate/validators';

export default{
    name:'LoginView',
    data(){
        return{
            valid:true,
            snackbar:false,
            colorInfo:'',
            info:'',
            userName:'',
            userNameRules: [
                v => !!v || 'Username is required',
                v => (v && v.length >= 3) || 'Username must be min 3 characters',
            ],
            password:'',
            passwordRules: [
                v => !!v || 'Password is required',
                v => (v && v.length >= 8) || 'Password must be min 8 characters',
            ],
        }
    },
    // setup:() => ({v$:useVuelidate()}),
    created() {
        if (this.loggedIn) {
            this.$router.push('/home');
        }
    },
    methods:{
        validate(){
            // const result = await this.v$.$validate();
            if( this.userName != '' && this.password != ''){
                // const {userName,password} = this
                const user = {'username':this.userName,'sandi':this.password}
                this.handleLogin(user)
            }else{
                this.info = 'Login, Error'
                console.log(this.info)
            }

            // const submitForm = this.$refs.form.validate()
            // if (submitForm){
                
            //     const data = {
            //         'username':this.userName,
            //         'sandi': this.password
            //     }
            //     axios.post('https://rafif.pythonanywhere.com/api/rafif/yourjobapp/login',data)
            //     .then(
            //         response => {
            //             if( response.data.status == '1'){
            //                 console.log(response.data.msg)
            //                 this.info = response.data.msg
            //                 this.colorInfo = '#2FBA39'
            //                 this.snackbar = true
            //                 this.$router.push('/home');
                            
            //             }
            //         }
            //     ).catch(
            //         error => {
            //             var errStatus = error.response.status
            //             if (errStatus == 401){
            //                 console.log(error.response.data.msg)
            //                 this.info = error.response.data.msg
            //                 this.colorInfo = '#E02E2E'
            //                 this.snackbar = true
            //             }
            //             else if(errStatus == 400){
            //                 console.log(error.response.data.msg)
            //                 this.info = error.response.data.msg
            //                 this.colorInfo = '#E02E2E'
            //                 this.snackbar = true
            //             }
            //         }
            //     )
            // }
        },
        handleLogin(user){
            this.$store.dispatch("auth/login",user).then(
                response => {
                    
                    if(response.access_token){
                        this.$router.push("/home");
                    }
                },
                error => {
                    console.log(error.toString())
                }
            )
        },
        failCloseSnackbar(){
            this.snackbar = false
            this.info = ''
            this.colorInfo = ''
        }
    },
    // validations() {
    //     return {
    //     userName: { required },
    //     password: { required }
    //     }
    // },
    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        },
    }
}

</script>

<style scoped>
h1{
    font-size: 300%; 
    color:rgb(87, 75, 75); 
    text-shadow:0px 3px 3px rgb(48, 43, 43);
}
.button-row-container{
    padding-left: 0%;
}
#card-container{
    border-radius: 15px; 
    max-width: 30vw; 
    background-color: rgba(117, 78, 26 ,0.3);
}
@media screen and (max-width:600px) {
    #card-container{
        max-width: 70vw;
    }
    .button-row-container{
        padding-left: 0%;
    }
    h1{
        font-size:200%;
    }
}
</style>