<template>
    <v-container>
        <v-form @submit.prevent="onClickResult" ref="form" lazy-validation v-model="valid">
        <v-row>
            <v-col cols="12" md="12" class="d-flex align-center justify-center">
                <v-card min-width="50vw" class="pa-16" style="border-radius:30px; background-color: rgba(100, 90, 90,0.5);">
                    <v-row>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_1"
                                outlined
                                label="Skill 1"
                                required
                                color="primary"
                                :rules="rulesSkill_1"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_2"
                                outlined
                                label="Skill 2"
                                required
                                color="primary"
                                :rules="rulesSkill_2"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_3"
                                outlined
                                label="Skill 3"
                                required
                                color="primary"
                                :rules="rulesSkill_3"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_4"
                                outlined
                                label="Skill 4"
                                required
                                color="primary"
                                :rules="rulesSkill_4"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_5"
                                outlined
                                label="Skill 5"
                                required
                                color="primary"
                                :rules="rulesSkill_5"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_6"
                                outlined
                                label="Skill 6"
                                required
                                color="primary"
                                :rules="rulesSkill_6"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_7"
                                outlined
                                label="Skill 7"
                                required
                                color="primary"
                                :rules="rulesSkill_7"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_8"
                                outlined
                                label="Skill 8"
                                required
                                color="primary"
                                :rules="rulesSkill_8"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                    </v-row>
                    <v-row style="margin-bottom:-50px;">
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_9"
                                outlined
                                label="Skill 9"
                                required
                                color="primary"
                                :rules="rulesSkill_9"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-autocomplete
                                v-model="skill_10"
                                outlined
                                label="Skill 10"
                                required
                                color="primary"
                                :rules="rulesSkill_10"
                                :items="itemSelect"
                                item-value="label"
                                item-text="label"
                            >
                            </v-autocomplete>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" md="12" class="d-flex align-center justify-center">
                <v-btn
                    elevation="0" 
                    color="rgb(49, 43, 43)" 
                    tile 
                    type="submit" 
                    class="pa-6 mb-16"
                    href="#hasil"
                    @click="onClickResult"
                    :style="{
                        'color':'#ecf0f1',
                        'border-radius':'15px'
                    }" 
                >
                    See the result
                </v-btn>
            </v-col>    
        </v-row>
        </v-form>
        <v-row height="100vh" id="hasil" class="my-16" >
            <v-col cols="12" md="12" class="d-flex align-center justify-center" v-if=isResult>
                <v-card min-width="80%" style="border-radius:30px;background-color: white;" class="pa-16">
                    <v-row>
                        <!-- <v-col cols="12" md="12" class="d-flex align-center justify-center mb-10">
                            <p>1. {{ this.rekomen_1 }}</p>
                        </v-col>
                        <v-col cols="12" md="12" class="d-flex align-center justify-center" style="margin-top:-50px;">
                            <v-img :src="require(`@/assets/${this.gambar_1}.png`)" max-width="20%"/>
                        </v-col> -->
                        <v-col cols="12" md="3"> </v-col>
                        <v-col cols="12" md="6" class="d-flex align-center justify-center mb-10">
                            <v-row>
                                <v-col cols="12" md="12" class="d-flex align-center justify-center">
                                    <p>1. {{ this.rekomen_1 }}</p>
                                </v-col>
                                <v-col cols="12" md="12" class="d-flex align-center justify-center">
                                    <v-img :src="require(`@/assets/${this.gambar_1}.png`)" max-width="40%"/>
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12" md="3"> </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" md="6" class="d-flex align-center justify-center mb-10">
                            <v-row>
                                <v-col cols="12" md="12" class="d-flex align-center justify-center">
                                    <p>2. {{ this.rekomen_2 }}</p>
                                </v-col>
                                <v-col cols="12" md="12" class="d-flex align-center justify-center">
                                    <v-img :src="require(`@/assets/${this.gambar_2}.png`)" max-width="40%"/>
                                </v-col>
                            </v-row>
                        </v-col>
                        <v-col cols="12" md="6" class="d-flex align-center justify-center mb-10">
                            <v-row>
                                <v-col cols="12" md="12" class="d-flex align-center justify-center">
                                    <p>3. {{ this.rekomen_3 }}</p>
                                </v-col>
                                <v-col cols="12" md="12" class="d-flex align-center justify-center">
                                    <v-img :src="require(`@/assets/${this.gambar_3}.png`)" max-width="40%"/>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                    <!-- <v-row style="margin-top:-50px;">
                        <v-col cols="12" md="6" class="d-flex align-center justify-center">
                            <v-img :src="require(`@/assets/${this.gambar_2}.png`)" max-width="40%"/>
                        </v-col>
                        <v-col cols="12" md="6" class="d-flex align-center justify-center">
                            <v-img :src="require(`@/assets/${this.gambar_3}.png`)" max-width="40%"/>
                        </v-col>
                    </v-row> -->
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import HomeServices from '@/services/home-service'

export default{
    name:'MainPage',
    mounted(){
        this.afterHome();
    },
    methods:{
        afterHome(){
            HomeServices.getMain().then(
                response => {
                    console.log(response.data.msg)
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
        },
        onClickResult(){
            const submitform = this.$refs.form.validate()
            if(submitform){
                const data = {
                    'skill_1':this.skill_1,
                    'skill_2':this.skill_2,
                    'skill_3':this.skill_3,
                    'skill_4':this.skill_4,
                    'skill_5':this.skill_5,
                    'skill_6':this.skill_6,
                    'skill_7':this.skill_7,
                    'skill_8':this.skill_8,
                    'skill_9':this.skill_9,
                    'skill_10':this.skill_10
                }
                HomeServices.submitForm(data).then(
                    response => {
                        if(response.data!=null){
                            this.gambar_1 = response.data.gambar_1
                            this.gambar_2 = response.data.gambar_2
                            this.gambar_3 = response.data.gambar_3
                            this.rekomen_1 = response.data.rekomen_1
                            this.rekomen_2 = response.data.rekomen_2
                            this.rekomen_3 = response.data.rekomen_3
                            this.isResult=true
                        }
                    }
                )
            }
            
        }
    },
    data(){
        return{
            gambar_1:'',
            gambar_2:'',
            gambar_3:'',
            rekomen_1:'',
            rekomen_2:'',
            rekomen_3:'',
            valid:true,
            isResult:false,
            skill_1:null,
            rulesSkill_1:[
                v => !!v || 'Skill 1 is required',
                v => (v && v!=null) || 'Skill 1 must be selected'
            ],
            skill_2:null,
            rulesSkill_2:[
                v => !!v || 'Skill 2 is required',
                v => (v && v!=null) || 'Skill 2 must be selected'
            ],
            skill_3:null,
            rulesSkill_3:[
                v => !!v || 'Skill 3 is required',
                v => (v && v!=null) || 'Skill 3 must be selected'
            ],
            skill_4:null,
            rulesSkill_4:[
                v => !!v || 'Skill 4 is required',
                v => (v && v!=null) || 'Skill 4 must be selected'
            ],
            skill_5:null,
            rulesSkill_5:[
                v => !!v || 'Skill 5 is required',
                v => (v && v!=null) || 'Skill 5 must be selected'
            ],
            skill_6:null,
            rulesSkill_6:[
                v => !!v || 'Skill 6 is required',
                v => (v && v!=null) || 'Skill 6 must be selected'
            ],
            skill_7:null,
            rulesSkill_7:[
                v => !!v || 'Skill 7 is required',
                v => (v && v!=null) || 'Skill 7 must be selected'
            ],
            skill_8:null,
            rulesSkill_8:[
                v => !!v || 'Skill 8 is required',
                v => (v && v!=null) || 'Skill 8 must be selected'
            ],
            skill_9:null,
            rulesSkill_9:[
                v => !!v || 'Skill 9 is required',
                v => (v && v!=null) || 'Skill 9 must be selected'
            ],
            skill_10:null,
            rulesSkill_10:[
                v => !!v || 'Skill 10 is required',
                v => (v && v!=null) || 'Skill 10 must be selected'
            ],
            itemSelect:[
                {
                    'id':'0',
                    'label':'architectures'
                },
                {
                    'id':'1',
                    'label':'attorney'
                },
                {
                    'id':'2',
                    'label':'business analyst'
                },
                {
                    'id':'3',
                    'label':'counselor'
                },
                {
                    'id':'4',
                    'label':'criminal investigations'
                },
                {
                    'id':'5',
                    'label':'editor'
                },
                {
                    'id':'6',
                    'label':'flight instructor'
                },
                {
                    'id':'7',
                    'label':'machine learning'
                },
                {
                    'id':'8',
                    'label':'web designer'
                },
                {
                    'id':'9',
                    'label':'writer'
                },
                {
                    'id':'10',
                    'label':'architectural design'
                },
                {
                    'id':'11',
                    'label':'arranger'
                },
                {
                    'id':'12',
                    'label':'home offices'
                },
                {
                    'id':'13',
                    'label':'lecturer'
                },
                {
                    'id':'14',
                    'label':'mediator'
                },
                {
                    'id':'15',
                    'label':'patrol'
                },
                {
                    'id':'16',
                    'label':'photographer'
                },
                {
                    'id':'17',
                    'label':'piloting'
                },
                {
                    'id':'18',
                    'label':'producer'
                },
                {
                    'id':'19',
                    'label':'programmer'
                },
                {
                    'id':'20',
                    'label':'r'
                },
                {
                    'id':'21',
                    'label':'big data'
                },
                {
                    'id':'22',
                    'label':'composer'
                },
                {
                    'id':'23',
                    'label':'construction disputes'
                },
                {
                    'id':'24',
                    'label':'crime prevention'
                },
                {
                    'id':'25',
                    'label':'design durable'
                },
                {
                    'id':'26',
                    'label':'director'
                },
                {
                    'id':'27',
                    'label':'flying'
                },
                {
                    'id':'28',
                    'label':'java programmer'
                },
                {
                    'id':'29',
                    'label':'teacher'
                },
                {
                    'id':'30',
                    'label':'webfocus'
                },
                {
                    'id':'31',
                    'label':'actor'
                },
                {
                    'id':'32',
                    'label':'advocate'
                },
                {
                    'id':'33',
                    'label':'data mining'
                },
                {
                    'id':'34',
                    'label':'design urban'
                },
                {
                    'id':'35',
                    'label':'evidence'
                },
                {
                    'id':'36',
                    'label':'graphic designer'
                },
                {
                    'id':'37',
                    'label':'instrument rated pilot'
                },
                {
                    'id':'38',
                    'label':'mis reporting'
                },
                {
                    'id':'39',
                    'label':'reporter'
                },
                {
                    'id':'40',
                    'label':'researcher'
                },
                {
                    'id':'41',
                    'label':'aviation'
                },
                {
                    'id':'42',
                    'label':'communication skill'
                },
                {
                    'id':'43',
                    'label':'design architectural'
                },
                {
                    'id':'44',
                    'label':'educator'
                },
                {
                    'id':'45',
                    'label':'enforcement'
                },
                {
                    'id':'46',
                    'label':'journalism'
                },
                {
                    'id':'47',
                    'label':'legal advice'
                },
                {
                    'id':'48',
                    'label':'python'
                },
                {
                    'id':'49',
                    'label':'webmaster'
                },
                {
                    'id':'50',
                    'label':'apache spark'
                },
                {
                    'id':'51',
                    'label':'author'
                },
                {
                    'id':'52',
                    'label':'copywriter'
                },
                {
                    'id':'53',
                    'label':'criminal justice'
                },
                {
                    'id':'54',
                    'label':'dancer'
                },
                {
                    'id':'55',
                    'label':'interpersonal communications'
                },
                {
                    'id':'56',
                    'label':'journalist'
                },
                {
                    'id':'57',
                    'label':'litigation'
                },
                {
                    'id':'58',
                    'label':'php'
                },
                {
                    'id':'59',
                    'label':'plan darchitecture'
                },
                {
                    'id':'60',
                    'label':'single engine land'
                },
                {
                    'id':'61',
                    'label':'cameraman'
                },
                {
                    'id':'62',
                    'label':'css'
                },
                {
                    'id':'63',
                    'label':'field training officer'
                },
                {
                    'id':'64',
                    'label':'freelancer'
                },
                {
                    'id':'65',
                    'label':'law firm administration'
                },
                {
                    'id':'66',
                    'label':'multiengine land'
                },
                {
                    'id':'67',
                    'label':'predictive analytics'
                },
                {
                    'id':'68',
                    'label':'speaker'
                },
                {
                    'id':'69',
                    'label':'sustainable architecture'
                },
                {
                    'id':'70',
                    'label':'administrator'
                },
                {
                    'id':'71',
                    'label':'attorneys'
                },
                {
                    'id':'72',
                    'label':'awardwinning writer'
                },
                {
                    'id':'73',
                    'label':'community policing'
                },
                {
                    'id':'74',
                    'label':'discrepancy resolution'
                },
                {
                    'id':'75',
                    'label':'flight training'
                },
                {
                    'id':'76',
                    'label':'hadoop'
                },
                {
                    'id':'77',
                    'label':'public speaker'
                },
                {
                    'id':'78',
                    'label':'sustainable design'
                },
                {
                    'id':'79',
                    'label':'web development'
                },
                {
                    'id':'80',
                    'label':'aircraft'
                },
                {
                    'id':'81',
                    'label':'customer relation'
                },
                {
                    'id':'82',
                    'label':'data visualization'
                },
                {
                    'id':'83',
                    'label':'design research'
                },
                {
                    'id':'84',
                    'label':'filmmaker'
                },
                {
                    'id':'85',
                    'label':'interrogation'
                },
                {
                    'id':'86',
                    'label':'javascript'
                },
                {
                    'id':'87',
                    'label':'legal counseling'
                },
                {
                    'id':'88',
                    'label':'novelist'
                },
                {
                    'id':'89',
                    'label':'performer'
                },
                {
                    'id':'90',
                    'label':'adaptive reuse'
                },
                {
                    'id':'91',
                    'label':'big data analytics'
                },
                {
                    'id':'92',
                    'label':'commercial piloting'
                },
                {
                    'id':'93',
                    'label':'corporate law'
                },
                {
                    'id':'94',
                    'label':'firearms'
                },
                {
                    'id':'95',
                    'label':'social worker'
                },
                {
                    'id':'96',
                    'label':'sviluppo web'
                }
                
            ]
        }
    }
}

</script>
<style scoped>
@media screen and (max-width:600px) {
    #gambar1{
        max-width:40vw;
    }
}
</style>